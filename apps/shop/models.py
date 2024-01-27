from core.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    attachment = models.TextField(null=True, blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="child_categories",
        null=True,
        blank=True,
    )
    app = models.ForeignKey(
        "applications.Application", on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "shops"
        verbose_name_plural = "Categories"


class Product(BaseModel):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    attachment = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="child_products",
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=30, decimal_places=2)
    discount_percentage = models.FloatField(null=True, blank=True)
    rating = models.FloatField(
        null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    stock = models.PositiveBigIntegerField(null=True, blank=True)
    app = models.ForeignKey(
        "applications.Application", on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"
