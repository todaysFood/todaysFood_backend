from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Posts


class PostSerializer(ModelSerializer):
    # auth_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posts
        fields = ('id', 'title', 'author', 'pub_date', 'content', 'rating', 'place_id')
