from rest_framework import serializers
from app.models import Like

class LikeSerializer(serializers.Serializer):

    class Meta:
        model = Like
        fields = '__all__'