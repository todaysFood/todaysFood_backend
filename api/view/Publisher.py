from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from posts.models import Posts
from posts.serializers import PostSerializer
# from posts.serializers import PostSerializer


class Feed(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        queryset = Posts.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            post = serializer.save()
            post.author = request.user.nick_name
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("error")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedEdit(APIView):
    def get(self, request, id, format=None):
        queryset = Posts.objects.get(id=id)
        queryset.author = request.user.email

        if queryset.author == request.user.email:

            serializer = PostSerializer(queryset, many=False)
            return Response(serializer.data)
        # return Response("serializer.data")


