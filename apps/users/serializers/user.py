from rest_framework import exceptions, serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if (
            attrs.get("username")
            and User.objects.filter(username=attrs.get("username")).exists()
        ):
            raise exceptions.ValidationError({"username": "Username already exists"})
        return attrs

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "password": {"write_only": True},
        }
