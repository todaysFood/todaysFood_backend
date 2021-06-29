from django.urls import path
from django.conf.urls import url

from .view import (
    Member,
    Publisher,
    KakaoLocal,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('', KakaoLocal.index),

    path('v1/place/', KakaoLocal.local_api),
    path('v1/food/', KakaoLocal.food_api),

    # Member
    path('register/', Member.Register.as_view()),  # Register Member
    # Login (JWT)
    path('login/', Member.JwtObtainView.as_view()),  # Member Login
    # Post
    path('feed/', Publisher.post_list),  # Post List

    path('feed/<int:pk>/', Publisher.post_detail),  # Post Detail

]
