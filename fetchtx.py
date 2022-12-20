#!/usr/bin/env python3

import json
import time
import requests
import sqlite3

import const

addresses = const.load_json("data/myaddresses.json")


def get_erc721_transactions(address):
    """
    This functions calls the snowtrace API
    Account Module
    Action:Tokennfttxn &
    accoutn where address is taken as argument
    """
    url = const.TXNURL + address
    response = requests.request("GET", url)
    return response.json()["result"]


def get_erc721_txn():
    """
    This function uses the get_erc721_transactions function to call the data from Snowtrace
    Then appends the needed data and dumps those into a nfttx.json.
    It keeps track of the ammount of transactions and prints those in the command line
    after its done putting the data for the current address into the .json
    """
    txns = []
    transaction_count = 0

    for address in addresses:
        transactions = get_erc721_transactions(address)
        print(address)

        for transaction in transactions:
            # txn dump
            if transaction["to"] != str(const.DEAD):
                txns.append(
                    {
                        "time_stamp": const.timestamp_to_time_and_date(int(transaction["timeStamp"])),
                        "contract_address": transaction["contractAddress"],
                        "token_id": transaction["tokenID"],
                        "to_address": transaction["to"],
                        "from_address": transaction["from"],
                    }
                )
                transaction_count += 1
                const.dump_json("data/nfttx.json", txns)
                # with open('data/nfttx.json', 'w') as outfile:
                # json.dump(txns, outfile, indent=4)

        print(f"Done. Found {transaction_count} total transactions.")


# // TODO: fetch token URI for each Token ID

# // TODO: fetch image/video link for each  TokenURI

get_erc721_txn()
