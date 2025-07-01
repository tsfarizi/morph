from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from morph_lesson.models import Lesson, Page


class LessonView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, title=None, page_number=None):
        def build_file_info(page_obj):
            return page_obj.filename, page_obj.file_url 

        if title and page_number is not None:
            try:
                lesson = Lesson.objects.get(title__iexact=title)
            except Lesson.DoesNotExist:
                return Response({"error": "Lesson not found."}, status=status.HTTP_404_NOT_FOUND)

            try:
                page = lesson.pages.get(page=page_number)
            except Page.DoesNotExist:
                return Response({"error": "Page not found in lesson."}, status=status.HTTP_404_NOT_FOUND)

            filename, file_url = build_file_info(page)
            return Response({
                "lesson": lesson.title,
                "page": {
                    "page": page.page,
                    "title": page.title,
                    "filename": filename,
                    "file_url": file_url
                }
            }, status=status.HTTP_200_OK)

        if request.query_params.get("only_titles") == "true":
            titles = Lesson.objects.values_list("title", flat=True)
            return Response(list(titles), status=status.HTTP_200_OK)

        lessons = Lesson.objects.prefetch_related("pages").all()
        data = []
        for lesson in lessons:
            pages = []
            for page in lesson.pages.all():
                filename, file_url = build_file_info(page)
                pages.append({
                    "page": page.page,
                    "title": page.title,
                    "filename": filename,
                    "file_url": file_url
                })

            data.append({
                "title": lesson.title,
                "pages": pages
            })

        return Response(data, status=status.HTTP_200_OK)
