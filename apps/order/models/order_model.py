from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords


class Order(TimeStampedModel):
    class State(models.TextChoices):
        Pending = ('pending', '대기')
        Payed = ('payed', '결제완료')
        Manufacturing = ('manufacturing', '제조중')
        Complete = ('complete', '완료')
        Cancel = ('cancel', '취소')

    state = models.CharField('주문상태', choices=State.choices, max_length=32, default='pending')
    amount = models.IntegerField('주문금액', default=0)

    ordered_merchant = models.ForeignKey('client.merchant', verbose_name='주문받은 매장', related_name='ordered_merchant_set',
                                         on_delete=models.DO_NOTHING)
    orderer = models.ForeignKey(User, verbose_name='주문자', related_name='orderer_set', on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(User, verbose_name='담당직원', related_name='assignment_set',
                                   on_delete=models.DO_NOTHING)
    product = models.ManyToManyField('logistics.product', verbose_name='주문상품')

    history = HistoricalRecords(
        history_change_reason_field=models.TextField(null=True)
    )

    class Meta:
        verbose_name = '주문'
        verbose_name_plural = '주문 목록'
