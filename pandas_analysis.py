import pandas as pd

def pandas_analysis(students:list):
    data = []
    for student in students:
        data.append({
            "Name": student.name,
            "Age": student.age,
            "Grades": student.grades,
            "Average": student.get_average()
        })
    
    df_students = pd.DataFrame(data)
    print (f"The table is :\n{df_students}")

    df_students_sorted = pd.DataFrame(data).sort_values(by= "Average", ascending= False)
    print(f"The sorted table by average is :\n {df_students_sorted}")
