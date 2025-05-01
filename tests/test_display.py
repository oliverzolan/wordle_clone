import unittest
from wordle.display import Display
from unittest.mock import patch
import io

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display()
    
    def test_get_word_feedback(self):
        """Test word feedback generation."""
        # Test exact match
        feedback = self.display.get_word_feedback("hello", "hello")
        self.assertIn(Display.GREEN, feedback)
        
        # Test partial match
        feedback = self.display.get_word_feedback("hills", "hello")
        self.assertIn(Display.GREEN, feedback)  # 'h' should be green
        self.assertIn(Display.GREY, feedback)   # 'i', 's' should be grey
        
        # Test no match
        feedback = self.display.get_word_feedback("abcde", "hello")
        self.assertIn(Display.GREY, feedback)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_welcome(self, mock_stdout):
        """Test welcome message display."""
        self.display.display_welcome()
        output = mock_stdout.getvalue()
        self.assertIn("Welcome to Wordle", output)
        self.assertIn("Try to guess the 5 letter word", output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_win_message(self, mock_stdout):
        """Test win message display."""
        self.display.display_win_message("hello")
        output = mock_stdout.getvalue()
        self.assertIn("Congratulations", output)
        self.assertIn("hello", output)
        self.assertIn(Display.GREEN, output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_loss_message(self, mock_stdout):
        """Test loss message display."""
        self.display.display_loss_message("hello")
        output = mock_stdout.getvalue()
        self.assertIn("Game Over", output)
        self.assertIn("hello", output)
        self.assertIn(Display.GREEN, output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_error(self, mock_stdout):
        """Test error message display."""
        self.display.display_error("Invalid word")
        output = mock_stdout.getvalue()
        self.assertIn("Error", output)
        self.assertIn("Invalid word", output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats(self, mock_stdout):
        """Test statistics display."""
        stats = {
            'games_played': 10,
            'games_won': 7,
            'win_percentage': 70.0,
            'average_guesses': 4.2,
            'best_guesses': 3
        }
        self.display.display_stats(stats)
        output = mock_stdout.getvalue()
        self.assertIn("Player Statistics", output)
        self.assertIn("Games Played: 10", output)
        self.assertIn("Games Won: 7", output)
        self.assertIn("Win Percentage: 70.0%", output)
        self.assertIn("Average Guesses per Win: 4.2", output)
        self.assertIn("Best Guesses: 3", output)

if __name__ == '__main__':
    unittest.main() 