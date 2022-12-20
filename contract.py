import json
import time
import requests
import const
from selenium import webdriver


contract = "0xcf0f4519f2f55ef40e2dddcb7c99893297e40336"
driver = webdriver.Chrome(const.CWDPATH)
search = driver.find_element("form-control form-control-xs")


def launchBrowser():
    driver.get(const.ADDRESSURL + contract + const.READCONTRACT)
    while True:
        pass


launchBrowser()


def enterTokenID():
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
    while True:
        pass


enterTokenID()
# nftcontracts = open("data/nfttx.json", "r")
# contract = json.load(nftcontracts["contract_address"])


# def get_erc721_smartcontract(contract):
#    url = const.ABIURL + addres
#    reponse = requests.request("GET", url)
#    return reponse.json()["result"]
