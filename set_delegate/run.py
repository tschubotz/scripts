import requests
from eth_account import Account
import time
from eth_utils import keccak

SAFE_ADDRESS = '0xaE3c91c89153DEaC332Ab7BBd167164978638c30'
OWNER_PRIVATE_KEY = ''
DELEGATE_ADDRESS = '0x1230B3d59858296A31053C1b8562Ecf89A2f888b'

TX_SERVICE_BASE_URL = 'https://safe-transaction.rinkeby.gnosis.io'

def main():
    
    # List delegates
    list_response = requests.get(f'{TX_SERVICE_BASE_URL}/api/v1/safes/{SAFE_ADDRESS}/delegates')

    print(list_response.text)
    print(list_response.status_code)

    # Add delegate 
    totp = int(time.time()) // 3600
    hash_to_sign = keccak(text=DELEGATE_ADDRESS + str(totp))
    account = Account.from_key(OWNER_PRIVATE_KEY)
    signature = account.signHash(hash_to_sign)

    add_payload = {
        "safe": SAFE_ADDRESS,
        "delegate": DELEGATE_ADDRESS,
        "signature": signature.signature.hex(),
        "label": "My new delegate2"
    }
    
    add_response = requests.post(f'{TX_SERVICE_BASE_URL}/api/v1/safes/{SAFE_ADDRESS}/delegates/', json=add_payload, headers = {'Content-type': 'application/json'})
    
    print(add_response.text)
    print(add_response.status_code)
    
    # Remove delegate

    delete_payload = {
        "signature": signature.signature.hex(),
    }
    delete_response = requests.delete(f'{TX_SERVICE_BASE_URL}/api/v1/safes/{SAFE_ADDRESS}/delegates/{DELEGATE_ADDRESS}/', json=delete_payload, headers = {'Content-type': 'application/json'})

    print(delete_response.text)
    print(delete_response.status_code)

main()