"""
We define a comboSuite to combine multiple test files into a single test file
to execute.

"""
import unittest
import sys

from tests import test_list_methods
from tests import test_string_methods
from tests import test_motion
from tests import test_list_methods2


def grade():
    suiteList=[]

    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_list_methods.TestListMethods))
    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_string_methods.TestStringMethods))
    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_motion.TestMotion))
    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_list_methods2.TestListMethods2))

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
    from grading.lint_test import lint_test
    passed,style1 = lint_test("src/list_methods.py")
    passed,style2 = lint_test("src/string_methods.py")
    passed,style3 = lint_test("src/motion.py")
    passed,style4 = lint_test("src/list_methods2.py")

    # Convert to percentage points
    style = (style1 + style2 + style3 + style4)*(10./4.0) # total style in percentage
    if style < 0.0:
        style = 0.0

    if score < 50.0:
        print(" Ignore style points until you get at least 50% on correctness!")
        style = 0.0

    grade = 0.40*score  + 0.30*style

    print(" Tests={}  errors={} failures={} skipped={} correctness={} style={} Grade={}/70".format(num_tests, num_errors, num_failures, num_skipped, score, style, grade))
    return grade

if __name__ == "__main__":
    project_grade = grade()
    print(" Final grade = ",project_grade, " of 70  (plus up to 30 for participation)")
