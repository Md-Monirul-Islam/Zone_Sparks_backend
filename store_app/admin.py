from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'get_total_sales', 'stock_status']

    def get_total_sales(self, obj):
        return obj.get_total_sales()
    get_total_sales.short_description = 'Total Sales'

    def stock_status(self, obj):
        return obj.stock_status()
    stock_status.short_description = 'Stock Status'

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderItems)