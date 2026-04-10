class Student:
    def __init__(self, name, age, grades:list):
        self.name = name
        self.age = age
        self.grades = grades
    
    def get_average(self):
        avg = sum(self.grades)/len(self.grades)
        return avg
    
    def to_dict(self):
        return {
            "name":self.name,
            "age":self.age,
            "grades":self.grades
        }

