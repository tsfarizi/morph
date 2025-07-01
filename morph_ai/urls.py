from django.urls import path
from .views import ChatView, UserChatLogView

urlpatterns = [
    path("chat/", ChatView.as_view()),
    path("history/", UserChatLogView.as_view())
]
