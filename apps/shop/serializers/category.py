from rest_framework import serializers
from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["parent"] = CategorySerializer(instance=instance.parent).data if instance.parent else {}
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        if hasattr(request, "app") and request.app:
            title = validated_data.get("title")
            description = validated_data.get("description")
            attachment = validated_data.get("attachment")
            parent_id = validated_data.get("parent_id")

            category = Category.objects.create(
                title=title, description=description, attachment=attachment, parent_id=parent_id, app=request.app
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
