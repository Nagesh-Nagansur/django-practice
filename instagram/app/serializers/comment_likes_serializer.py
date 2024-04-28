from rest_framework import serializers
from app.models import CommentLike

class CommentLikeSerializer(serializers.Serializer):

    class Meta:
        model = CommentLike
        fields = '__all__'