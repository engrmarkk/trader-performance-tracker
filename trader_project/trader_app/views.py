from django.shortcuts import render
from .models import Trader, Trade
# Create your views here.
import random
from decimal import Decimal


def simulate_profit_loss():
    traders = Trader.objects.all()
    for trader in traders:
        profit_loss = Decimal(random.uniform(-10, 10))  # Convert float to Decimal
        trader.balance += profit_loss
        trader.save()

        trade = Trade.objects.create(trader=trader, profit_loss=profit_loss)
        trade.save()
