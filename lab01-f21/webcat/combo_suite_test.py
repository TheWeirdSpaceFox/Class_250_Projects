import unittest
import sys

from tests import test_hello_world

from tests import test_say_it

suiteList=[]
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_hello_world.TestHelloWorld))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_say_it.TestSayIt))

# ----------------   Join them together and run them
comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=0).run(comboSuite)
