
import csv

def read_csv(file_path):
    data = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def write_csv(data, file_path):
    if not data:
        print("No data to save.")
        return

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())

        writer.writeheader()
        writer.writerows(data)
