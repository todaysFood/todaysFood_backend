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

    # Post 목록
    url(r"^post$", Publisher.Feed.as_view()),  # Post List

    # Post 작성
    url(r"^post/write$", Publisher.FeedWrite.as_view()),

    # Post 상세보기
    url(r"^post/(?P<id>\d+)$", Publisher.FeedDetail.as_view(), name='postdetail'),  # Post Detail

    # Post 수정/삭제하기
    url(r"^post/(?P<id>\d+)/edit$", Publisher.FeedEdit.as_view(), name='postedit'),  # Post Edit/Delete

]
