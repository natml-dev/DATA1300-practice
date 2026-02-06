"""
CSV Student Grade Manager
Professional file I/O with error handling and type hints
"""

import csv
import json
import os
from typing import List, Dict


def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    Read CSV file and return list of dictionaries.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found")

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def update_csv_student(filename: str, name: str, new_grade: int) -> None:
    """
    Update a student's grade in CSV file.
    """
    rows = read_csv(filename)
    updated = False

    for row in rows:
        if row["name"] == name:
            row["grade"] = str(new_grade)
            updated = True

    if not updated:
        print(f"Student '{name}' not found")
        return

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "course", "grade"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated {name} to grade {new_grade}")


def read_json(filename: str) -> List[Dict]:
    """
    Read JSON file and return list of dictionaries.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found")

    with open(filename, "r") as f:
        return json.load(f)


def update_json_student(filename: str, name: str, new_grade: int) -> None:
    """
    Update a student's grade in JSON file.
    """
    data = read_json(filename)
    updated = False

    for student in data:
        if student["name"] == name:
            student["grade"] = new_grade
            updated = True

    if not updated:
        print(f"Student '{name}' not found")
        return

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Updated {name} to grade {new_grade}")



     
