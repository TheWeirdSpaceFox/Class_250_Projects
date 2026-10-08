"""
We define a comboSuite to combine multiple test files into a single test file
to execute.

"""
import unittest
import sys


def grade():
    suiteList=[]

    # No unit tests this week

    # Style checking
    from grading.lint_test import lint_test
    passed,style1 = lint_test("src/server_log.py")

    # Convert to percentage points
    style = (style1)*(2.0) # total style points (of 20 max)
    if style < 0.0:
        style = 0.0

    return style

if __name__ == "__main__":
    project_grade = grade()
    print(" Final style grade = ", project_grade, ' of 20 total (+ up to 40 pts participation)')
