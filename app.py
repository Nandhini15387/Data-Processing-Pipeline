
from flask import Flask, jsonify, send_from_directory
from pipeline.reader import read_csv, write_csv
from pipeline.cleaner import clean_data
from pipeline.transformer import transform_data
import os
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/data")
def get_data():
    try:
        data = read_csv("data/input.csv")

        missing_fixed = sum(
            1
            for row in data
            for value in row.values()
            if value is None or value.strip() == ""
        )

        cleaned = clean_data(data)
        transformed = transform_data(cleaned)

        write_csv(transformed, "output/cleaned_data.csv")

        return jsonify({
            "success": True,
            "total_records": len(transformed),
            "missing_fixed": missing_fixed,
            "employees": transformed
        })

    except Exception as error:
        logging.exception("Pipeline failed")
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


@app.route("/api/health")
def health():
    return jsonify({"status": "running"})




if __name__ == "__main__":
    import webbrowser
    import threading

    os.makedirs("logs", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    print("Starting DataFlow Dashboard...")
    print("Open this address in Chrome:")
    print("http://127.0.0.1:5000")

    threading.Timer(
        2,
        lambda: webbrowser.open("http://127.0.0.1:5000")
    ).start()

    app.run(debug=True, use_reloader=False)

