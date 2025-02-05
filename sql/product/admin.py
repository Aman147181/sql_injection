from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'stock', 'category', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'price', 'description', 'stock', 'category', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):  # Use Django's default ModelAdmin
    resource_class = ProductResource

    list_display = ('name', 'price', 'stock', 'category', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')
