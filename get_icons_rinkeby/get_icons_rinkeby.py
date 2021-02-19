import requests

# This script fetches mainnet token icons for rinkeby tokens in case their token symbol matches exactly.

# get token info we have on rinkeby.

req = requests.get('https://safe-transaction.rinkeby.gnosis.io/api/v1/tokens/', params={'limit': 400})  # I know that we have ~300 currently.

data = req.json()

for token_info in data['results']:
    # check if token already has an image
    if token_info['symbol'] == 'CRC':  # Fix for xdai to disregard the many circles images
        continue
    if requests.get(token_info['logoUri']).status_code == 200:
        # if yes, skip
        print('Rinkeby token logo present for {} at {}'.format(token_info['symbol'], token_info['address']))
        continue

    # check if there is a token for this on mainnet
    mainnet_token_req = requests.get('https://safe-transaction.gnosis.io/api/v1/tokens/', params={'symbol': token_info['symbol']})
    mainnet_token_data = mainnet_token_req.json()
    if mainnet_token_data['count'] == 0:
        # if no token, skip
        print('No mainnet token found for symbol {}'.format(token_info['symbol']))
        continue
    
    # check if mainnet token has an image
    mainnet_logo_req = requests.get(mainnet_token_data['results'][0]['logoUri'])
    if mainnet_logo_req.status_code != 200:
        # if no logo, skip
        print('Mainnet token logo not found for {} at {}'.format(token_info['symbol'], token_info['address']))
        continue
    
    # Write logo to file with filename of rinkeby token address
    filename = '{}.png'.format(token_info['address'])
    open(filename, 'wb').write(mainnet_logo_req.content)
    print('Rinkeby token logo written to {} for {} at {}'.format(filename, token_info['symbol'], token_info['address']))