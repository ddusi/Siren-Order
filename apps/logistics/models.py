from django.db import models
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from simple_history.models import HistoricalRecords


class Product(TimeStampedModel, ActivatorModel):
    class Size(models.TextChoices):
        null = ''
        Tall = 'tall'
        Grande = 'grande'
        Venti = 'venti'

    class Kind(models.TextChoices):
        null = ''
        Coffee = 'coffee'
        Tea = 'tea'
        MD = 'MD_product'
        Frappuccino = 'frappuccino'
        Blended = 'blended'

    pd_num = models.CharField('상품번호', max_length=200)
    name = models.CharField('상품명', max_length=200)
    price = models.IntegerField('가격', default=0)
    kind = models.CharField('상품 종류', choices=Kind.choices, max_length=200, default='')
    size = models.CharField('사이즈', choices=Size.choices, max_length=8, blank=True, default='')
    history = HistoricalRecords(
        history_change_reason_field=models.TextField(null=True)
    )

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품 모음'
        ordering = ['pd_num']

    def __str__(self):
        return f'{self.pd_num} {self.name}'

    def save(self, *args, **kwargs):
        self.update_modified = kwargs.pop('update_modified', getattr(self, 'update_modified', True))
        if not self.activate_date:
            self.activate_date = now()
        super().save(**kwargs)