#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:00:02 2023

@author: dev
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dev013@online",
  database="KeyVault"
)

print(mydb)

mycursor = mydb.cursor()

# Inserting Values
#sql = "INSERT INTO Vault (Platform, Vaultname, Keyvalue, Email) VALUES (%s, %s, %s, %s)"
#val = ("David", "California", "poqpwoe", "asdsafa")
#mycursor.execute(sql, val)
#
#mydb.commit()
#
#print(mycursor.rowcount, "record(s) inserted.")

# Selecting Values
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Vault LIMIT 5")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)