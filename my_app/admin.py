from django.contrib import admin
from my_app.models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "slug", "updated_at", "created_at")

admin.site.register(Product, ProductAdmin)