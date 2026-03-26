from actions import add_new_student, show_students, top_3_students, global_average
from data import export_students_to_csv, students_reader

def menu():
    option = 0
    total_list = []
    csv_file = "semana 11/students_list.csv"
    while(option != 7):
        try:
            option = int(input('''Hi, welcome to the Student Control System, What do you want to do?
            1- Add a new student
            2- See the students list
            3- See top 3 students
            4- See global average
            5- Export to a CSV document
            6- Import a CSV document to continue
            7- Exit
            '''))
        except ValueError as error:
            print(f'Please enter a valid number!')
        except Exception as error:
            print(f'an unexpected error occurred in menu(): {error}')
        if (option == 1):
            students_list = add_new_student(total_list)
            total_list = students_list
            #print(total_list)
        elif (option == 2):
            show_students(total_list)
        elif (option == 3):
            top_3_students(total_list)
        elif (option == 4):
            global_average(total_list)
        elif (option == 5):
            if total_list:
                headers = ("name", "group", "grades", "average")
                export_students_to_csv(csv_file, total_list, headers)
                print('The list was exported successfully!')
            else:
                print("The list of students is empty!")
        elif (option == 6):
            csv_list = students_reader(csv_file)
            #print (csv_list)
            if csv_list:
                total_list = total_list + csv_list
        elif (option < 1 or option > 7):
            print('Select only the options in the list!!')
    print('Have a nice day!')    
    