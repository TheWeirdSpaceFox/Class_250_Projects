"""
Example file for loading unit tests used by WebCAT
This is not generally distributed to students!

We define a comboSuite to combine multiple test files into a single test file
that WebCAT will execute.

"""
import unittest
import sys

from tests import test_hello_world
from tests import test_say_it
from tests import test_homework

from exam import exam

def grade():
    suiteList=[]

    if exam.section() is not None and exam.exam() is not None:
        suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_hello_world.TestHelloWorld))
        suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_say_it.TestSayIt))
        suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_homework.TestHomework))

    else:
        #print("Invalid section {} or exam {} ! ", exam.section(), exam.exam())
        import test_fail
        suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_fail.TestFail))

    # ----------------   Join them together and run them
    comboSuite = unittest.TestSuite(suiteList)
    result = unittest.TextTestRunner(verbosity=1).run(comboSuite)

    num_errors = len(result.errors)
    num_failures = len(result.failures)
    num_skipped = len(result.skipped)
    num_tests = result.testsRun

    # Correctness score percentage
    score = 100.0*(num_tests - (num_errors+num_failures+num_skipped))/num_tests

    # Style checking
    from tests.lint_test import lint_test
    passed,style1 = lint_test("src/hello_world.py")
    passed,style2 = lint_test("src/say_it.py")
    passed,style3 = lint_test("src/homework.py")

    # Convert to percentage points
    style = (style1 + style2 + style3)*3.33333333 # total style in percents
    if style < 0.0:
        style = 0.0

    grade = 0.75*score  + 0.25*style

    print(" Tests={}  errors={} failures={} skipped={} correctness={} style={} Grade={}".format(num_tests, num_errors, num_failures, num_skipped, score, style, grade))
    return grade

if __name__ == "__main__":
    project_grade = grade()
    print(" Final grade = ",project_grade)
