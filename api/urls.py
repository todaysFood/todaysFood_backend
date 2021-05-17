from django.urls import path
from django.conf.urls import url
from . import views

from .view import (
    Member,
    Posts
)

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/place', views.api, name='api'),

    # Member
    url(r"register$", Member.Register.as_view()),  # Register Member

    # Login (JWT)
    url(r"login$", Member.ObtainToken.as_view()),  # Member Login



]
