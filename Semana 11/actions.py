import csv
import ast


class Students:
    def __init__(self, name, group, spa, eng, soc, sci, ave):
        self.name = name
        self.group = group
        self.spanish_grade = spa
        self.english_grade = eng
        self.socials_grade = soc
        self.science_grade = sci
        self.average = ave

    def convert_to_dict(self):
        return {
            "name": self.name,
            "group": self.group,
            "grades": str({
                "Spanish": self.spanish_grade,
                "English": self.english_grade,
                "Socials": self.socials_grade,
                "Science": self.science_grade
            }),
            "average": self.average
        }


def add_new_student(total_list):
    students = total_list
    again="yes"
    try:
        while(again != 'no'):
            full_name = input('Full name: ')
            the_group = input('Group: (Ex: 11B)')

            while True:
                spanish = int(input('What is the Spanish grade: '))
                if (0 <= spanish <= 100):
                    break
                else:    
                    print("Grade must be between 0 and 100!")


            while True:
                english = int(input('What is the English grade: '))
                if (0 <= english <= 100):
                    break
                else:    
                    print("Grade must be between 0 and 100!")

            while True:
                socials = int(input('What is the Socials grade: '))
                if (0 <= socials <= 100):
                    break
                else:    
                    print("Grade must be between 0 and 100!")
            
            while True:
                science = int(input('What is the Science grade: '))
                if (0 <= science <= 100):
                    break
                else:    
                    print("Grade must be between 0 and 100!")

            average = (spanish+english+socials+science) / 4

            new_student = Students(full_name,the_group, spanish, english, socials, science, average)
            students.append(new_student)

            while True:
                again = input("Do you want to add another one? (yes/no): ")
                again.lower()
                if again in ("yes", "no"):
                    break
                else:
                    print("Please select a valid response!")

        print("The student(s) where added successfully!")
        return students
    
    except Exception as error:
        print(f'an unexpected error occurred in add_new_student(): {error}')

def show_students(students_list):
    try:
        for student in students_list:
            print(f'''
                Name: {student.name}
                Group: {student.group}
                Grades: SPA: {student.spanish_grade}, ENG: {student.english_grade}, SOC: {student.socials_grade}, SCI: {student.science_grade}
                Average: {student.average}
                ''')
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
            if (student.average > first):
                third = second
                student_3_name = student_2_name
                student_3_average = student_2_average
                second = first
                student_2_name = student_1_name
                student_2_average = student_1_average
                first = student.average
                student_1_name = student.name
                student_1_average = student.average
            elif (first >= student.average and student.average >= second):
                third = second
                student_3_name = student_2_name
                student_3_average = student_2_average
                second = student.average
                student_2_name = student.name
                student_2_average = student.average
            elif (second >= student.average and student.average >= third):
                third = student.average
                student_3_name = student.name
                student_3_average = student.average
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
                total_average += student.average
            total_average = total_average / len(students_list)    
            print(f'The global average is {total_average}')
        else:
            print("The list of students is empty!")
        
    except Exception as error:
        print(f'An unexpected error occurred in global_average(): {error}')