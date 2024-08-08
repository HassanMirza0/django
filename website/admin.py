from django.contrib import admin
from website.models import *




class OrderItemTubLeinLine(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
  inlines=[OrderItemTubLeinLine]




# Register your models here.
admin.site.register(Contactus)
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)