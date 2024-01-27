from django.urls import path
from users.views.sign_up import SignUpView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("sign-up", SignUpView.as_view(), name="sign-up"),
    path('sign-in', TokenObtainPairView.as_view(), name='sign-in'),
    path('token-refresh', TokenRefreshView.as_view(), name='token-refresh'),
]
