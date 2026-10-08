"""
We define a comboSuite to combine multiple test files into a single test file
to execute.

"""
import unittest
import sys

from tests import test_calculate
from tests import test_calculate_lists
from tests import test_calculate_file


def grade():
    suiteList=[]

    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_calculate.TestCalculateMethod))
    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_calculate_lists.TestCalculateListsMethod))
    suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_calculate_file.TestCalculateFileMethod))

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
    passed,style1 = lint_test("src/calculate.py")

    # Convert to percentage points
    style = (style1)*(10.0) # total style in percentage
    if style < 0.0:
        style = 0.0

    if score < 50:
        style = 0

    grade = 0.4*score  + 0.2*style

    print(" Tests={}  errors={} failures={} skipped={} correctness={} style={} Grade={}".format(num_tests, num_errors, num_failures, num_skipped, score, style, grade))
    return grade

if __name__ == "__main__":
    project_grade = grade()
    print(" Final grade = ",project_grade, ' of 60 total (+ up to 40 pts participation)')
