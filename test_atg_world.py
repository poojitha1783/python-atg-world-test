# test_atg_world.py
import requests
import unittest

class TestAtgWorldWebsite(unittest.TestCase):
    def test_website_access(self):
        response = requests.get("https://atg.world")
        self.assertEqual(response.status_code, 200, "Website did not load successfully")

if __name__ == "__main__":
    unittest.main()
