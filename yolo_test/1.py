from tkinter import *
import tkinter.ttk

import tkinter as tk
import time
import os

import sys
# import csv

from tkinter import messagebox

# from tkinter import filedialog

# 文件命名
now = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(time.time()))

file_name = now + ".txt"
new_name = file_name

pro_name = "记事本文件" + file_name
rename = pro_name

root = tkinter.Tk()
root.title(rename)
root.geometry("750x500")


# benbenhao = "20240315_1"

def pack_at():
    get_text = text.get("1.0", "end")
    fname = time.strftime(rename)
    with open(fname, 'w') as f:
        f.write(get_text)


def save_file():
    def save_position():
        def pack_at_fail():
            get_text = text.get("1.0", "end")
            with open(pro_name, 'w') as f:
                f.write(get_text)


