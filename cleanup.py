#! usr/bin/python3
# filename: cleanup.py
import pyperclip
import re
import os

sepReg = re.compile(r' +\||\|\s+(?!\n)')
tableReg = re.compile(r'\+?-+\+|->')
lineReg = re.compile(r'mysql> mysql>?|mysql>')
endReg = re.compile(r';')
emptylineReg = re.compile(r'mysql>\n')
doubles = '||'


def clean_up_markup(text):
    extracted_seps = sepReg.search(text)
    extracted_table = tableReg.search(text)
    extracted_line = lineReg.search(text)
    extracted_end = endReg.search(text)
    extracted_empty = emptylineReg.search(text)
    if extracted_seps:
        text = sepReg.sub('|', text)
    if extracted_table:
        text = tableReg.sub('', text)
    if extracted_line:
        text = lineReg.sub('{code:sql} ', text)
    if extracted_end:
        text = endReg.sub('; {code}\n ', text)
    if extracted_empty:
        text = emptylineReg.sub('\n', text)

    text = text.replace('||', '|-|')
    text = os.linesep.join([s for s in text.splitlines() if s])

    pyperclip.copy(text)
