from rest_framework import serializers
from app.models import PostLike

class PostLikeSerializer(serializers.Serializer):

    class Meta:
        model = PostLike
        fields = '__all__'