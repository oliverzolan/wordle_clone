import unittest
from wordle.player import Player
import os
import json

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_stats_file = "test_player_stats.json"
        self.player = Player(self.test_stats_file)
    
    def tearDown(self):
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
    
    def test_initial_stats(self):
        """Test initial statistics."""
        stats = self.player.get_stats()
        self.assertEqual(stats['games_played'], 0)
        self.assertEqual(stats['games_won'], 0)
        self.assertEqual(stats['win_percentage'], 0)
        self.assertEqual(stats['average_guesses'], 0)
        self.assertEqual(stats['best_guesses'], 0)
    
    def test_record_win(self):
        """Test recording a win."""
        self.player.record_game(True, 3)
        stats = self.player.get_stats()
        self.assertEqual(stats['games_played'], 1)
        self.assertEqual(stats['games_won'], 1)
        self.assertEqual(stats['win_percentage'], 100)
        self.assertEqual(stats['average_guesses'], 3)
        self.assertEqual(stats['best_guesses'], 3)
    
    def test_record_loss(self):
        """Test recording a loss."""
        self.player.record_game(False, 6)
        stats = self.player.get_stats()
        self.assertEqual(stats['games_played'], 1)
        self.assertEqual(stats['games_won'], 0)
        self.assertEqual(stats['win_percentage'], 0)
        self.assertEqual(stats['average_guesses'], 0)
        self.assertEqual(stats['best_guesses'], 0)
    
    def test_multiple_games(self):
        """Test recording multiple games."""
        # Win in 3 guesses
        self.player.record_game(True, 3)
        # Win in 5 guesses
        self.player.record_game(True, 5)
        # Loss
        self.player.record_game(False, 6)
        
        stats = self.player.get_stats()
        self.assertEqual(stats['games_played'], 3)
        self.assertEqual(stats['games_won'], 2)
        self.assertAlmostEqual(stats['win_percentage'], 66.67, places=2)
        self.assertEqual(stats['average_guesses'], 4)
        self.assertEqual(stats['best_guesses'], 3)
    
    def test_stats_persistence(self):
        """Test that stats are saved and loaded correctly."""
        # Record some games
        self.player.record_game(True, 3)
        self.player.record_game(True, 5)
        
        # Create a new player instance with the same stats file
        new_player = Player(self.test_stats_file)
        stats = new_player.get_stats()
        
        self.assertEqual(stats['games_played'], 2)
        self.assertEqual(stats['games_won'], 2)
        self.assertEqual(stats['win_percentage'], 100)
        self.assertEqual(stats['average_guesses'], 4)
        self.assertEqual(stats['best_guesses'], 3)

if __name__ == '__main__':
    unittest.main() 