from django.db import models
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from simple_history.models import HistoricalRecords


class Partner(TimeStampedModel, ActivatorModel):
    employee_number = models.IntegerField("사원번호", unique=True, db_index=True)
    nick_name = models.CharField("호칭", max_length=50, blank=True)
    rank = models.CharField("직급", max_length=30, blank=True)
    is_store_manager = models.BooleanField("매장관리자", default=False)
    employment_date = models.DateTimeField("입사날짜", null=True)

    # TODO 추후 정규화 할 필요가 있음.
    department = models.CharField("부서", max_length=30, blank=True)

    merchant = models.ForeignKey(
        "client.merchant",
        verbose_name="매장",
        related_name="merchant_set",
        on_delete=models.CASCADE,
    )

    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))

    class Meta:
        verbose_name = "파트너"
        verbose_name_plural = "파트너 목록"
        ordering = ["employee_number"]

    def save(self, *args, **kwargs):
        self.update_modified = kwargs.pop(
            "update_modified", getattr(self, "update_modified", True)
        )
        if not self.activate_date:
            self.activate_date = now()

        # when create model
        if self.pk is None:
            self.employee_number = int(Partner.objects.last().employee_number) + 1

        super().save(**kwargs)
