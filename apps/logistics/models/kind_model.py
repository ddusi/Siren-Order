from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Kind(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "상품 종류"
        verbose_name_plural = "상품 종류 목록"

    def __str__(self):
        return self.name
