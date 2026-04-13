from student import Student
from json_manager import save, load
from numpy_analysis import avg, highest
from pandas_analysis import pandas_analysis

students=[]

def add_student():
    print("\nAdd your student!")
    name = input("What is the name?: ").strip().lower().capitalize()
    if not name:
        print("Name cannot be empty!")
        return
    
    try:
        age = int(input("What is the age?: "))
    except Exception:
        print("Age must be a number!")
        return
    
    grades_input = input("Give me the grades separated by space: ").split()
    try:
        grades = [int(g) for g in grades_input]
    except Exception:
        print("Marks must be integers! ")
        return
    
    student = Student(name, age, grades)
    students.append(student)
    print(f"{student.name} Had been added to the dataset!")
    return save(students)

def show_all():
    if not students:
        print("The dataset is empty!")
        return
    
    print(f"\nStudent list is: {len(students)}")

    for num, s in enumerate(students, 1):
        print(f"  {num}. {s.name} | Age: {s.age} | Grades: {s.grades} | Average: {s.get_average()}")

def remove():
    if not students:
        print("The dataset is empty!")
        return
    
    name = input("Enter the name of the student to remove: ").strip().lower().capitalize()

    for s in students:
        if s.name == name:
            students.remove(s)
            print(f"{s.name} has been removed!")
        else:
            print(f"{name} was not found!")
    return save(students)

def find_student():
    name=input("Enter student's name: ")
    for student in students:
        if name==student.name:
             print(f'''
        Name: {student.name},
        Age: {student.age},
        Grades: {student.grades},
        Grades average: {student.get_average()}
        ''')
             
        else:
            print('Такого студента не существует')

def print_menu():
    print("Student Analysis Centre ")
    print("  1. Add Student ")
    print("  2. Show all students ")
    print("  3. Delete a student ")
    print("  4. Save students ")
    print("  5. Load students ")
    print("  6. Numpy analysis ")
    print("  7. Pandas analysis ")
    print("  8. Display the menu ")
    print("  9. Find student ")
    print("  0. Exit ")

def main():
    print_menu()
    loaded = load()
    students.extend(loaded)
    while True:
        choice = input("Choose a point ").strip()
 
        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            remove()
        elif choice == "4":
            save(students)
        elif choice == "5":
            loaded = load()
            students.extend(loaded)
        elif choice == "6":
            avg(students)
            highest(students)
        elif choice == "7":
            pandas_analysis(students)
        elif choice == "8":
            print_menu()
        elif choice == "9":
            find_student()
        elif choice == "0":
            print("\nBye! ")
            break
        else:
            print("The input is wrong! ")
 
 
if __name__ == "__main__":
    main()