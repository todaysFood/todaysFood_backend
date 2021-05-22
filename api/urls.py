from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from . import views
from .view.Posts import PostViewSet

from .view import (
    Member,
    Posts
)

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/place', views.api, name='api'),

    # Member
    url(r"register$", Member.Register.as_view()),  # Register Member

    # Login (JWT)
    url(r"login$", Member.ObtainToken.as_view()),  # Member Login

    # Post
    url(r"^", include(router.urls)),

    url(r"^token-auth/", obtain_jwt_token),
    url(r"^token-verify", verify_jwt_token),
    url(r"^token-refresh", refresh_jwt_token),
]
