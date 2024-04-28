from django.urls import path
from app.views.user import UserCreateListAPIView, UserRetrieveUpdateDeleteAPIView
from app.views.post import PostCreateListAPIView, PostRetrieveUpdateDeleteAPIView
from app.views.like import LikeListCreateAPIView, LikeRetrieveUpdateDeleteAPIView
from app.views.comment import CommentListCreateAPIView, CommentRetrieveUpdateDeleteAPIView
from app.views.follow import FollowCreateListAPIView, FollowRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('users/', UserCreateListAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view()),
    path('posts/', PostCreateListAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view()),
    path('likes/', LikeListCreateAPIView.as_view()),
    path('likes/<int:pk>/', LikeRetrieveUpdateDeleteAPIView.as_view()),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteAPIView.as_view()),
    path('follow/', FollowCreateListAPIView.as_view()),
    path('follow/<int:pk>/', FollowRetrieveUpdateDeleteAPIView.as_view()),

]