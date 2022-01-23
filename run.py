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



    if shortCode == 'cc' :

      print('\n')

      print('New Account Credentials:')

      print('-' * 24)

      print('Account Name:')
      account = input()

      print('Username:')
      username = input()

      print('Password:')
      password = input()

      saveAccount(createAccount(account, username, password))

      print('\n')

      print(f'Successful. Credentials for your {account} account have been created.')

      print('\n')



    elif shortCode == 'dc' :

      if displayAccounts() :

        print('Successful.\nBelow are your credentials saved with us...')

        print('\n')

        for account in displayAccounts() :

          print(f'Account: {account.account}\n-->Username: {account.username}\n-->Password: {account.password}')

          print('\n')

      else :

        print('\n')

        print('Oops! Your vault is empty.\nSpare yourself the memory hustle and save your credentials with us.')

        print('\n')

















