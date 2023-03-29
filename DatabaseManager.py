#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:00:02 2023

@author: dev
"""

import mysql.connector
import Cryptograph as crypt

def initializeDb():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Dev013@online",
      database="KeyVault"
    )

    return mydb

mydb = initializeDb()
#mycursor = mydb.cursor()

# Inserting Values
#sql = "INSERT INTO Vault (Platform, Vaultname, Keyvalue, Email) VALUES (%s, %s, %s, %s)"
#val = ("David", "California", "poqpwoe", "asdsafa")
#mycursor.execute(sql, val)
#
#mydb.commit()
#
#print(mycursor.rowcount, "record(s) inserted.")

# Selecting Values
#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM Vault LIMIT 5")
#myresult = mycursor.fetchall()

#insert(('1','2','3','5'))
#fetch('1')
#delete('1')

#for x in myresult:
#  print(x)
    


class DatabaseManager:
    
    def fetchAll(self):
        myCursor = mydb.cursor()
        mysql = "SELECT * FROM Vault LIMIT 5"
        myCursor.execute(mysql)
        myResult = myCursor.fetchall()
        print(myResult)
        return myResult
    
    def fetch(self, Platform):
        myCursor = mydb.cursor()
        mysql = "SELECT * FROM Vault WHERE Platform='{platform}'"
        myCursor.execute(mysql.format(platform=Platform))
        myResult = myCursor.fetchone()
        return myResult
        
    def check(self, username, password):
        myCursor = mydb.cursor()
        mysql = "SELECT * FROM Vault WHERE Vaultname='{vaultname}' AND BINARY Keyvalue='{keyvalue}'"
        myCursor.execute(mysql.format(vaultname=username, keyvalue=password))
        myResult = myCursor.fetchone()
        if myResult == None:
            return False
        return True
            
    def insert(self, values):
        myCursor = mydb.cursor()
        print(values)
        mysql = "INSERT INTO Vault (Platform, Vaultname, Keyvalue, Email) VALUES (%s, %s, %s, %s)"
        myCursor.execute(mysql, values)
        mydb.commit()
        return myCursor.rowcount
        
    def delete(self, Platform):
        myCursor = mydb.cursor()
        print(Platform)
        mysql = "DELETE FROM Vault WHERE Platform='{platform}'"
        myCursor.execute(mysql.format(platform=Platform))
        mydb.commit()
        print(myCursor.rowcount)

#d = DatabaseManager()
#d.fetchAll()