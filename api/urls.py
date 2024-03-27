from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import UserLoginView, UserRegistrationView


from .routers import router

urlpatterns = [
   path('', include(router.urls)),
   path('login', UserLoginView.as_view(), name='user_login'),
   path('register', UserRegistrationView.as_view(), name='user_registration'),
]

urlpatterns = format_suffix_patterns(urlpatterns)