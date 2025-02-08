from django.contrib import admin

from main.models import Products, ProductsCategory, Table, Basket


admin.site.register(ProductsCategory)
admin.site.register(Table)



@admin.register(Products)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'category')
    fields = ('name', 'price', 'category', 'description', 'image')
    search_fields = ['name']
    
    

class BasketAdmin(admin.TabularInline): 
    model = Basket  
    fields = ('product', 'quantity', 'creating_time_stamp')
    readonly_fields = ('creating_time_stamp',)
    extra =0 