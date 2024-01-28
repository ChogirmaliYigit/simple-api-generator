from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["parent"] = (
            ProductSerializer(instance=instance.parent).data if instance.parent else {}
        )
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        if hasattr(request, "app") and request.app:
            validated_data.pop("app")
            product = Product.objects.create(
                **validated_data,
                app=request.app,
            )
            return product

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "attachment",
            "category",
            "parent",
            "price",
            "discount_percentage",
            "rating",
            "stock",
        )
