import csv
import ast
from actions import Students


def export_students_to_csv(csv_file, information, headers):
    try: 
        with open(csv_file, "w", encoding="UTF-8") as file:
            writer = csv.DictWriter(file,headers)
            writer.writeheader()
            
            data = [student.convert_to_dict() for student in information]
            writer.writerows(data)

    except Exception as error: 
        print(f'An unexpected error occurred in create_csv(): {error}')


def students_reader(csv_file):
    students_from_csv = []
    try:
        with open(csv_file, 'r', newline='', encoding='UTF-8') as file:
            reader = csv.DictReader(file)
            for index in reader:
                all_grades = ast.literal_eval(index["grades"])

                new_student = Students(index["name"],index["group"],all_grades["Spanish"], 
                all_grades["English"], all_grades["Socials"], all_grades["Science"], 
                float(index["average"]))

                students_from_csv.append(new_student)
            if students_from_csv:
                print("The list was imported successfully!")
                return students_from_csv
            else:
                print("The students have not been exported since the list is empty!")

    except Exception as error:
        print(f'An unexpected error occurred in students_reader(): {error}')