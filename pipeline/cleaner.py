
def clean_data(data):
    cleaned_data = []

    for row in data:
        for key, value in row.items():
            if value is None or value.strip() == "":
                if key == "age":
                    row[key] = "0"
                elif key == "salary":
                    row[key] = "0"
                else:
                    row[key] = "Unknown"

        cleaned_data.append(row)

    return cleaned_data
