
students = dict()
for student in range(4):
    line = input("Name, birth year: ").split(",")
    name = line[0]
    birth_year = line[1]
    students[name] = birth_year


#swap keys and values:
reversed_student = dict();
for student_name, students_birth in students.items():
    reversed_student[students_birth] = student_name


print(f"The original dictionary is {students}")
print(f'The new dictionary is {reversed_student}')
students.copy()


#sorting the dictionary from youngest to oldest student
