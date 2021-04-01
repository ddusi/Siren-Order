from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.logistics.models import Product


class ProductAdmin(SimpleHistoryAdmin):
    list_display = ('pd_num', 'name', 'price', 'kind', 'status')
    history_list_display = ('pd_num', 'name', 'price', 'kind', 'status')
    search_fields = ['pd_num', 'name']

admin.site.register(Product, ProductAdmin)