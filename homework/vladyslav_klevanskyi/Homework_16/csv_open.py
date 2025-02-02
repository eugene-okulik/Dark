import csv
import os


def get_csv_data(file_name):
    # Define file path
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(base_path)),
        "eugene_okulik",
        "Lesson_16",
        "hw_data",
        file_name
    )

    # Open csv file
    with open(file_path, newline='') as csv_file:
        csv_data = csv.DictReader(csv_file)
        file_data = []
        for row in csv_data:
            file_data.append(row)

    return file_data
