import unittest
from wordle.word_list import WordList
import os
import json

class TestWordList(unittest.TestCase):
    def setUp(self):
        # Create a temporary word list file
        self.test_words = ["hello", "world", "python", "tests"]
        self.test_file = "test_word_list.json"
        with open(self.test_file, 'w') as f:
            json.dump(self.test_words, f)
        self.word_list = WordList(self.test_file)
    
    def tearDown(self):
        # Clean up the temporary file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_load_words(self):
        """Test that words are loaded correctly from the file."""
        self.assertEqual(len(self.word_list.words), 4)
        self.assertIn("hello", self.word_list.words)
        self.assertIn("world", self.word_list.words)
    
    def test_is_valid_word(self):
        """Test word validation."""
        self.assertTrue(self.word_list.is_valid_word("hello"))
        self.assertTrue(self.word_list.is_valid_word("world"))
        self.assertFalse(self.word_list.is_valid_word("invalid"))
        self.assertFalse(self.word_list.is_valid_word("toolongword"))
        self.assertFalse(self.word_list.is_valid_word("hi"))
    
    def test_get_random_word(self):
        """Test getting a random word."""
        word = self.word_list.get_random_word()
        self.assertIn(word, self.test_words)
    
    def test_get_word_count(self):
        """Test getting the word count."""
        self.assertEqual(self.word_list.get_word_count(), 4)
    
    def test_reload_words(self):
        """Test reloading words from file."""
        # Add a new word to the file
        self.test_words.append("new")
        with open(self.test_file, 'w') as f:
            json.dump(self.test_words, f)
        
        # Reload and verify
        self.word_list.reload_words()
        self.assertEqual(self.word_list.get_word_count(), 5)
        self.assertIn("new", self.word_list.words)

if __name__ == '__main__':
    unittest.main() 