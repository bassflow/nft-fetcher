#!/usr/bin/env python3


import web3
from web3.middleware import geth_poa_middleware
import json
import requests

from modules import const


w3 = web3.Web3(web3.Web3.HTTPProvider(const.RPC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


addresses = const.load_json("nft-fetcher/data/myaddresses.json")


def whitelist_checker(contract):
    contractabi = w3.eth.contract(address=w3.toChecksumAddress(contract), abi=const.getABI(contract))
    for address in addresses:
        wlstate = contractabi.functions.whiteListed(w3.toChecksumAddress(address)).call()
        if wlstate:
            print(f"whitelisted")
        else:
            print(f" not  whitelisted")
