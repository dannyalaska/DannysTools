#!/usr/bin/python3
# Filename: list_this.py
import pyperclip


def list_no_quotes(mylist):
    # this could be one-lined but is broken up for improved readability
    mylist = str(mylist.split('\n')).strip('[').strip(']').replace(r'\r', r",").replace(r"'", "")
    pyperclip.copy(mylist)


def list_quotes(mylist):
    # this could be one-lined but is broken a little up to improve readability
    split_on_lines = str(mylist.split('\n')).strip('[').strip(']').replace(r'\r', r"', '")
    pyperclip.copy(split_on_lines)
