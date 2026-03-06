"""
Tests for math_utils.py functions
Run with: pytest tests/test_math_utils.py -v
"""
import pytest
from math_utils import average_grades, pass_rate, letter_grade

def test_average_grades_empty():
    """
    test case: empty list
    we expect 0.0 because there are no grades to average
    """
    assert average_grades([]) == 0.0

def test_average_grades_single():
    """
    test case: list with only one grade
    the average of one number is the same number
    """

    assert average_grades([85.0]) == 85.0

def test_average_grades_normal():
    """
    test case: normal case with multiple grades
    """
    assert average_grades([85, 92, 78]) == 85.0

#run the same test several times with different inputs
@pytest.mark.parametrize("grades, expected", [
    ([100], 100.0),
    ([0, 100], 50.0),
    ([85.5, 90.5], 88.0),
    ([70, 80, 90], 80.0)
])
def test_average_parametrized(grades, expected):
    """
    Parametrized test = one test function, many test cases.

    Pytest will run this same test several times:
    1) grades = [100], expected = 100.0
    2) grades = [0, 100], expected = 50.0
    3) grades = [85.5, 90.5], expected = 88.0
    4) grades = [70, 80, 90], expected = 80.0
    """
    assert average_grades(grades) == expected

def test_pass_rate_all_pass():
    """
    test case: al grades are passing
    default treshold is 70.0
    grades: 85,90,75
    expected pass rate: 100.0
    """

    assert pass_rate([85,90,75]) == 100.0

def test_pass_rate_some_pass():
    """
    test case: some students pass
    grades: [85, 60, 92]
    2 out of 3 pass (expected approx 66.67%)
    We use abs(... - 66.67) < 0.1 because floating-point results
    are not always stored perfectly exactly in Python.
    """

    result = pass_rate([85, 60, 92])
    assert abs(result - 66.67) < 0.1

def test_pass_rate_custom_threshold():
    """
    test case: custom passing threshold (=90.0)
    """
    result = pass_rate([85, 60, 92], threshold = 90)
    assert abs(result - 33.33) < 0.1

def test_pass_rate_empty():
    """
    test case: empty list
    expected: return 0.0
    """
    assert pass_rate([]) == 0.0

@pytest.mark.parametrize("score, expected", [
    (95, 'A'),
    (90, 'A'),
    (89, 'B'),
    (85, 'B'),
    (80, 'B'),
    (79, 'C'),
    (75, 'C'),
    (70, 'C'),
    (69, 'D'),
    (65, 'D'),
    (60, 'D'),
    (59, 'F'),
    (0, 'F')
])
def test_letter_grade(score, expected):
    """
    Test grade boundaries for letter_grade()
    """

    assert letter_grade(score) == expected

