import unittest
from wordle.word_list import WordList
from wordle.game_state import GameState
from wordle.display import Display

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.word_list = WordList()
        self.game_state = GameState()
        self.display = Display()
    
    def test_word_feedback(self):
        """Test word feedback generation."""
        # Test exact match
        feedback = self.display.get_word_feedback("hello", "hello")
        self.assertIn(Display.GREEN, feedback)
        
        # Test partial match
        feedback = self.display.get_word_feedback("hills", "hello")
        self.assertIn(Display.GREEN, feedback)  # 'h' should be green
        self.assertNotIn(Display.YELLOW, feedback)  # No letters should be yellow
        self.assertIn(Display.GREY, feedback)  # 'i', 's' should be grey
        
        # Test no match
        feedback = self.display.get_word_feedback("abcde", "hello")
        self.assertIn(Display.GREY, feedback)
    
    def test_check_valid_guess(self):
        """Test guess validation."""
        # Test valid guess
        self.assertTrue(self.word_list.is_valid_word("hello"))
        
        # Test invalid length
        self.assertFalse(self.word_list.is_valid_word("hell"))
        self.assertFalse(self.word_list.is_valid_word("helloo"))
        
        # Test non-alphabetic
        self.assertFalse(self.word_list.is_valid_word("12345"))
        
        # Test invalid word
        self.assertFalse(self.word_list.is_valid_word("xyzzy"))
    
    def test_select_random_word(self):
        """Test random word selection."""
        word = self.word_list.get_random_word()
        self.assertEqual(len(word), 5)
        self.assertTrue(word.isalpha())
        self.assertTrue(word.islower())

if __name__ == '__main__':
    unittest.main() 