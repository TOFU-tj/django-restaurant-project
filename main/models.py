from typing import Iterable
from django.db import models
from user.models import User
from django.db.models import Sum
from django.conf import settings
import stripe



class ProductsCategory(models.Model):

    name = models.CharField("Категории", max_length=250)
    description =  models.TextField("Описание", null=True, blank=True)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Products(models.Model):
    
    name = models.CharField("Название", max_length=250)
    description =  models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    image = models.ImageField("Фото Блюда", upload_to="Product_IMG")
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE, verbose_name="Категории")
    

    class Meta:
        verbose_name = ("Products")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name
        

    
    
    
class Table(models.Model):

    table_number = models.IntegerField("Номер стола", unique=True)

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"

    def __str__(self):
        return f"Стол {self.table_number}"
    
    
    


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    creating_time_stamp = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey("Table", on_delete=models.CASCADE,  null=True, blank=True)  # Привязываем к столу

    
    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"

    def __str__(self):
        return f"Корзина {self.user.username} (Стол {self.table.table_number if self.table else 'Не указан'})"
    
    def sum(self): 
        return self.product.price * self.quantity
    




