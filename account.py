# Import the module for Copy() Paste() behavior functionality
import pyperclip




class Account :
  '''
  Class Account that generates new instances of contacts

  Use pass keyword to allow creation of empty block of code so as to return a null or nothing when it runs
  '''

  # pass



  accountList = []
  '''
  Declare a class variable that'll belong to the entire class and will be accessed by all instances of the class
  The variable will be used to store our created account objects 
  '''



  def __init__(self, account, username, password) :
    '''
    __init__ method declaration that helps us define properties for our various account objects.
    self is a variable that represents the instance of the object itself
    
    Args :
      account : New account type name.
      username : New username for the account.
      phone : New password for the account.
    '''

    self.account = account
    self.username = username
    self.password = password



  def saveAccount(self) :
    '''
    Create the method to save objects into the accountList[]
    '''
    Account.accountList.append(self)



  def deleteAccount(self) :
    '''
    Create the method to delete objects from the accountList
    '''
    Account.accountList.remove(self)



  @classmethod
  def findAccountByAcc(cls, account) :
    '''
    Method that takes in an account and returns credentials that match that account

    Args:
      account: The account credentials to search for

    Returns:
      Account of person that matches the account
    '''

    for account in cls.accountList :
      if account.account == account :

        return account


      
  @classmethod
  def accountExists(cls, account) :
    '''
    Method that checks if an account exists from the accountList[]

    Args :
      account : account to search if it exists

    Returns :
      Boolean : True or false depending on if the account exists
    '''

    for account in cls.accountList :
      if account.account == account :

        return True

      return False



  @classmethod
  def displayAccounts(cls) :
    '''
    Method that returns the accountList
    '''

    return cls.accountList



  @classmethod
  def copyUsername(cls, account) :

    accountFound = Account.findAccountByAcc(account)

    pyperclip.copy(accountFound.account)
