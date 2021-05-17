from rest_framework import viewsets
from posts.serializers import PostSerializer
from posts.models import Posts

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer