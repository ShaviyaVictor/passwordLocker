# Import the unittest module
import unittest

# Import the Account class
from account import Account

class testAccount(unittest.TestCase) :
  '''
  Create a subclass test class that defines test cases for the Account class behaviours

  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''


  def setUp(self) :
    '''
    setUp() method to run before each test case

    Create new account object to facilitate the pre-tests
    '''
    self.newAccount = Account('Instagram', 'ignionreads', '33176819')

  
  