"""
BUGGY PROGRAM - Contains errors for debugging practice!
This program tries to calculate the average grade from a CSV file.
"""

import csv


def calculate_average(filename):
    rows = []

    # BUG 1: Using csv.reader instead of DictReader
    # This means rows will be lists, not dictionaries
    with open(filename, 'r') as f:
        reader = csv.DictReader(f) # changed csv.reader(f) to csv.DictReader(f)
        rows = list(reader)

    total = 0
    count = 0

    for row in rows:
        print(row)
        # BUG 2: Accessing wrong indexes
        # If CSV has columns: name, course, grade
        # valid indexes are 0, 1, 2
        # but here we try to access row[3] (doesn't exist)
        name = row['name'] #changed indexes to keys, since now csv.DictReader read it as a dictionary
        course = row['course']
        grade_str = row['grade']   # ❌ IndexError will happen here/ FIXED

        grade = float(grade_str)

        total += grade
        count += 1

        print(f"{name} ({course}): {grade}")

    # add protection against division by zero:
    if count == 0:
        print("No students found!")
        return 0.0

    avg = total / count


    print(f"\nAverage: {avg:.2f}")

    return avg


if __name__ == "__main__":
    calculate_average('data/students.csv')