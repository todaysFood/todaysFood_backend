from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Posts


class PostSerializer(ModelSerializer):
    # auth_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posts
        fields = "__all__"