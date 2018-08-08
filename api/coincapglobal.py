import json
import requests
from datetime import datetime as dt

global_url = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(global_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))


active_currencies = results['data']['active_cryptocurrencies']
active_marcets = results['data']['active_markets']
bit_perc = results['data']['bitcoin_percentage_of_market_cap']
last_update = results['data']['last_updated']
market_cap = int(results['data']['quotes']['USD']['total_market_cap'])
twentyfour_volume = int(results['data']['quotes']['USD']['total_volume_24h'])

active_currencies_str = '{:,}'.format(active_currencies)
active_marcets_str = '{:,}'.format(active_marcets)
market_cap_str = '{:,}'.format(market_cap)
twentyfour_volume = '{:,}'.format(twentyfour_volume)
last_update_str = dt.fromtimestamp(last_update).strftime('%d %B, %Y at %T')


print()
print('There are currently: ' + active_currencies_str + ' active cryptos & ' + active_marcets_str + " active markets.")
print('The Global cap of all cryptos is: ' + market_cap_str + ' and the 24h volume is ' + twentyfour_volume + '.')
print('The dominance of BTC is: ' + str(bit_perc) + '%.')
print()
print('This information was last updated on: ' + last_update_str + '.')
print()
