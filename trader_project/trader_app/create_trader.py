from .models import Trader, Trade
from django.contrib.auth.hashers import make_password

traders = {
    'trader1': {
        'name': 'trader1',
        'password': 'password',
        'username': 'trader1',
    },
    'trader2': {
        'name': 'trader2',
        'password': 'password',
        'username': 'trader2',
    },
    'trader3': {
        'name': 'trader3',
        'password': 'password',
        'username': 'trader3',
    },
    'trader4': {
        'name': 'trader4',
        'password': 'password',
        'username': 'trader4',
    },
    'trader5': {
        'name': 'trader5',
        'password': 'password',
        'username': 'trader5',
    },
    'trader6': {
        'name': 'trader6',
        'password': 'password',
        'username': 'trader6',
    },
    'trader7': {
        'name': 'trader7',
        'password': 'password',
        'username': 'trader7',
    },
    'trader8': {
        'name': 'trader8',
        'password': 'password',
        'username': 'trader8',
    },
    'trader9': {
        'name': 'trader9',
        'password': 'password',
        'username': 'trader9',
    },
    'trader10': {
        'name': 'trader10',
        'password': 'password',
        'username': 'trader10',
    },
    'admin': {
        'name': 'admin',
        'password': 'admin',
        'username': 'admin',
        'is_superuser': True,
        'email': 'admin@admin.com'
    },
}


def create_trader_func():
    for trader in traders.values():
        password = make_password(trader['password'])
        if 'is_superuser' in trader:
            Trader.objects.create_superuser(
                name=trader['name'],
                password=trader['password'],
                username=trader['username'],
                email=trader['email']
            )
        else:
            Trader.objects.create(name=trader['name'], password=password, username=trader['username'])
        # print(f"Created {trader['name']}")
