import json
import time
import requests

nftcontracts = open("data/nfttx.json", "r")
contract = json.load(nftcontracts["contract_address"])

def get_erc721_smartcontract(contract):
    url = const.ABIURL + addres
    reponse = requests.request("GET", url)
    return reponse.json()["result"]
