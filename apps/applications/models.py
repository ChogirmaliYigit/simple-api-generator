import uuid

from core.models import BaseModel
from django.db import models


class Application(BaseModel):
    PRIVATE = "private"
    PUBLIC = "public"

    VISIBILITIES = (
        (PRIVATE, "Private"),
        (PUBLIC, "Public"),
    )

    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    visibility = models.CharField(choices=VISIBILITIES, db_default=PUBLIC)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="applications"
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "applications"
