from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
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

]
