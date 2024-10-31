from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','total_sales','stock_status']
admin.site.register(Product,ProductAdmin)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderItems)