from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from app.models import CommentLike
from app.serializers.comment_likes_serializer import CommentLikeSerializer
from rest_framework.views import APIView



class CommentLikeListCreateAPIView(APIView):
    def post(self, request):
        serializer = CommentLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Liked it"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    def get(self, request):
        likes = CommentLike.objects.all()
        serializer = CommentLikeSerializer(likes, many=True)
        return Response(serializer.data)

class CommentLikeRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        like = get_object_or_404(CommentLike, pk=pk)
        serializer = CommentLikeSerializer(like)
        return Response(serializer.data)

    def put(self, request, pk):
        like = get_object_or_404(CommentLike, pk=pk)
        serializer = CommentLikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        like = get_object_or_404(CommentLike, pk=pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)