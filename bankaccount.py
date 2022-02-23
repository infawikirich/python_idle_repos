"""
Script file: bankaccount.py


Purpose: This program learns about the
OOP (Object oriented programming)
Private and public class

Date: 08/22/21

Author: Mr. Asiamah

"""

import os

# change the working directory
os.chdir("C:\\Users\\CBAS\\Documents\\Python Scripts\\Python IDLE")

# creat the Back Accunt class
class BankAccount:
    def __init__(self, accountHolder):
        """ BankAccount methods can access self._balance, but code outside of
            this class should not:
        """
        self._balance = 0
        self._name = accountHolder
        with open(self._name + "Ledger.txt", 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <=0:
            return  # Don't allow negative "defposit"
        self._balance += amount
        with open(self._name + "Ledger.txt", 'a') as ledgerFile:
            ledgerFile.write("Deposit " + str(amount) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return  #Not enough in accountm or withdraw is negative
        self._balance -= amount
        with open(self._name + "Ledger.txt", 'a') as ledgerFile:
            ledgerFile.write("Withdraw " + str(amount) + "\n")
            ledgerFile.write("Balance is " + str(self._balance) + '\n')











            

        
