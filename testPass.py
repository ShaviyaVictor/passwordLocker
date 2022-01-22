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
    self.newAccount = Account('Instagram', 'ignitionreads', '33176819')


  def tearDown(self) :
    '''
    tearDown() method cleans up the saved instances after each test case has run
    '''
    Account.accountList = []



  def testInstance(self) :
    '''
    Create testInstance() TestCase to test if the object is initialized properly/ instantiated correctly
    '''

    self.assertEqual(self.newAccount.account, 'Instagram')
    self.assertEqual(self.newAccount.username, 'ignitionreads')
    self.assertEqual(self.newAccount.password, '33176819')



  def testSaveAccount(self) :
    '''
    TestCase to test if the account object is saved into the accountList[]

    Saving the new account
    '''
    self.newAccount.saveAccount()

    self.assertEqual(len(Account.accountList), 1)
  


  def testSaveAccounts(self) :
    '''
    TestCase to check if we can save multiple accounts to our accountList[]

    Will bring an assertion error since everytime we run a test, we create instances of account and saving them and all are being counted hence we get 3 != 2 coz the first instance has been counted twice

    The already saved accounts are thus cleaned up after calling the tearDown() method right after the setUp() method
    '''
    self.newAccount.saveAccount()

    # Creating another account to see if it will be saved
    testAccount = Account('Twitter', 'ShaviyaVictor', '29834070')

    testAccount.saveAccount()

    self.assertEqual(len(Account.accountList), 2)



  def testDeleteAccount(self) :
    '''
    This method will test if we can remove an account from our accountList
    '''
      
    # Creating the accounts afresh to enable the delete() to work now that the tearDown() method clears things up

    self.newAccount.saveAccount()
    testAccount = Account('Twitter', 'ShaviyaVictor', '29834070')

    testAccount.saveAccount()

    # Deleting an account
    self.newAccount.deleteAccount()

    self.assertEqual(len(Account.accountList), 1)



  def testFindAccountByAcc(self) :
    '''
    TestCase to check if we can find an account by account name and display the information
    '''

    self.newAccount.saveAccount()
    testAccount = Account('Twitter', 'ShaviyaVictor', '29834070')

    foundAccount = Account.findByAccount('Twitter')

    self.assertEqual(foundAccount.username, testAccount.username)




if __name__ == '__main__' :
    unittest.main()
    '''
    Confirming that anything inside the if block should run only if this is the file that is currently being run

    Then provide a CLI that collects all the test methods and executes them using the unittest.main()
    '''  
  