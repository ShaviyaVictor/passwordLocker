




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




