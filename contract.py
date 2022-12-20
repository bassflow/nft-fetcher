#!/usr/bin/env python3

import json
import time
import requests
import const


# contract = "0xcf0f4519f2f55ef40e2dddcb7c99893297e40336"

nftcontracts = open("data/nfttx.json", "r")
contract = json.load(nftcontracts)
