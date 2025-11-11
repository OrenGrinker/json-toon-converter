import unittest
from json_to_toon_converter.converter import json_to_toon, toon_to_json


class TestJsonToToonConverter(unittest.TestCase):

    def test_json_to_toon(self):
        json_data = {
            "name": "Alice",
            "age": 25,
            "city": "Wonderland"
        }
        toon_result = json_to_toon(json_data)
        self.assertIsInstance(toon_result, str)
        self.assertIn("name", toon_result)

    def test_toon_to_json(self):
        toon_data = '(name "Alice") (age 25) (city "Wonderland")'
        json_result = toon_to_json(toon_data)
        self.assertIsInstance(json_result, dict)
        self.assertEqual(json_result['name'], 'Alice')
        self.assertEqual(json_result['age'], 25)
        self.assertEqual(json_result['city'], 'Wonderland')


if __name__ == "__main__":
    unittest.main()
