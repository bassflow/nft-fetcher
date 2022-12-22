#!/usr/bin/env python3

import json
import requests
from modules.db import db

from modules import const

addresses = const.load_json("nft-fetcher/data/myaddresses.json")


def get_erc721_transactions(address: str):
    """
    This functions calls the snowtrace API
    Account Module
    Action:Tokennfttxn &
    account where address is taken as argument
    """
    url = const.ERC721TXNURL + address
    response = requests.request("GET", url)
    return response.json()["result"]


def get_erc20_transactions(address: str):
    """
    This functions calls the snowtrace API
    Account Module
    Action:Tokentxn &
    account where address is taken as argument
    """
    url = const.ERC20TXNURL + address
    response = requests.request("GET", url)
    return response.json()["result"]


def get_erc1155_transactions(addres: str):
    url = const.ERC1155TXNURL + addresses
    response = requests.request("GET", url)
    return response.json()["result"]


def dump_erc721_txn():
    """
    This function uses the get_erc721_transactions function to call the data from Snowtrace
    Then it records all the transactions into Database tokennfttx
    It keeps track of the ammount of transactions and prints those in the command line
    after its done putting the data for the current address into the database
    """
    transaction_count = 0

    for address in addresses:
        transactions = get_erc721_transactions(address)
        print(address)

        for transaction in transactions:
            # txn dump
            db.record(
                """INSERT OR IGNORE INTO tokennfttx (
                    blocknumber, 
                    timestampint, 
                    hashnr, 
                    nonce, 
                    blockhash, 
                    fromaddress, 
                    contractaddress, 
                    toaddress, 
                    tokenid, 
                    tokenname, 
                    tokensymbol, 
                    tokendecimal, 
                    transactionindex, 
                    gas, 
                    gasprice, 
                    gasused, 
                    cumulativegasused, 
                    input,
                    confirmations
                    )
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (transaction["blockNumber"]),
                (transaction["timeStamp"]),
                (transaction["hash"]),
                (transaction["nonce"]),
                (transaction["blockHash"]),
                (transaction["from"]),
                (transaction["contractAddress"]),
                (transaction["to"]),
                (transaction["tokenID"]),
                (transaction["tokenName"]),
                (transaction["tokenSymbol"]),
                (transaction["tokenDecimal"]),
                (transaction["transactionIndex"]),
                (transaction["gas"]),
                (transaction["gasPrice"]),
                (transaction["gasUsed"]),
                (transaction["cumulativeGasUsed"]),
                (transaction["input"]),
                (transaction["confirmations"]),
            )
            transaction_count += 1

            db.commit()

        print(f"Done. Found {transaction_count} total transactions.")


def dump_erc20_txn():
    """
    This function uses the get_erc20_transactions function to call the data from Snowtrace
    Then it records all the transactions into Database tokentx
    It keeps track of the ammount of transactions and prints those in the command line
    after its done putting the data for the current address into the database
    """
    transaction_count = 0

    for address in addresses:
        transactions = get_erc20_transactions(address)
        print(address)

        for transaction in transactions:
            db.record(
                """
                INSERT OR IGNORE INTO tokentx (
                    blocknumber, 
                    timestampint, 
                    hashnr, 
                    nonce, 
                    blockhash, 
                    fromaddress, 
                    contractaddress, 
                    toaddress, 
                    value, 
                    tokenname, 
                    tokensymbol, 
                    tokendecimal, 
                    transactionindex, 
                    gas, 
                    gasprice, 
                    gasused, 
                    cumulativegasused, 
                    input,
                    confirmations
                    )
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (transaction["blockNumber"]),
                (transaction["timeStamp"]),
                (transaction["hash"]),
                (transaction["nonce"]),
                (transaction["blockHash"]),
                (transaction["from"]),
                (transaction["contractAddress"]),
                (transaction["to"]),
                (transaction["value"]),
                (transaction["tokenName"]),
                (transaction["tokenSymbol"]),
                (transaction["tokenDecimal"]),
                (transaction["transactionIndex"]),
                (transaction["gas"]),
                (transaction["gasPrice"]),
                (transaction["gasUsed"]),
                (transaction["cumulativeGasUsed"]),
                (transaction["input"]),
                (transaction["confirmations"]),
            )
            transaction_count += 1

            db.commit()

        print(f"Done. Found {transaction_count} total transactions.")
