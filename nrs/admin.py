from django.contrib import admin
from .models import DmsProjekte, DmsStatus, TblDmsProjectAdditionalData


@admin.register(DmsProjekte)
class RoleAdmin(admin.ModelAdmin):
    fields = ['prjlist']
    list_display = ('prjlist', 'prjlist','prjlist')
    search_fields = fields
    list_filter = fields