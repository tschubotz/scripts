import requests
from pathlib import Path

# This script goes through atoken list and checks if we have this token in the backend and whether it has an icon or not. If not, then the icon is downloaded.

tx_service_token_url = 'https://safe-transaction.gnosis.io/api/v1/tokens/'

chain_id = 1

token_list_urls = [
    'https://wispy-bird-88a7.uniswap.workers.dev/?url=http://tokens.1inch.eth.link',
    'https://tokens.coingecko.com/uniswap/all.json',
    'https://uniswap.mycryptoapi.com/',
    'https://wispy-bird-88a7.uniswap.workers.dev/?url=http://tokenlist.zerion.eth.link',
    'https://zapper.fi/api/token-list',
    'https://wispy-bird-88a7.uniswap.workers.dev/?url=http://tokenlist.aave.eth.link',
    'https://raw.githubusercontent.com/compound-finance/token-list/master/compound.tokenlist.json',
    'https://raw.githubusercontent.com/SetProtocol/uniswap-tokenlist/main/set.tokenlist.json',
    'https://gateway.ipfs.io/ipns/tokens.uniswap.org'
    ]

# Get tokens that the backend knows about

req = requests.get(tx_service_token_url, params={'limit': 3200})  # I know that we have ~31xx currently.

known_tokens = dict()

data = req.json()

for token_info in data['results']:
    known_tokens[token_info['address']] = token_info

# Go through all tokens 

for token_list_url in token_list_urls:
    # Fetch the token info
    req = requests.get(token_list_url)  # I know that we have ~3150 tokens currently.

    data = req.json()

    for token_info in data['tokens']:
        address = token_info['address']

        # Check if this is for the correct chain
        if token_info['chainId'] != chain_id:
            print(f'Skipped {token_info["name"]} at {address}: Wrong chainId: {token_info["chainId"]}.')
            continue
        
        
        # Check if the backend has this token
        if address not in known_tokens:
            print(f'Skipped {token_info["name"]} at {address}: Not know to backend.')
            continue

        filename = f'{address}.png'
        # Check if icon has been downloaded already
        my_file = Path(filename)
        if my_file.exists:
            print(f'Skipped {token_info["name"]} at {address}: Icon already downloaded.')
            continue

        # Check if we already have an icon in the backend.
        known_icon_req = requests.get(known_tokens[address]['logoUri'])
        if known_icon_req.status_code == 200:
            print(f'Skipped {token_info["name"]} at {address}: We have an icon already.')
            continue

        # If all checks were (un)successful, then fetch the icon.
        token_list_icon_req = requests.get(token_info['logoURI'])
        if token_list_icon_req.status_code != 200:
            print(f'Skipped {token_info["name"]} at {address}: Could not load icon at {token_info["logoURI"]}')
            continue

        # Write logo to file with filename of rinkeby token address
        open(filename, 'wb').write(token_list_icon_req.content)
        print(f'{token_info["name"]} at {address}: Logo successfully downloaded.')