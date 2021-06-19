from datetime import (
    datetime,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtaionSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add Custom Claims
        token['name'] = user.name
        token['email'] = user.email
        token['iat'] = datetime.now()

        return token
