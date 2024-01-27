from django.db import models
from core.queryset.base import BaseManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = BaseManager()

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    class Meta:
        abstract = True
        ordering = ("id",)
