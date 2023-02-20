#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:43:19 2023

@author: dev
"""

import Cryptograph as coder
import DatabaseManager as db

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Success').grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.quit).grid(column=1, row=0)
root.mainloop()