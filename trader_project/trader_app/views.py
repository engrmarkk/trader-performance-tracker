from django.shortcuts import render
from .models import Trader, Trade
import random
from decimal import Decimal


def simulate_profit_loss():
    traders = Trader.objects.filter(username__startswith='trader').all()
    for trader in traders:
        profit_loss = Decimal(random.uniform(-10, 10))
        trader.balance = Decimal(trader.balance) + profit_loss
        trader.save()

        trade = Trade.objects.create(trader=trader, profit_loss=profit_loss)
        trade.save()

        # print(f"Profit/Loss: {str(profit_loss)}")
