from ethereum.utils import ecsign
from eth_account.account import Account
import codecs
import json
import web3

private_key = ''

def main_func():
    print(123)

    safe_tx_hash = codecs.decode('9436d1513f7a822ef30e87f59bbf2d8eda830c811fa11e9fa078c0113af7e9e6', 'hex_codec')

    address = Account.privateKeyToAccount(private_key).address

    print(address)

    v, r, s = ecsign(safe_tx_hash, codecs.decode(private_key, 'hex_codec'))
    signature = {'v': v, 'r': r, 's': s}
    print('Signature:\n\n{}'.format(json.dumps(signature)))

    byte_order = 'big'

    x = r.to_bytes(32, byteorder=byte_order) + s.to_bytes(32, byteorder=byte_order) + v.to_bytes(1, byteorder=byte_order)
    print(x.hex())

main_func()