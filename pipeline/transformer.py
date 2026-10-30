
def transform_data(data):
    transformed_data = []

    for row in data:
        row["age"] = int(row["age"])
        row["salary"] = float(row["salary"])

        transformed_data.append(row)

    return transformed_data
