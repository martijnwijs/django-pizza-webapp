from django.contrib import admin

# Register your models here.
from .models import *

# add the classes from models.py that should be able to be manipulated via the admin application
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Toppings)
admin.site.register(Size)
#admin.site.register(Shop_cart)
admin.site.register(Order)
admin.site.register(Type)
admin.site.register(Name)
