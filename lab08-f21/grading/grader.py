"""
No unit tests - only style grading
"""
import unittest
from os import listdir
from os.path import isfile, join

from grading.lint_test import lint_test


def grade():

    only_files = [f for f in listdir('src') if isfile(join('src', f))]

    total_possible = 0
    total_points = 0
    for file_name in only_files:
        if file_name == '__init__.py':
            continue

        total_possible += 10

        passed, style = lint_test(join('src', file_name))

        if style < 0.0:
            style = 0.0

        print(f"  grading {file_name} with {style} of 10 ")
        total_points += style


    grade = 100.0*total_points / total_possible
    return grade

if __name__ == "__main__":
    style_grade = grade()
    print(f" Final style percent = {style_grade}%")
