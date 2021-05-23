from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


# from posts.serializers import PostSerializer


class Feed(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        print("API Called")
        # new_content = request.data['content']
        # new_title = request.data['title']
        # print(new_content, new_title)
        return Response(200)
