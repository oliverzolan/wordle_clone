import unittest
from wordle.game_state import GameState
from unittest.mock import MagicMock

class TestGameState(unittest.TestCase):
    def setUp(self):
        # Create a mock WordList
        self.mock_word_list = MagicMock()
        self.mock_word_list.get_random_word.return_value = "hello"
        self.mock_word_list.is_valid_word.return_value = True
        
        # Create GameState with mock WordList
        self.game_state = GameState(max_attempts=3)
        self.game_state.word_list = self.mock_word_list
        self.game_state.correct_word = "hello"
    
    def test_initial_state(self):
        """Test the initial state of the game."""
        self.assertEqual(self.game_state.max_attempts, 3)
        self.assertEqual(self.game_state.correct_word, "hello")
        self.assertEqual(len(self.game_state.guesses), 0)
        self.assertFalse(self.game_state.game_over)
        self.assertFalse(self.game_state.won)
    
    def test_make_guess_correct(self):
        """Test making a correct guess."""
        result = self.game_state.make_guess("hello")
        self.assertTrue(result)
        self.assertTrue(self.game_state.game_over)
        self.assertTrue(self.game_state.won)
        self.assertEqual(len(self.game_state.guesses), 1)
    
    def test_make_guess_incorrect(self):
        """Test making an incorrect guess."""
        result = self.game_state.make_guess("world")
        self.assertIsNone(result)
        self.assertFalse(self.game_state.game_over)
        self.assertFalse(self.game_state.won)
        self.assertEqual(len(self.game_state.guesses), 1)
    
    def test_max_attempts(self):
        """Test reaching maximum attempts."""
        self.game_state.make_guess("world")
        self.game_state.make_guess("python")
        result = self.game_state.make_guess("tests")
        
        self.assertFalse(result)
        self.assertTrue(self.game_state.game_over)
        self.assertFalse(self.game_state.won)
        self.assertEqual(len(self.game_state.guesses), 3)
    
    def test_get_remaining_attempts(self):
        """Test getting remaining attempts."""
        self.assertEqual(self.game_state.get_remaining_attempts(), 3)
        self.game_state.make_guess("world")
        self.assertEqual(self.game_state.get_remaining_attempts(), 2)
    
    def test_get_guesses(self):
        """Test getting guesses."""
        self.game_state.make_guess("world")
        self.game_state.make_guess("python")
        guesses = self.game_state.get_guesses()
        
        self.assertEqual(len(guesses), 2)
        self.assertEqual(guesses[0], "world")
        self.assertEqual(guesses[1], "python")
        guesses.append("test")
        self.assertEqual(len(self.game_state.guesses), 2)

if __name__ == '__main__':
    unittest.main() 