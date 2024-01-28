from rest_framework import serializers
from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["parent"] = (
            CategorySerializer(instance=instance.parent).data if instance.parent else {}
        )
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        if hasattr(request, "app") and request.app:
            validated_data.pop("app")
            category = Category.objects.create(
                **validated_data,
                app=request.app,
            )
            return category

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "description",
            "attachment",
            "parent",
        )
