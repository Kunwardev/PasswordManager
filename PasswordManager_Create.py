#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 00:27:05 2023

@author: dev
"""

import Cryptograph as coder
import DatabaseManager as db

from tkinter import *
from tkinter import ttk

def create(*args):
    try:
        pass
    except:
        pass

def makeWindow():
    root = Tk()
    root.title("Password Manager")
    
    mainframe = ttk.Frame(root, padding="7 7 16 16")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    platform = StringVar()
    platform_entry = ttk.Entry(mainframe, width=17, textvariable=platform)
    platform_entry.grid(column=3, row=1, sticky=(W,E))
    vaultname = StringVar()
    vaultname_entry = ttk.Entry(mainframe, width=17, textvariable=vaultname)
    vaultname_entry.grid(column=3, row=2, sticky=(W,E))
    keyvalue = StringVar()
    keyvalue_entry = ttk.Entry(mainframe, width=17, textvariable=keyvalue)
    keyvalue_entry.grid(column=3, row=3, sticky=(W,E))
    email = StringVar()
    email_entry = ttk.Entry(mainframe, width=17, textvariable=email)
    email_entry.grid(column=3, row=4, sticky=(W,E))
    
    #meters = StringVar()
    #ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
    
    ttk.Button(mainframe, text="Save", command=create).grid(column=2, row=6, sticky=W)
    
    ttk.Label(mainframe, text="Platform").grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe, text="Vaultname").grid(column=1, row=2, sticky=W)
    ttk.Label(mainframe, text="KeyValue").grid(column=1, row=3, sticky=W)
    ttk.Label(mainframe, text="Email").grid(column=1, row=4, sticky=W)
    
    root.mainloop()