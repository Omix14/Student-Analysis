import json
from student import Student
path = "students.json"

def save(students):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def load():
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Student(d["name"], d["age"], d["grades"]) for d in data]
