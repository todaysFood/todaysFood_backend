from ..models import Posts
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    # auth_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posts
        fields = "__all__"
