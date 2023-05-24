from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class Trader(AbstractUser):
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

    def __str__(self):
        return self.name

    def get_balance(self):
        return self.balance


class Trade(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Trade by {self.trader.name} at {self.timestamp}"
