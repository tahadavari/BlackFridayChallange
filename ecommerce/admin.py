from django.contrib import admin

from ecommerce.models import Product, ProductCount, Invoice, Basket

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCount)
admin.site.register(Invoice)
admin.site.register(Basket)
