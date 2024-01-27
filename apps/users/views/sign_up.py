from rest_framework.views import APIView
from rest_framework import permissions, response, status
from users.serializers.user import UserSerializer
from users.utils.user import get_sign_in_response


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(get_sign_in_response(user), status.HTTP_201_CREATED)
