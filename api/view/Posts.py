from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from posts.serializers import PostSerializer
from posts.models import Posts


# @permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
class PostViewSet(ModelViewSet):
    permission_classes = []
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    def post(self, request, format=None):
        new_content = request.data['content']
        new_title = request.data['title']
        return Response("Post Added")

