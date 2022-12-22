#!/usr/bin/env python3


"""
Write function to have an executable URI Grabber, redo the CONTRACT & ID = to have it 
get the correct info from the database

"""

import web3
from web3.middleware import geth_poa_middleware
import json
import requests

from modules import const

CONTRACT = "0x54e957E991546a40032BbF18ba5fc2a627d2Dcee"
ID = 186

w3 = web3.Web3(web3.Web3.HTTPProvider(const.RPC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


def fetch_token_uri(contract, id):
    contract = w3.eth.contract(address=w3.toChecksumAddress(CONTRACT), abi=const.getABI(CONTRACT))

    token_uri = contract.functions.tokenURI(ID).call()
    print(token_uri)
    # Fetch info from database

    # Insert into database
    db.record(
        """INSERT OR IGNORE INTO nftholding (
            contractaddres,
            tokenid,
            tokenuri
            ) 
            VALUES (?,?,?)""",
        (contract_addres),
        (tokenid),
        (token_uri),
    )

    db.commit()
