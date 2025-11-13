import unittest
from datetime import datetime
from utils import sum_numbers, create_user, filter_adults, find_in_list, parse_json, approximate_division


class TestUtils(unittest.TestCase):
    def test_equality_passing(self):
        self.assertEqual(sum_numbers(3,7),10)
        user={"name":"Mercy", "age":12, "created_at": create_user('Mercy', 12)["created_at"]}
        self.assertDictEqual(create_user("Mercy", 12) | {"created_at": user["created_at"]},user,
        )
        a = 10
        b = a
        self.assertIs(a, b)
        self.assertIsNotNone(user)

    def test_equality_failing(self):
        self.assertEqual(sum_numbers(3,7),12)

    def test_negation_passing(self):
        self.assertNotEqual(sum_numbers(1, 1), 3)
        self.assertIsNot(None, 0)
        self.assertNotIn("z", "apple")

    def test_negation_failing(self):
        self.assertNotEqual(sum_numbers(1, 2), 3)

    def test_truthiness(self):
        self.assertTrue(find_in_list([1,4,3],4))
        self.assertFalse(sum_numbers(4,6),5)
        self.assertIsNone(None)
        self.assertIsNotNone(create_user("Doll", 5))

    def test_numbers(self):
        self.assertGreater(sum_numbers(2,7),4)
        self.assertGreaterEqual(sum_numbers(10, 20),100)
        self.assertAlmostEqual(approximate_division(1,3), 0.3333, places=3)
        self.assertLess(sum_numbers(3,5),2)
        self.assertGreater(sum_numbers(1, 1), 5)

    def test_strings(self):
        self.assertRegex("Good Morning", "Sir")
        self.assertNotRegex('Good Morning', "Madam")
        self.assertRegex("Good Morning", "Sir")

    def test_iterables(self):
        users = ['Mercy', 'Monica']
        self.assertIn("Mercy", users)
        self.assertNotIn("Macklyn",users)
        self.assertIn("Tracy", users)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            parse_json(None)
        with self.assertRaisesRegex(ValueError, "it does not have JSON string provided"):
            parse_json('')
        with self.assertRaises(ValueError):
            parse_json('{"alright": true}')
