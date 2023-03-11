#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:22:55 2023

@author: dev
"""

import random
import string

class RandomPasswordGenerator:
    
    def generate(self, length):
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
    
        password = ''.join(random.choice(letters + digits + symbols) for i in range(length))
    
        return password