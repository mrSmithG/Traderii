from django.contrib import admin
from django.utils.html import format_html

from . import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductImage)
