"""
Tests for CSV/JSON file operations
"""

from csv_handler import read_csv, read_json, update_csv_student


def test_csv_read():
    students = read_csv('data/students.csv')
    assert len(students) >= 3
    assert students[0]['name'] in ['Alice', 'Bob', 'Charlie']


def test_csv_update():
    update_csv_student('data/students.csv', 'Charlie', 82)
    students = read_csv('data/students.csv')
    charlie = next(s for s in students if s['name'] == 'Charlie')
    assert int(charlie['grade']) == 82


def test_json_read():
    students = read_json('data/students.json')
    assert len(students) >= 3
    assert isinstance(students[0]['grade'], int)