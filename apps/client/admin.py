from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.client.models import Merchant, Partner


class MerchantAdmin(SimpleHistoryAdmin):
    list_display = ('merchant_number', 'name', 'type', 'addr', 'merchant_contract')
    history_list_display = ('merchant_number', 'name', 'type', 'addr', 'merchant_contract')


class PartnerAdmin(SimpleHistoryAdmin):
    list_display = ('employee_number', 'nick_name', 'rank', 'is_store_manager', 'employment_date')
    history_list_display = ('employee_number', 'nick_name', 'rank', 'is_store_manager', 'employment_date')


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Partner, PartnerAdmin)
