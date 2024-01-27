from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["parent"] = ProductSerializer(instance=instance.parent).data if instance.parent else {}
        return data

    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "attachment",
            "category",
            "parent",
            "price",
            "discount_percentage",
            "rating",
            "stock"
        )
