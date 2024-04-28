from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from app.models import Like
from app.serializers.likes_serializer import LikeSerializer
from rest_framework.views import APIView



class LikeListCreateAPIView(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Liked it"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

class LikeRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        like = get_object_or_404(Like, pk=pk)
        serializer = LikeSerializer(like)
        return Response(serializer.data)

    def put(self, request, pk):
        like = get_object_or_404(Like, pk=pk)
        serializer = LikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        like = get_object_or_404(Like, pk=pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)