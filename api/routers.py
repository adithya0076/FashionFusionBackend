from django.urls import path
from rest_framework import routers
from api import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'items', viewsets.ItemViewSet)
# router.register(r'login', viewsets.UserLoginView.as_view(),basename="user-login")

