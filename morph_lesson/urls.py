from django.urls import path
from .views import LessonView

urlpatterns = [
    path("lessons/", LessonView.as_view()),  
    path("lesson/<str:title>/page/<int:page_number>/", LessonView.as_view()), 
]
