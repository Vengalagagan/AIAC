import unittest
import string

def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        c.lower() for c in sentence if c.isalnum()
    )
    return cleaned == cleaned[::-1]

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_sentence_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_sentence_palindrome("Madam In Eden, I’m Adam"))
        self.assertTrue(is_sentence_palindrome("Able was I, I saw Elba"))
        self.assertTrue(is_sentence_palindrome("Step on no pets"))
        self.assertTrue(is_sentence_palindrome("Never odd or even"))
        self.assertTrue(is_sentence_palindrome("Red roses run no risk, sir, on Nurse's order"))
        self.assertTrue(is_sentence_palindrome("Go hang a salami, I'm a lasagna hog"))

    def test_non_palindromes(self):
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
        self.assertFalse(is_sentence_palindrome("Hello, world!"))
        self.assertFalse(is_sentence_palindrome("Python programming"))
        self.assertFalse(is_sentence_palindrome("Palindrome test case"))
        self.assertFalse(is_sentence_palindrome("OpenAI is awesome"))

    def test_edge_cases(self):
        self.assertTrue(is_sentence_palindrome(""))  # Empty string
        self.assertTrue(is_sentence_palindrome("!@#$%^&*()"))  # Only punctuation
        self.assertTrue(is_sentence_palindrome("A"))  # Single character
        self.assertTrue(is_sentence_palindrome("   "))  # Only spaces
        self.assertTrue(is_sentence_palindrome(".,;:"))  # Only punctuation

    def test_mixed_cases_and_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Murder for a jar of red rum"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("Sir, I demand, I am a maid named Iris."))
        self.assertTrue(is_sentence_palindrome("Yo, Banana Boy!"))
        self.assertTrue(is_sentence_palindrome("Borrow or rob?"))

    def test_numeric_palindromes(self):
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertTrue(is_sentence_palindrome("1 2 3 2 1"))
        self.assertTrue(is_sentence_palindrome("12,321"))
        self.assertFalse(is_sentence_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()
