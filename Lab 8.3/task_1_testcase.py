import unittest
from task_1 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@domain.co.uk"))
        self.assertTrue(is_valid_email("a_b-c.d@sub.domain.com"))
        self.assertTrue(is_valid_email("abc.def@ghi.jkl"))
    
    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user.example.com"))
    
    def test_multiple_at_symbols(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))
    
    def test_missing_dot(self):
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("user@com"))
    
    def test_starts_with_special_character(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email("_user@example.com"))
        self.assertFalse(is_valid_email("-user@example.com"))
    
    def test_ends_with_special_character(self):
        self.assertFalse(is_valid_email("user.@example.com"))
        self.assertFalse(is_valid_email("user@.example.com"))
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("user@example.com@"))
        self.assertFalse(is_valid_email("user@example.com-"))
    
    def test_at_or_dot_at_start_or_end(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email("user@example.com@"))
    
    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))
    
    def test_only_at_and_dot(self):
        self.assertFalse(is_valid_email("@."))
        self.assertFalse(is_valid_email(".@"))
        self.assertFalse(is_valid_email("@"))
        self.assertFalse(is_valid_email("."))

if __name__ == "__main__":
    unittest.main()
