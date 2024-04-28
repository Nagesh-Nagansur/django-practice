from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Follow, User
from app.serializers.follow_serializer import FollowSerializer


class FollowCreateListAPIView(APIView):

    def post(self, request):
        follower = request.data['follower']
        followed = request.data['followed']
        if followed == follower:
            return Response({"message":"You can't follow yourself"},status=status.HTTP_400_BAD_REQUEST)
        follower_user = get_object_or_404(User, pk=follower)
        followed_user = get_object_or_404(User, pk=followed)
        Follow.objects.create(follower=follower_user, followed=followed_user)
        return Response({"message":"Successfully Followed"},status=status.HTTP_201_CREATED)


class FollowRetrieveUpdateDeleteAPIView(APIView):

    def get(self, request, pk):
        follow = Follow.objects.filter(followed=pk).all()
        serializer = FollowSerializer(follow,many=True)
        return Response(serializer.data)


    def delete(self, request, pk):
        current_user_id = 2
        follow = Follow.objects.filter(followed=pk, follower=current_user_id).first()
        follow.delete()
        return Response({"message":"Unfollowed Successfully"},status=status.HTTP_204_NO_CONTENT)
