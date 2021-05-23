from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from rest_framework import exceptions

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import (
    BaseJSONWebTokenAuthentication,
    JSONWebTokenAuthentication
)
from .utils.jwt_payload import jwt_get_user_email_from_payload_handler

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_user_email_from_payload_handler = jwt_get_user_email_from_payload_handler

User = get_user_model()


class CustomBaseJSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    """
    Token based authentication using the JSON Web Token standard.
    """

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        email = jwt_get_user_email_from_payload_handler(payload)
        if not email:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get_by_natural_key(email)
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return user


class CustomJSONWebTokenAuthentication(
    CustomBaseJSONWebTokenAuthentication,
    JSONWebTokenAuthentication
):
    pass
