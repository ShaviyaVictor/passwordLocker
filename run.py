#!/usr/bin/env python 3.8

from account import Account


def intro() :
  print("               ____                        _                        _    _      ")
  print("              |  _ \                      | |                      | | / /      ")
  print("              | |_) )  ____  ___   ___    | |      _____     ____  | |/ /       ")
  print("              |  __/  / _  |/ __  / __    | |     /  _  \   / ___| | | :        ")
  print("              | |    / (_| |\__ \ \__ \ - | |___ (  (_)  ) | |___  | |\ \       ")
  print("              |_|    \_____| ___/  ___/   |_____) \_____/   \____| |_| \_\      ")
intro()



def createAccount(account, username, password) :
  '''
  Function that creates a new account
  '''

  newAccount = Account(account, username, password)

  return newAccount


def saveAccount(account) :
  '''
  Function to save our accounts
  '''

  account.saveAccount()



def deleteAccount(account) :
  '''
  Function to delete an account
  '''

  account.deleteAccount()



def findAccount(account) :
  '''
  Function that finds an account by account and returns the account
  '''

  return Account.findAccountByAcc(account)



def accountExists(account) :
  '''
  Function that checks if an account exists with that account name and return a Boolean
  '''

  return Account.accountExists(account)



def displayAccounts() :
  '''
  Function that returns all the saved accounts
  '''

  return Account.displayAccounts()





def main() :
  print('Hallo, Welcome to your Pass-Vault.\nWhat is your name?')

  user = input()

  print('\n')

  print(f'Hello {user},\nDo you have an account with us?\n(Notice!Notice!Notice!\nDear {user}, you can only save 4 accounts with a free subscription account.)')

  print('\n')

  while True :
    print('Use these short-codes:\ncc - to create new account credentials...\ndc - to display your credentials...\nfc - to find a saved account...\nex - to exit the vault.')

    shortCode = input().lower()

    








