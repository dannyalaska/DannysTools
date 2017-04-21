#!/usr/bin/python3
# filename: runscripts.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
from MyGUI import cleanup
from MyGUI import scp_to_from
from MyGUI import list_this


def callback_scp_from():
    entry = pyperclip.paste()
    scp_to_from.scp_from(entry)
    messagebox.showinfo(message='Commands printed in Console')


def callback_scp_to():
    entry = pyperclip.paste()
    scp_to_from.scp_to(entry)
    messagebox.showinfo(message='Commands printed in Console')


def callback_cleanup():
    text = pyperclip.paste()
    cleanup.clean_up_markup(text)


def callback_list():
    mylist = pyperclip.paste()
    list_this.list_no_quotes(mylist)


def callback_list_quotes():
    mylist = pyperclip.paste()
    list_this.list_quotes(mylist)


# create window
def main():
    root = tk.Tk()
    style = ttk.Style()
    root.title('Danny\'s Tools')
    # set styling
    style.theme_use('default')
    style.configure('TButton',
                    background='firebrick',
                    foreground='white smoke',
                    font='Helvetica 16',
                    width=21,
                    borderwidth=2)
    style.map('TButton',
              foreground=[('pressed', 'sea green'),
                      ('active', 'firebrick')],
              background=[('pressed', '!focus', 'cyan'),
                      ('active', 'white smoke')],
              relief=[('pressed', 'groove'),
                  ('!pressed', 'raised')])
    # add widgets with callbacks
    scp_from = ttk.Button(root, text="Copy From / Zip", command=callback_scp_from).pack()
    scp_to = ttk.Button(root, text="Copy To", command=callback_scp_to).pack()
    clean = ttk.Button(root, text="Cleanup Markup", command=callback_cleanup).pack()
    lister_no = ttk.Button(root, text="Make List: No Quotes", command=callback_list).pack()
    lister_quotes = ttk.Button(root, text='Make List: Quotes', command=callback_list_quotes).pack()
    # run
    root.mainloop()

if __name__ == "__main__":
    main()
