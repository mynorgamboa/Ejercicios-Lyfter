import csv
import ast


def export_students_to_csv(csv_file, information, headers):
    try: 
        with open(csv_file, "w", encoding="UTF-8") as file:
            writer = csv.DictWriter(file,headers)
            writer.writeheader()
            writer.writerows(information)
    except Exception as error: 
        print(f'An unexpected error occurred in create_csv(): {error}')


def students_reader(csv_file):
    students_from_csv = []
    try:
        with open(csv_file, 'r', newline='', encoding='UTF-8') as file:
            reader = csv.DictReader(file)
            for index in reader:
                student = {
                    "name": index["name"],
                    "group": index["group"],
                    "grades": ast.literal_eval(index["grades"]),
                    "average": float(index["average"])
                }
                students_from_csv.append(student)
            if students_from_csv:
                print("The list was imported successfully!")
                return students_from_csv
            else:
                print("The students have not been exported since the list is empty!")

    except Exception as error:
        print(f'An unexpected error occurred in students_reader(): {error}')