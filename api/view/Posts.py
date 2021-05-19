from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.serializers import PostSerializer
from posts.models import Posts


class PostViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
