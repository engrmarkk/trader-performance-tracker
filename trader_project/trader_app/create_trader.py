from .models import Trader, Trade

traders = {
    'trader1': {
        'name': 'trader1',
    },
    'trader2': {
        'name': 'trader2',
    },
    'trader3': {
        'name': 'trader3',
    },
    'trader4': {
        'name': 'trader4',
    },
    'trader5': {
        'name': 'trader5',
    },
    'trader6': {
        'name': 'trader6',
    },
    'trader7': {
        'name': 'trader7',
    },
    'trader8': {
        'name': 'trader8',
    },
    'trader9': {
        'name': 'trader9',
    },
    'trader10': {
        'name': 'trader10',
    },
}


def create_trader_func():
    for trader in traders.values():
        Trader.objects.create(name=trader['name'])
        print(f"Created {trader['name']}")
