from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils import timezone

from .serializers import ChatSerializer
from morph_ai.rag.chat_service import run_chat


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser = ChatSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        role = ser.validated_data["role"]
        question = ser.validated_data["content"]
        timestamp = ser.validated_data.get("timestamp", timezone.now())

        if role != "user":
            return Response(
                {"error": "Hanya role 'user' yang diperbolehkan."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            answer, rec = run_chat(request.user, question, timestamp=timestamp)
        except Exception as e:
            return Response(
                {"role": "system", "content": f"Terjadi kesalahan internal: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        response = {
            "role": "ai",
            "content": answer
        }

        if rec:
            response["recommended_lesson"] = rec  
        return Response(response)


class UserChatLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = request.user.chat_logs.order_by('-timestamp')
        data = [
            {
                "role": log.role,
                "content": log.content,
                "timestamp": log.timestamp
            }
            for log in logs
        ]
        return Response(data, status=status.HTTP_200_OK)
