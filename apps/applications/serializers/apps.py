from applications.models import Application
from rest_framework import serializers


class AppsListSerializer(serializers.ModelSerializer):
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data["owner"] = UserSerializer(instance=instance.owner)
    #     return data

    def create(self, validated_data):
        request = self.context.get("request")
        app = Application.objects.create(**validated_data, owner=request.user)
        return app

    class Meta:
        model = Application
        fields = (
            "title",
            "owner",
            "visibility",
            "uuid",
            "description",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "owner": {"read_only": True},
            "visibility": {"required": False},
            "uuid": {"read_only": True},
        }
