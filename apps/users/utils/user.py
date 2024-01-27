from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers.user import UserSerializer


def get_sign_in_response(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        **UserSerializer(instance=user).data,
    }
