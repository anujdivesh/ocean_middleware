from django.contrib import admin
from .models import DataType
# Register your models here.


class DataTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(DataType,DataTypeAdmin)
