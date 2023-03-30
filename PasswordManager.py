#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:43:19 2023

@author: dev
"""

import Cryptograph as coder
import DatabaseManager as db
import PasswordManager_Create as create
import PasswordManager_Read as read

from tkinter import Tk, messagebox, StringVar, ttk

class PasswordManager:
    
    def __init__(self):
        self.dbManager = db.DatabaseManager()
        self.cryptoManager = coder.Cryptograph()
        self.root = Tk()
        self.root.title("Login")
        self.mainframe = ttk.Frame(self.root, padding="10 10 30 30")
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("350x200")
        ttk.Label(self.mainframe, text="Name").grid(column=1, row=2, sticky='W')
        self.username = StringVar()
        self.username_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.username)
        self.username_entry.grid(column=3, row=2, sticky=('W','E'))
        ttk.Label(self.mainframe, text="          ").grid(column=2, row=3, sticky=('W'))
        ttk.Label(self.mainframe, text="Password").grid(column=1, row=4, sticky='W')
        self.password = StringVar()
        self.password_entry = ttk.Entry(self.mainframe, width=17, textvariable=self.password, show='*')
        self.password_entry.grid(column=3, row=4, sticky='W')
        ttk.Label(self.mainframe, text="          ").grid(column=2, row=5, sticky=('W'))
        ttk.Button(self.mainframe, text="Login", command=self.check_password).grid(column=2, row=6, sticky=('W','E'))
    
    def run(self):
        self.root.mainloop()

    def check_password(self, *args):
        uname = self.username.get()
        pswd = self.password.get()
        if(self.dbManager.check(uname, pswd)):
            self.main_window()
            self.root.quit()
        else:
            messagebox.showerror("Login Failed", "Incorrect UserName or Password")
        
    def openPasswordManager_create(self):
        createManager = create.PasswordManager_create()
        createManager.run()
        
    def openPasswordManager_read(self):
        readManager = read.PasswordManager_Read()
        readManager.run()
    
        # Having the Create and Read Function for now
    def main_window(self):
        self.mainroot = Tk()
        self.mainroot.title("Password Manager")
        
        self.mainframe = ttk.Frame(self.mainroot, padding="10 10 30 30")
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        self.mainroot.columnconfigure(0, weight=1)
        self.mainroot.rowconfigure(0, weight=1)
        self.mainroot.geometry("350x200")
        ttk.Button(self.mainframe, text="Create", command=self.openPasswordManager_create).grid(column=0, row=2, sticky=('W','E'))
        ttk.Label(self.mainframe, text="          ").grid(column=3, row=2, sticky=('W'))
        ttk.Button(self.mainframe, text="Read", command=self.openPasswordManager_read).grid(column=4, row=2, sticky=('W','E'))
        self.mainroot.mainloop()
        
if __name__ == "__main__":
    myApp = PasswordManager()
    myApp.run()