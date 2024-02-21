from rest_framework import permissions, response, status
from rest_framework.views import APIView
from users.serializers.user import UserSerializer
from users.utils.user import get_sign_in_response


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(get_sign_in_response(user), status.HTTP_201_CREATED)
