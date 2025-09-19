import unittest
from task_5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_standard_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")

    def test_single_digit_month_and_day(self):
        self.assertEqual(convert_date_format("2023-2-5"), "5-2-2023")
        self.assertEqual(convert_date_format("2023-02-05"), "05-02-2023")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_non_string_input(self):
        with self.assertRaises(AttributeError):
            convert_date_format(20231015)
        with self.assertRaises(AttributeError):
            convert_date_format(None)

if __name__ == "__main__":
    unittest.main()
