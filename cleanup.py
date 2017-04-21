#! usr/bin/python3
# filename: cleanup.py
import pyperclip
import re
import os


tableReg = re.compile(r'\+?-+\+|->')
lineReg = re.compile(r'mysql> mysql>?|mysql>')
endReg = re.compile(r';')
emptylineReg = re.compile(r'mysql>\n')


def clean_up_markup(text):
    extracted_table = tableReg.search(text)
    extracted_line = lineReg.search(text)
    extracted_end = endReg.search(text)
    extracted_empty = emptylineReg.search(text)

    if extracted_table:
        text = tableReg.sub('\r', text)
    if extracted_line:
        text = lineReg.sub('{code:java} ', text)
    if extracted_end:
        text = endReg.sub('; {code}\n ', text)
    if extracted_empty:
        text = emptylineReg.sub('\n', text)

    text = os.linesep.join([s for s in text.splitlines() if s])

    pyperclip.copy(text)

