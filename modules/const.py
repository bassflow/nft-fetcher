#!/usr/bin/env python3

import datetime
import json
import requests

""" Addresses """
DEAD = "0x000000000000000000000000000000000000dead"  # Burn address
MINT = "0x0000000000000000000000000000000000000000"  # Mint address

""" Links"""
ERC721TXNURL = (
    "https://api.snowtrace.io/api?module=account&action=tokennfttx&address="  # API Link for ERC721 Transactions
)
ERC20TXNURL = "https://api.snowtrace.io/api?module=account&action=tokentx&address="  # API Link for ERC20 Transactions
ERC1155TXNURL = "https://api.snowtrace.io/api?module=account&action=tokentxns-nft1155&addres="
ADDRESSURL = "https://snowtrace.io/address/"  # Snowtrace addres link for contracts and wallets
ABIURL = "https://api.snowtrace.io/api?module=contract&action=getabi&address="  # API Link for Contract ABI
RPC_URL = "https://api.avax.network/ext/bc/C/rpc"  # RPC URL
IPFSURL = "https://ipfs.io/ipfs/"  # IPFS Prefix for Metadata & Image/Video links

"""File locations"""
CWDPATH = "C:\Program Files (x86)\chromedriver.exe"  # Path to chrome Web Driver
MYADDRESSES = "nft-fetcher/data/myaddresses.json"  # Path for myaddresses File
BUILD_PATH = "nft-fetcher/data/build.sql"  # Path for Database Build file .sql
DB_PATH = "nft-fetcher/data/database.db"  # Path for Database location

"""Regex"""
URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

"""Suffix for selenium web scraping"""
READCONTRACT = "#readContract"  # open the read section of the contract
WRITECONTRACT = "#writeContract"  # open the write section of the contract
CODECONTRACT = "#code"  # open the code section of the contract

"""GUI Settings for tkinter"""
RESOLUTION = "600x400"
ICON_LOGO = "nft-fetcher/ui/avalanche-avax-logo.png"
BG1_COLOR = "#1D3557"  # Cello
BG2_COLOR = "#457B9D"  # Wedgewood
BG3_COLOR = "#A8DADC"  # Aqua Island
FG1_COLOR = "#F1FAEE"  # Peppermint
ACC_COLOR = "#E63946"  # Amaranth
FONT = "Comic Sans"
FONT_SIZE1 = 18
FONT_SIZE2 = 10


"""Basic functions used troughout the code"""


def timestamp_to_time_and_date(timestamp: int):
    """
    This Function converts a timestamp to a readable format:
    e.g. March 31, 2022, 01:20 PM
    """
    dt = datetime.datetime.fromtimestamp(timestamp)

    date = dt.strftime("%B %d, %Y")  # Extracts the date and returns a readable format: March 31, 2022
    time = dt.strftime("%I:%M, %p")  # Extracts the time and returns a readable format: 01:20 PM

    return (date, time)


def getABI(contract_address):
    url = ABIURL + contract_address
    reponse = requests.request("GET", url)
    return reponse.json()["result"]


def load_json(filename: str):
    """
    This Function loads a json file from the file specified in filename as a string.
    """
    with open(filename, "r") as f:
        data = json.load(f)

    return data


def dump_json(filename: str, arg):
    """
    This function dumps data into a json file, taking filename and and the list to dump as arguments.
    """
    with open(filename, "w") as of:
        json.dump(arg, of, indent=4)
