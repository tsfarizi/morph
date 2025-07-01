from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, UserUpdateView, UserDeleteView,UserLessonProgressView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("me/", UserDetailView.as_view()),
    path("me/update/", UserUpdateView.as_view()),
    path("me/delete/", UserDeleteView.as_view()),
    path("me/progress/", UserLessonProgressView.as_view())
]
