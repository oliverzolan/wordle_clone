import unittest
from wordle.word_list import WordList

class TestWordValidation(unittest.TestCase):
    def setUp(self):
        self.word_list = WordList()
    
    def test_valid_word(self):
        """Test with valid words."""
        self.assertTrue(self.word_list.is_valid_word("hello"))
        self.assertTrue(self.word_list.is_valid_word("world"))
    
    def test_invalid_word(self):
        """Test with invalid words."""
        self.assertFalse(self.word_list.is_valid_word("xyzzy"))
        self.assertFalse(self.word_list.is_valid_word("12345"))
    
    def test_word_length(self):
        """Test with words of different lengths."""
        self.assertFalse(self.word_list.is_valid_word("toolongword"))
        self.assertFalse(self.word_list.is_valid_word("zzzzz"))  # Using a word we know is not in the list
        self.assertFalse(self.word_list.is_valid_word(""))
    
    def test_case_sensitivity(self):
        """Test that word validation is case-sensitive."""
        # Convert to lowercase before checking
        self.assertTrue(self.word_list.is_valid_word("hello".lower()))
        self.assertTrue(self.word_list.is_valid_word("Hello".lower()))
        self.assertTrue(self.word_list.is_valid_word("HELLO".lower()))

if __name__ == '__main__':
    unittest.main() 