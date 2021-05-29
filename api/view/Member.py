from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from ..serializer.JwtSerializer import CustomTokenObtaionSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from exceptions.policy import define

User = get_user_model()


class Register(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        """ 회원 생성 API """
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        name = request.data.get("name", None)
        nick_name = request.data.get("nick_name", None)

        if not (email and password):
            raise define.EmptyValueException()

        if not (name and nick_name):
            raise define.EmptyValueException()

        try:
            User.objects.create_user(
                email=email,
                password=password,
                name=name,
                nick_name=nick_name
            )
        except Exception as err:
            raise define.AlreadyExistUserIdentified()

        return Response({
            "status": 200,
        })


class JwtObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtaionSerializer
