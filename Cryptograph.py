# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from cryptography.fernet import Fernet
key = b'tUrzsMQD_XMYVHTmwIzGL8hoFlh8ooyMGqIQG9ytqJk='
fernet = Fernet(key)

def encode(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def decode(encMessage):
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage

