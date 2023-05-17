from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Document


# Register your models here.



@admin.register(Document)
class ProductAdminModel(ModelAdmin):
    pass