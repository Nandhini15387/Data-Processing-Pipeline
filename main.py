
import logging
from pipeline.reader import read_csv, write_csv
from pipeline.cleaner import clean_data
from pipeline.transformer import transform_data

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Pipeline started")

    data = read_csv("data/input.csv")
    logging.info("CSV file read successfully")

    cleaned_data = clean_data(data)
    logging.info("Data cleaning completed")

    transformed_data = transform_data(cleaned_data)
    logging.info("Data transformation completed")

    write_csv(transformed_data, "output/cleaned_data.csv")
    logging.info("Output file saved successfully")

    print("Pipeline completed successfully!")

except Exception as error:
    logging.error("Pipeline failed: %s", error)
    print("Error:", error)
