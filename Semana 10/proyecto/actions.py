import csv
import ast

def add_new_student(total_list):
    students = total_list
    again="yes"
    try:
        while(again != 'no'):
            each_student = {}
            full_name = input('Full name: ')
            each_student['name'] = full_name
            group = input('Group: (Ex: 11B)')
            each_student['group'] = group

            subjects = ["Spanish", "English", "Socials", "Science"]
            grades = {}

            for subject in subjects: 
                while True:
                    try:
                        grade = int(input(f"{subject} grade: "))
                        grades[subject] = grade
                        if (0 <= grade <= 100):
                            break
                        else:
                            print("Grade must be between 0 and 100!")
                    except ValueError:
                        print("Please use just numbers!")
            
            each_student['grades'] = grades

            average = sum(grades.values()) / len(grades)
            each_student['average'] = average
            students.append(each_student)

            while True:
                again = input("Do you want to add another one? (yes/no): ")
                again.lower()
                if again in ("yes", "no"):
                    break
                print("Please select a valid response!")
        print("The student(s) where added successfully!")
        return students
    
    except Exception as error:
        print(f'an unexpected error occurred in add_new_student(): {error}')

def show_students(students_list):
    try:
        for student in students_list:
            for key,value in student.items():
                if (key == 'grades'):
                    for grades,number in value.items():
                        print(f'{grades}: {number}')
                else:
                    print(f'{key}: {value}')
        if not students_list:
            print("The list of students is empty!")
    except Exception as error:
        print(f'An unexpected error occurred in show_students(): {error}')


def top_3_students(students_list):
    first = 0
    student_1_name=""
    student_1_average = 0
    second = 0
    student_2_name=""
    student_2_average = 0
    third = 0
    student_3_name=""
    student_3_average = 0
    try:
        for student in students_list:
            for key,value in student.items():
                if (key == 'average'):
                    if (value > first):
                        third = second
                        student_3_name = student_2_name
                        student_3_average = student_2_average
                        second = first
                        student_2_name = student_1_name
                        student_2_average = student_1_average
                        first = value
                        student_1_name = student["name"]
                        student_1_average = student["average"]
                    elif (first > value and value > second):
                        third = second
                        student_3_name = student_2_name
                        student_3_average = student_2_average
                        second = value
                        student_2_name = student["name"]
                        student_2_average = student["average"]
                    elif (second > value and value > third):
                        third = value
                        student_3_name = student["name"]
                        student_3_average = student["average"]
        if students_list:
            print(f'''This is the top 3 students:
                    1: Name: {student_1_name}, Average: {student_1_average}
                    2: Name: {student_2_name}, Average: {student_2_average}
                    3: Name: {student_3_name}, Average: {student_3_average}
                    ''')
        else:
            print("The list of students is empty!")
    except Exception as error:
        print(f'An unexpected error occurred in top_3_students(): {error}')

def global_average(students_list):
    total_average = 0
    try:
        if students_list:
            for student in students_list:
                for key, value in student.items():
                    if(key == "average"):
                        total_average += value
            total_average = total_average / len(students_list)    
            print(f'The global average is {total_average}')
        else:
            print("The list of students is empty!")
        
    except Exception as error:
        print(f'An unexpected error occurred in global_average(): {error}')