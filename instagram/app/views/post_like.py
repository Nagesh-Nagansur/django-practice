from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from app.models import PostLike
from app.serializers.post_likes_serializer import PostLikeSerializer
from rest_framework.views import APIView



class PostLikeListCreateAPIView(APIView):
    def post(self, request):
        serializer = PostLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Liked it"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    def get(self, request):
        likes = PostLike.objects.all()
        serializer = PostLikeSerializer(likes, many=True)
        return Response(serializer.data)

class PostLikeRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        like = get_object_or_404(PostLike, pk=pk)
        serializer = PostLikeSerializer(like)
        return Response(serializer.data)

    def put(self, request, pk):
        like = get_object_or_404(PostLike, pk=pk)
        serializer = PostLikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        like = get_object_or_404(PostLike, pk=pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)