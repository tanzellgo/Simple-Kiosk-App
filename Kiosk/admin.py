from django.contrib import admin
from .models import Food, Customer, Order, OrderLine


admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderLine)
# Register your models here.
