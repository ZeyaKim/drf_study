from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "updated_at"]
        # 모든 필드를 포함하고 싶다면 '__all__'을 사용할 수 있습니다.
        # fields = '__all__'
