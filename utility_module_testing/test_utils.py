import unittest
from datetime import datetime
from utils import sum_numbers, create_user, filter_adults, find_in_list, parse_json, approximate_division


class testUtils(unittest.TestCase):
    def test_eqaulity(self):
        self.assertEqual(sum_numbers(3,7),10)
        user=create_user("Mercy",20)
        self.assertIsNotNone(user)

    def test_truthiness(self):
        self.assertTrue(find_in_list([1,4,3],4))
        # self.assertAlmostEqual(sum_numbers(4,6),5)

    def test_numbers(self):
        self.assertGreater(sum_numbers(2,7),4)
        self.assertAlmostEqual(approximate_division(1,3), 0.3333, places=3)
        # self.assertLess(sum_numbers(3,5),2)

    def test_strings(self):
        self.assertRegex("Hello World", r"World")
        self.assertNotRegex('Hello world', r"Python")

    def test_containment(self):
        users=['Mercy', 'Monica']
        self.assertIn("Mercy",users)
        self.assertNotIn("Macklyn",users)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            parse_json('')
        with self.assertRaises(ValueError):
            parse_json('{"alright": true}')
