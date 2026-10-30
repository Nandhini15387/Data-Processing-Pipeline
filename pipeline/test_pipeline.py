
import unittest
from pipeline.reader import read_csv
from pipeline.cleaner import clean_data
from pipeline.transformer import transform_data


class TestPipeline(unittest.TestCase):

    def test_read_csv(self):
        data = read_csv("data/input.csv")
        self.assertEqual(len(data), 5)

    def test_clean_data(self):
        data = read_csv("data/input.csv")
        cleaned = clean_data(data)

        self.assertEqual(cleaned[1]["age"], "0")
        self.assertEqual(cleaned[2]["city"], "Unknown")
        self.assertEqual(cleaned[3]["salary"], "0")

    def test_transform_data(self):
        data = read_csv("data/input.csv")
        cleaned = clean_data(data)
        transformed = transform_data(cleaned)

        self.assertIsInstance(transformed[0]["age"], int)
        self.assertIsInstance(transformed[0]["salary"], float)


if __name__ == "__main__":
    unittest.main()
