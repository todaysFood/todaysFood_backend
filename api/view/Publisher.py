from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from posts.models import Posts
from accounts.models import User
from posts.serializers import PostSerializer
from exceptions.policy import define


# 게시글 목록 : 비회원도 접근 가능하도록 설정
class Feed(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        queryset = Posts.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# 게시글 쓰기 : 회원 권한 필요
class FeedWrite(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            post = serializer.save()
            user_id = User.objects.get(id=request.user.id)
            post.author = user_id
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 게시글 조회 : 회원 권한 필요
class FeedDetail(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id, format=None):
        queryset = Posts.objects.get(id=id)
        serializer = PostSerializer(queryset, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)


# 게시글 수정/삭제 : 회원 권한 필요 + 글 작성자만 접근 가능
class FeedEdit(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        queryset = Posts.objects.get(id=id)

        if queryset.author.id == request.user.id:
            serializer = PostSerializer(queryset, many=False)
            return Response(serializer.data)
        else:
            raise define.NotEqualToAuthor()

    def put(self, request, id):

        post = Posts.objects.get(id=id)
        if post.author.id == request.user.id:
            post.content = request.data['content']
            post.title = request.data['title']
            post.rating = request.data['rating']
            post.place_id = request.data['place_id']
            post.modified_date = timezone.now()
            post.save()
            return Response("Post edited")
        else:
            raise define.NotEqualToAuthor()

    def delete(self, request, id):
        post = Posts.objects.get(id=id)
        if post.author_id == request.user.id:
            post.delete()
            return Response("Post deleted")
        else:
            raise define.NotEqualToAuthor()
