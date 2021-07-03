from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from posts.models import Posts
from posts.serializers import PostSerializer


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # GET, HEAD, OPTION 요청에 대해서는 Permission 부여
        return obj.author == request.user


class FeedViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated and IsOwnerOrReadOnly]
    authentication_classes = (JWTAuthentication,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


post_list = FeedViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = FeedViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# # 게시글 목록 : 비회원도 접근 가능하도록 설정
# @permission_classes([AllowAny])
# class Feed(APIView):
#     # permission_classes = (permissions.AllowAny,)
#     # @permission_classes([AllowAny])
#     def get(self, request, format=None):
#         queryset = Posts.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# # 게시글 쓰기 : 회원 권한 필요
# @permission_classes([AllowAny])
# class FeedWrite(APIView):
#     authentication_classes = (JWTAuthentication,)
#
#     # permission_classes = (permissions.IsAuthenticated,)
#     # @permission_classes(permissions.IsAuthenticated)
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#
#         if serializer.is_valid():
#             post = serializer.save()
#             user_id = User.objects.get(id=request.user.id)
#             post.author = user_id
#             post.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # 게시글 조회 : 회원 권한 필요
# class FeedDetail(APIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request, id, format=None):
#         queryset = Posts.objects.get(id=id)
#         serializer = PostSerializer(queryset, many=False)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# # 게시글 수정/삭제 : 회원 권한 필요 + 글 작성자만 접근 가능
# class FeedEdit(APIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request, id):
#         queryset = Posts.objects.get(id=id)
#
#         if queryset.author.id == request.user.id:
#             serializer = PostSerializer(queryset, many=False)
#             return Response(serializer.data)
#         else:
#             raise define.NotEqualToAuthor()
#
#     def put(self, request, id):
#
#         post = Posts.objects.get(id=id)
#         if post.author.id == request.user.id:
#             post.content = request.data['content']
#             post.title = request.data['title']
#             post.rating = request.data['rating']
#             post.place_id = request.data['place_id']
#             post.modified_date = timezone.now()
#             post.save()
#             return Response("Post edited")
#         else:
#             raise define.NotEqualToAuthor()
#
#     def delete(self, request, id):
#         post = Posts.objects.get(id=id)
#         if post.author_id == request.user.id:
#             post.delete()
#             return Response("Post deleted")
#         else:
#             raise define.NotEqualToAuthor()
