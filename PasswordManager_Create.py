#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 00:27:05 2023

@author: dev
"""

import Cryptograph as coder
import DatabaseManager as db
import RandomPasswordGenerator as rpg
from tkinter import Tk, simpledialog, StringVar, ttk, messagebox

class PasswordManager_create:

    def random(self, *args):
        self.length = simpledialog.askinteger(title="Generate Password", prompt="Enter the length of password to generate: ")
        if self.length == None:
            self.length = 0
        self.keyvalue.set(self.generator.generate(self.length))
        
    def create(self, *args):
        try:
            encrypted = self.crypter.encode(self.keyvalue.get())
            platform = self.platform.get()
            values = (platform, self.vaultname.get(), encrypted, self.email.get())
            print("PLATFORM: ",self.platform.get())
            created = self.dbManager.insert(values)
            if created == 1:
                txt = "The row has been added for {platform} with Username: {username} and Password: {password}"
                messagebox.showinfo(title="Added Value", message=txt.format(platform=values[0], username=values[1], password=self.keyvalue.get()))
        except:
            messagebox.showerror(title="Exception", prompt="Something went wrong, Try again!")

    def __init__(self):
        self.root = Tk()
        self.generator = rpg.RandomPasswordGenerator()
        self.dbManager = db.DatabaseManager()
        self.crypter = coder.Cryptograph()
        
        self.root.title("Password Manager")
        self.mainframe = ttk.Frame(self.root, padding="7 7 16 16")
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("400x350")
        
        self.platform = StringVar()
        self.platform_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.platform)
        self.platform_entry.grid(column=3, row=1, sticky=('W','E'))
        ttk.Label(self.mainframe, text="     ").grid(column =3, row=2, sticky='W')
        self.vaultname = StringVar()
        self.vaultname_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.vaultname)
        self.vaultname_entry.grid(column=3, row=3, sticky=('W','E'))
        ttk.Label(self.mainframe, text="     ").grid(column =3, row=4, sticky='W')
        self.keyvalue = StringVar()
        self.keyvalue_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.keyvalue)
        self.keyvalue_entry.grid(column=3, row=5, sticky=('W','E'))
        ttk.Label(self.mainframe, text="     ").grid(column =3, row=6, sticky='W')
        self.email = StringVar()
        self.email_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.email)
        self.email_entry.grid(column=3, row=7, sticky=('W','E'))
        ttk.Label(self.mainframe, text="     ").grid(column =3, row=8, sticky='W')
        
        ttk.Button(self.mainframe, text="Save", command=self.create).grid(column=2, row=10, sticky='W')
        ttk.Button(self.mainframe, text="Random", command=self.random).grid(column=3, row=10, sticky='E')
        
        ttk.Label(self.mainframe, text="Platform").grid(column=1, row=1, sticky='W')
        ttk.Label(self.mainframe, text="     ").grid(column =1, row=2, sticky='W')
        ttk.Label(self.mainframe, text="Vaultname").grid(column=1, row=3, sticky='W')
        ttk.Label(self.mainframe, text="     ").grid(column =1, row=4, sticky='W')
        ttk.Label(self.mainframe, text="KeyValue").grid(column=1, row=5, sticky='W')
        ttk.Label(self.mainframe, text="     ").grid(column =1, row=6, sticky='W')
        ttk.Label(self.mainframe, text="Email").grid(column=1, row=7, sticky='W')
        ttk.Label(self.mainframe, text="     ").grid(column =1, row=8, sticky='W')
        
    def run(self):
        self.root.mainloop()

#p = PasswordManager_create()
#p.run()