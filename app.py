#!/usr/bin/env python3

import os

import tkinter as tk
from tkinter import filedialog, Text

import modules
from modules import db, const

__author__ = "Bart Pekelaer"
__copyright__ = "Copyright 2022, Bart Pekelaer"
__credits__ = ["Lawfulmonk"]

__licence__ = "MIT"
__version__ = "0.0.1"
__application__ = "Avalanche NFT Downloader"
__maintainer__ = "Bart Pekelaer"
__twitter__ = "BPekelaer"
__status__ = "Production"


root = tk.Tk()
iconlogo = tk.PhotoImage(file=const.ICON_LOGO)

root.geometry(const.RESOLUTION)  # Resolution
root.title(__application__)  # Title Name (Windows window)
root.iconphoto(False, iconlogo)  # Title Icon (Windows window)
root.configure(bg=const.ACC_COLOR)  # Background Color

label = tk.Label(root, text="Test", font=(const.FONT, const.FONT_SIZE1), bg=const.ACC_COLOR)
label.pack(padx=20, pady=20)

# textbox = tk.Text(root, height=1, font=(const.FONT, const.FONT_SIZE2))
# textbox.pack()

# myentry = tk.Entry(root)
# myentry.pack(pady=10)

nftbutton = tk.Button(
    root,
    text="Fetch ERC721 Transactions",
    font=(const.FONT, const.FONT_SIZE2),
    command=modules.dump_erc721_txn,
    fg=const.FG1_COLOR,
    bg=const.BG2_COLOR,
)  # Button to execute dump_erc721_txn
nftbutton.pack(pady=10)

tokenbutton = tk.Button(
    root,
    text="Fetch ERC20 Transactions",
    font=(const.FONT, const.FONT_SIZE2),
    command=modules.dump_erc20_txn,
    fg=const.FG1_COLOR,
    bg=const.BG2_COLOR,
)
tokenbutton.pack(pady=10)

wlentry = tk.Entry(
    root,
    text="Enter 0x Address to check",
    font=(const.FONT, const.FONT_SIZE2),
    fg=const.FG1_COLOR,
    bg=const.BG2_COLOR,
    width=30,
)
wlentry.pack(pady=10)


def get_wlentry():
    wl_entry = wlentry.get()
    modules.whitelist_checker(wl_entry)


wlbutton = tk.Button(
    root,
    text="Check Whitelist",
    font=(const.FONT, const.FONT_SIZE2),
    command=get_wlentry,
    fg=const.FG1_COLOR,
    bg=const.BG2_COLOR,
    width=30,
)
wlbutton.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
