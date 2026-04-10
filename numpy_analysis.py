import numpy as np

def avg(students:list):
    for student in students:
        grades_array = np.array(student.grades)
        print(f"{student.name}: {np.average(grades_array)}")

def highest(students:list):
    for student in students:
        grades_array = np.array(student.grades)
        print(f"{student.name}: {np.max(grades_array)}")