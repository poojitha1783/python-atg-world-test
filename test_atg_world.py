import unittest
import requests

class TestWebsiteAvailability(unittest.TestCase):
    def test_website_loading(self):
        url = "https://www.atg.world"  # Replace with the correct your Website  URL

        print(f"Attempting to connect to {url}...")

        try:
            response = requests.get(url)
            status_code = response.status_code

            print(f"Status code received: {status_code}")

            # Check if the status code is in the 2xx range (indicating success)
            self.assertTrue(status_code >= 200 and status_code < 300)
            print("Website loaded successfully!")
        except requests.RequestException as e:
            print(f"Failed to connect to the website: {e}")
            self.fail("Website loading failed")

if _name_ == '_main_':
    unittest.main()
