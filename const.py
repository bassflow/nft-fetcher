#!/usr/bin/env python3

import datetime
import json


DEAD = "0x000000000000000000000000000000000000dead"
MINT = "0x0000000000000000000000000000000000000000"
TXNURL = "https://api.snowtrace.io/api?module=account&action=tokennfttx&address="
ADDRESSURL = "https://snowtrace.io/address/"
ABIURL = "https://api.snowtrace.io/api?module=contract&action=getabi&address="
CWDPATH = "C:\Program Files (x86)\chromedriver.exe"
URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
READCONTRACT = "#readContract"
WRITECONTRACT = "#writeContract"
CODECONTRACT = "#code"


def timestamp_to_time_and_date(timestamp):
    """
    This Function converts a timestamp to a readable format:
    e.g. March 31, 2022, 01:20 PM
    """
    dt = datetime.datetime.fromtimestamp(timestamp)

    date = dt.strftime("%B %d, %Y")
    time = dt.strftime("%I:%M, %p")

    return (date, time)


def load_json(filename):
    """
    This Function loads a json file, take the filename as argument.
    """
    with open(filename, "r") as f:
        data = json.load(f)

    return data


def dump_json(filename, arg):
    """
    This function dumps data into a json file, taking filename and and the list to dump as arguments.
    """
    with open(filename, "w") as of:
        json.dump(arg, of, indent=4)
