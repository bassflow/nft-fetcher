import json
import time
import requests

import const

addresses = const.load_json("data/myaddresses.json")

        # Fetch token Transactions for each address

def get_erc721_transactions(address):
    url = const.TXNURL + address
    response = requests.request("GET", url)
    return response.json()['result']


def get_erc721_txn():
    txns = []
    transaction_count = 0

    for address in addresses:
        transactions = get_erc721_transactions(address)
        print(address)
        
        for transaction in transactions:
            #txn dump
            if transaction['to'] != str(const.DEAD):
                txns.append({
                    'time_stamp': const.timestamp_to_time_and_date(int(transaction['timeStamp'])),
                    'contract_address': transaction['contractAddress'],
                    'token_id': transaction['tokenID'],
                    'to_address': transaction['to'],
                    'from_address': transaction['from']
                })
                transaction_count += 1
                const.dump_json("data/nfttx.json", txns)
                #with open('data/nfttx.json', 'w') as outfile:
                    #json.dump(txns, outfile, indent=4)
        
        print(f'Done. Found {transaction_count} total transactions.')

#// TODO: fetch token URI for each Token ID

#// TODO: fetch image/video link for each  TokenURI

get_erc721_txn()