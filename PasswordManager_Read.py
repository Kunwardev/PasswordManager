#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:22:21 2023

@author: dev
"""

import Cryptograph as coder
import DatabaseManager as db
from tkinter import Tk, StringVar, ttk, messagebox

class PasswordManager_Read:
    
    def getValue(self):
        platform = self.platform.get()
        print(platform)
        self.vaultname = StringVar()
        self.keyvalue = StringVar()
        self.email = StringVar()
        
        if platform == '':
            messagebox.showinfo(title="Empty Platform", message="Please Fill Platform")
        else:
            fetchedvalues = (self.dbManager.fetch(platform))
            self.vaultname = fetchedvalues[1]
            self.keyvalue = self.cryptoManager.decode(bytes(fetchedvalues[2], encoding='utf8'))
            self.email = fetchedvalues[3]
            
            ttk.Label(self.mainframe, text="User Name").grid(column=1, row=8, sticky=('W'))
            ttk.Label(self.mainframe, text=self.vaultname).grid(column=3, row=8, sticky=('W'))
            ttk.Label(self.mainframe, text="Password").grid(column=1, row=10, sticky=('W'))
            ttk.Label(self.mainframe, text=self.keyvalue).grid(column=3, row=10, sticky=('W'))
            ttk.Label(self.mainframe, text="Email").grid(column=1, row=12, sticky=('W'))
            ttk.Label(self.mainframe, text=self.email).grid(column=3, row=12, sticky=('W'))
        
        
    
    def __init__(self):
        self.dbManager = db.DatabaseManager()
        self.cryptoManager = coder.Cryptograph()
        self.root = Tk()
        self.root.title("Get Values")
        self.mainframe = ttk.Frame(self.root, padding="10 10 30 30")
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("400x250")
        ttk.Label(self.mainframe, text="Platform").grid(column=1, row=2, sticky='W')
        self.platform = StringVar()
        self.platform_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.platform)
        self.platform_entry.grid(column=3, row=2, sticky=('W','E'))
        ttk.Label(self.mainframe, text="          ").grid(column=2, row=3, sticky=('W'))
        ttk.Button(self.mainframe, text="Get Values", command=self.getValue).grid(column=2, row=6, sticky=('W','E'))
        
        
    def run(self):
        self.root.mainloop()
