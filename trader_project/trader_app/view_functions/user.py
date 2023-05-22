from django.shortcuts import render
from ..models import Trade
from ..models import Trader
from ..views import simulate_profit_loss
import json
import plotly.graph_objects as go
from django.http import HttpResponseNotFound
from ..create_trader import create_trader_func
from django.http import HttpResponse


def home_to_create(request):
    traders = Trader.objects.all()
    if not traders:
        create_trader_func()
        return HttpResponse('<h1>Created traders</h1>')
    simulate_profit_loss()
    return HttpResponse('<h1>Done simulating</h1>')


def user_dashboard(request, trader_id):
    trades = Trade.objects.filter(trader=trader_id).order_by('timestamp')
    if not trades:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    # simulate_profit_loss()
    profit_loss_data = [(trade.timestamp.isoformat(), float(trade.profit_loss)) for trade in trades]

    timestamps = [data[0] for data in profit_loss_data]
    profit_loss_values = [data[1] for data in profit_loss_data]

    fig = go.Figure(data=go.Scatter(x=timestamps, y=profit_loss_values, mode='lines'))
    fig.update_layout(
        title='Profit/Loss',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Profit/Loss($)')
    )
    chart_data = fig.to_json()

    return render(request, 'index.html',
                  {'chart_data': chart_data,
                   'trader': trades[0].trader,
                   'balance': trades[0].trader.balance,
                   })


def admin_dashboard(request):
    traders = Trader.objects.all()
    return render(request, 'admin.html', {'traders': traders})


def trader_details(request, trader_id):
    trade = Trade.objects.filter(trader=trader_id).all()
    return render(request, 'trader_details.html',
                  {'trades': trade[::-1],
                   'trader': trade[0].trader,
                   })
