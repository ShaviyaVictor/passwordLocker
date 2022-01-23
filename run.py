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








