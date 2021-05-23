from django.urls import path
from django.conf.urls import url
from . import views

from .view import (
    Member,
    Publisher
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)


urlpatterns = [
    path('', views.index, name='index'),
    path('v1/place', views.api, name='api'),

    # Member
    url(r"^register$", Member.Register.as_view()),  # Register Member

    # Login (JWT)
    url(r"^login$", Member.ObtainToken.as_view()),  # Member Login

    # Login (JWT)
    url(r"^token-get", TokenObtainPairView.as_view()),  # Member Login


    # Post
    # url(r"^", include(router.urls)),
    url(r"^post$", Publisher.Feed.as_view()),  # post viewset 추가

    # 삭제 2021.05.23 이후 삭제
    # url(r"^token-auth/", obtain_jwt_token),
    # url(r"^token-verify", verify_jwt_token),
    # url(r"^token-refresh", refresh_jwt_token),
]
