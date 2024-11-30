from django.contrib import admin
from home.models import CrousalHome,VideoAPIResponse
from import_export.admin import ImportExportModelAdmin


class CrousalHomeAdmin(ImportExportModelAdmin):
    list_display=['title','rating','visiting_link']
admin.site.register(CrousalHome,CrousalHomeAdmin)
admin.site.register(VideoAPIResponse)