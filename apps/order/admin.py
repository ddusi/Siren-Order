from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.order.models import Order


class OrderAdmin(SimpleHistoryAdmin):
    list_display = (
        "id",
        "orderer",
        "ordered_merchant",
        "assignment",
        "state",
        "amount",
    )
    history_list_display = (
        "id",
        "orderer",
        "ordered_merchant",
        "assignment",
        "state",
        "amount",
    )


admin.site.register(Order, OrderAdmin)
