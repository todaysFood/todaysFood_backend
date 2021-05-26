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
    url(r"^login$", Member.JwtObtainView.as_view()),  # Member Login

    # Post
    url(r"^post/$", Publisher.Feed.as_view()),  # post viewset 추가

    # Postedit
    url(r"^post/(?P<id>\d+)/edit/$", Publisher.FeedEdit.as_view(), name='postedit'),

]
