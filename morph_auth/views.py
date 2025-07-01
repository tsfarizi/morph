from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model
from morph_auth.models import LessonProgress
from django.utils import timezone
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

def serialize_lesson_progress(user):
    return [
        {
            "date": progress.date,
            "title": progress.title,
            "page": progress.page
        }
        for progress in user.lesson_progress.all()
    ]


class RegisterView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user": {
                "email": user.email,
                "username": user.username,
                "lesson_progress": serialize_lesson_progress(user)
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user": {
                "email": user.email,
                "username": user.username,
                "lesson_progress": serialize_lesson_progress(user)
            }
        }, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "email": user.email,
            "username": user.username,
            "lesson_progress": serialize_lesson_progress(user)
        }
        return Response(data)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        data = request.data
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        if "password" in data:
            user.set_password(data["password"])
        user.save()
        return Response({"detail": "User updated successfully."}, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.is_active = False
        user.save(update_fields=["is_active"])
        return Response({"detail": "User deactivated (soft-deleted)."}, status=status.HTTP_204_NO_CONTENT)

class UserLessonProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        title = request.data.get("title")
        page = request.data.get("page")

        if not title or not page:
            return Response({"error": "Both 'title' and 'page' are required."}, status=status.HTTP_400_BAD_REQUEST)

        progress, _ = LessonProgress.objects.update_or_create(
            user=user,
            title=title,
            defaults={
                "page": page,
                "date": timezone.now().date()
            }
        )

        return Response({
            "date": progress.date,
            "title": progress.title,
            "page": progress.page
        }, status=status.HTTP_200_OK)
