# tests/test_app.py
import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b"Hello, Jenkins CI/CD!")

if __name__ == "__main__":
    unittest.main()
