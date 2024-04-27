from django.urls import path
from app.views.user import UserCreateListAPIView, UserRetrieveUpdateDeleteAPIView
from app.views.post import PostCreateListAPIView, PostRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('users/', UserCreateListAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view()),
    path('posts/', PostCreateListAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view()),

]