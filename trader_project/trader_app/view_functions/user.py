from django.shortcuts import render, redirect
from ..models import Trade
from ..models import Trader
from ..views import simulate_profit_loss
from django.contrib import messages
import json
import plotly.graph_objects as go
from django.http import HttpResponseNotFound
from ..create_trader import create_trader_func
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home_to_create(request):
    traders = Trader.objects.all()
    if not traders:
        create_trader_func()
        return HttpResponse('<h1>Created traders</h1>')
    simulate_profit_loss()
    return HttpResponse('<h1>Done simulating</h1>')


@login_required(login_url='login')
def user_dashboard(request, trader_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged-in')
        return redirect('login')
    if request.user.id != trader_id and not request.user.is_superuser:
        return HttpResponseNotFound('<h1>Page not found</h1>')
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


@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged-in')
        return redirect('login')
    if not request.user.is_superuser:
        return HttpResponseNotFound('<h1>Admin access only</h1>')
    traders = Trader.objects.filter(is_superuser=False).all
    return render(request, 'admin.html', {'traders': traders})


@login_required(login_url='login')
def trader_details(request, trader_id):
    trader_profit_lost = {}
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged-in')
        return redirect('login')
    if not request.user.is_superuser:
        return HttpResponseNotFound('<h1>Admin access only</h1>')
    trade = Trade.objects.filter(trader=trader_id).all()
    if not trade:
        return HttpResponseNotFound('<h1>No details yet</h1>')
    for t in trade:
        prof = float(t.profit_loss)
        trader_profit_lost[t.timestamp.isoformat()] = prof

    # Reverse the dictionary
    reversed_profit_lost = {value: key for key, value in trader_profit_lost.items()}

    return render(request, 'trader_details.html',
                  {'trades': trade[::-1],
                   'trader': trade[0].trader,
                   'prof_lost': reversed_profit_lost,
                   })
