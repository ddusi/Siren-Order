from django.db import models
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from simple_history.models import HistoricalRecords


class Merchant(TimeStampedModel, ActivatorModel):
    merchant_number = models.IntegerField("매장번호", unique=True, db_index=True)
    name = models.CharField("매장이름", max_length=50)
    type = models.CharField("매장유형", max_length=30, default="store")
    merchant_contract = models.CharField("매장연락처", max_length=50, blank=True)

    # TODO address 관련 -> 추후 정규화
    addr = models.CharField("매장주소", max_length=200, blank=True)
    addr_detail = models.CharField("상세주소", max_length=100, blank=True)
    addr_city = models.CharField("시,도", max_length=30)
    addr_province = models.CharField("구,동", max_length=30)

    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))

    class Meta:
        verbose_name = "매장"
        verbose_name_plural = "매장 목록"
        ordering = ["merchant_number"]

    def save(self, *args, **kwargs):
        self.update_modified = kwargs.pop(
            "update_modified", getattr(self, "update_modified", True)
        )
        if not self.activate_date:
            self.activate_date = now()
        super().save(**kwargs)
