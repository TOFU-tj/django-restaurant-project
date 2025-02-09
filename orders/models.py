from django.db import models
from user.models import User
from main.models import Table

class Order(models.Model):
    READY = 0 
    PAID = 1 
    WAITING = 2
    STATUSES = (
        (WAITING, 'в ожидании'),
        (PAID, 'оплачено'),
        (READY, 'готово'),
    )
    
    # first_name = models.ForeignKey(User,on_delete=models.CASCADE)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    basket_history = models.JSONField( default=dict)
    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.SmallIntegerField(default=WAITING, choices=STATUSES)
    
    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return f"заказ номер {self.id}, {self.table_number}"
