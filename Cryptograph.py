# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from cryptography.fernet import Fernet

class Cryptograph:
    
    def __init__(self):
        self.key = b'tUrzsMQD_XMYVHTmwIzGL8hoFlh8ooyMGqIQG9ytqJk='
        self.fernet = Fernet(self.key)

    def encode(self, message):
        encMessage = self.fernet.encrypt(message.encode())
        return encMessage

    def decode(self, encMessage):
        decMessage = self.fernet.decrypt(encMessage).decode()
        return decMessage