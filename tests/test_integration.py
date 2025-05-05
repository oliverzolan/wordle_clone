import unittest
from wordle.word_list import WordList
from wordle.game_state import GameState
from wordle.player import Player
from wordle.display import Display
import os
import json
import tempfile

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        
        # Create a test word list file
        self.test_words = ["hello", "world", "python", "tests"]
        self.test_word_file = os.path.join(self.temp_dir, "test_word_list.json")
        with open(self.test_word_file, 'w') as f:
            json.dump(self.test_words, f)
        
        # Create a test stats file
        self.test_stats_file = os.path.join(self.temp_dir, "test_player_stats.json")
    
    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.test_word_file):
            os.remove(self.test_word_file)
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)
    
    def test_word_list_and_game_state(self):
        """Test integration between WordList and GameState."""
        word_list = WordList(self.test_word_file)
        game_state = GameState(max_attempts=3)
        game_state.word_list = word_list
        game_state.correct_word = word_list.get_random_word()
        
        # Verify the word is from our test list
        self.assertIn(game_state.correct_word, self.test_words)
        
        # Test making a correct guess
        result = game_state.make_guess(game_state.correct_word)
        self.assertTrue(result)
        self.assertTrue(game_state.game_over)
        self.assertTrue(game_state.won)
    
    def test_game_state_and_display(self):
        """Test integration between GameState and Display."""
        word_list = WordList(self.test_word_file)
        game_state = GameState(max_attempts=3)
        game_state.word_list = word_list
        game_state.correct_word = "hello"
        display = Display()
        
        # Test feedback for a guess
        game_state.make_guess("hills")
        feedback = display.get_word_feedback("hills", game_state.correct_word)
        self.assertIn(Display.GREEN, feedback)  # 'h' should be green
        self.assertNotIn(Display.YELLOW, feedback)  # No letters should be yellow
        self.assertIn(Display.GREY, feedback)  # 'i', 's' should be grey
    
    def test_player_and_game_state(self):
        """Test integration between Player and GameState."""
        player = Player(self.test_stats_file)
        game_state = GameState(max_attempts=3)
        game_state.correct_word = "hello"
        
        # Simulate a game
        game_state.make_guess("world")
        game_state.make_guess("hello")
        
        # Record the game
        player.record_game(game_state.won, len(game_state.guesses))
        
        # Verify stats
        stats = player.get_stats()
        self.assertEqual(stats['games_played'], 1)
        self.assertEqual(stats['games_won'], 1)
        self.assertEqual(stats['win_percentage'], 100)
        self.assertEqual(stats['average_guesses'], 2)
        self.assertEqual(stats['best_guesses'], 2)
    
    def test_full_game_flow(self):
        """Test the complete game flow with all components."""
        word_list = WordList(self.test_word_file)
        game_state = GameState(max_attempts=3)
        game_state.word_list = word_list
        game_state.correct_word = "hello"
        player = Player(self.test_stats_file)
        display = Display()
        
        # Simulate a complete game
        guess = "world"
        if word_list.is_valid_word(guess):
            result = game_state.make_guess(guess)
            feedback = display.get_word_feedback(guess, game_state.correct_word)
            game_state.guesses[-1] = feedback
        
        guess = "hello"
        if word_list.is_valid_word(guess):
            result = game_state.make_guess(guess)
            feedback = display.get_word_feedback(guess, game_state.correct_word)
            game_state.guesses[-1] = feedback
        
        # Record the game
        player.record_game(game_state.won, len(game_state.guesses))
        
        # Verify final state
        self.assertTrue(game_state.game_over)
        self.assertTrue(game_state.won)
        self.assertEqual(len(game_state.guesses), 2)
        
        stats = player.get_stats()
        self.assertEqual(stats['games_played'], 1)
        self.assertEqual(stats['games_won'], 1)
    
    def test_error_handling(self):
        """Test error handling across components."""
        word_list = WordList(self.test_word_file)
        game_state = GameState(max_attempts=3)
        game_state.word_list = word_list
        game_state.correct_word = "hello"
        display = Display()
        
        # Test invalid word
        guess = "invalid"
        is_valid = word_list.is_valid_word(guess)
        self.assertFalse(is_valid)
        
        # Test word too long
        guess = "toolongword"
        is_valid = word_list.is_valid_word(guess)
        self.assertFalse(is_valid)
        
        # Test word too short
        guess = "hi"
        is_valid = word_list.is_valid_word(guess)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main() 