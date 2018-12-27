from django.contrib import admin
from .models import user, container, container_product_detail, product, product_category, provider_product, container_product_log, order, order_detail

# Register your models here.
class userAdmin(admin.ModelAdmin):
	list_display = ['username', 'password', 'name', 'address', 'email', 'mobile', 'code', 'image', 'status', 'dele']
	search_fields = ['username']

class productAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'price', 'description', 'image', 'product_category_id', 'dele']
	search_fields = ['name']

class product_categoryAdmin(admin.ModelAdmin):
	list_display = ['name','description', 'dele']
	search_fields = ['name']

class container_product_detailAdmin(admin.ModelAdmin):
	list_display = ['product_id', 'container_id', 'provider_id', 'amount', 'manufacturing_date', 'expiry_date']
	search_fields = ['product_id']

class provider_productAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'product_id', 'dele']

class containerAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'address', 'mobile', 'dele']
	search_fields = ['code']

class container_product_logAdmin(admin.ModelAdmin):
	list_display = ['container_from', 'container_to', 'product_id', 'amount', 'manufacturing_date', 'expiry_date']

class orderAdmin(admin.ModelAdmin):
	list_display = ['code', 'user_id', 'price_total', 'order_date', 'status', 'export_date']

class order_detailAdmin(admin.ModelAdmin):
	list_display = ['order_id', 'product_id', 'amount', 'price', 'manufacturing_date', 'expiry_date']
 
admin.site.register(user, userAdmin)
admin.site.register(product, productAdmin)
admin.site.register(product_category, product_categoryAdmin)
admin.site.register(container, containerAdmin)
admin.site.register(provider_product, provider_productAdmin)
admin.site.register(container_product_detail, container_product_detailAdmin)
admin.site.register(container_product_log, container_product_logAdmin)
admin.site.register(order, orderAdmin)
admin.site.register(order_detail, order_detailAdmin)