from django.contrib import admin

from main.models import Products, ProductsCategory, Table, Basket

admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(Table)
admin.site.register(Basket)