from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.logistics.models import Product, Kind


class ProductAdmin(SimpleHistoryAdmin):
    list_display = ("pd_num", "name", "price", "kind", "status")
    history_list_display = ("pd_num", "name", "price", "kind", "status")
    search_fields = ["pd_num", "name"]


class KindAdmin(admin.ModelAdmin):
    fields = ["name", "parent"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Kind, KindAdmin)
