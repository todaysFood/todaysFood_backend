from rest_framework.exceptions import APIException
from rest_framework import status

from django.utils.translation import gettext_lazy as _


class EmptyValueException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Required Value is Empty.")


class InValidLoginCredential(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Request Credential is invalid.")


class AlreadyExistUserIdentified(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Already User ID Exist")
