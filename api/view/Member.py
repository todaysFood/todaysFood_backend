from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from exceptions.policy import define

User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class Register(APIView):

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


class ObtainToken(APIView):
    def post(self, request):
        """  JWT Token Obtain"""
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if not (email and password):
            raise define.EmptyValueException()

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.save()
            payload = jwt_payload_handler(user)
        except Exception as err:
            raise define.InValidLoginCredential()

        return Response({
            "access-token": "JWT " + jwt_encode_handler(payload)
        })
