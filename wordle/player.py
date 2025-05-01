import json
from pathlib import Path

class Player:
    def __init__(self, stats_file='wordle/player_stats.json'):
        self.stats_file = stats_file
        self.stats = self._load_stats()
    
    def _load_stats(self):
        """Load player statistics from file."""
        try:
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                'games_played': 0,
                'games_won': 0,
                'total_guesses': 0,
                'best_guesses': float('inf')
            }
    
    def _save_stats(self):
        """Save player statistics to file."""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f)
    
    def record_game(self, won, num_guesses):
        """Record the results of a game."""
        self.stats['games_played'] += 1
        if won:
            self.stats['games_won'] += 1
            self.stats['total_guesses'] += num_guesses
            if num_guesses < self.stats['best_guesses']:
                self.stats['best_guesses'] = num_guesses
        self._save_stats()
    
    def get_win_percentage(self):
        """Calculate win percentage."""
        if self.stats['games_played'] == 0:
            return 0
        return (self.stats['games_won'] / self.stats['games_played']) * 100
    
    def get_average_guesses(self):
        """Calculate average number of guesses per win."""
        if self.stats['games_won'] == 0:
            return 0
        return self.stats['total_guesses'] / self.stats['games_won']
    
    def get_best_guesses(self):
        """Get the best (lowest) number of guesses to win."""
        return self.stats['best_guesses'] if self.stats['best_guesses'] != float('inf') else 0
    
    def get_stats(self):
        """Get all player statistics."""
        return {
            'games_played': self.stats['games_played'],
            'games_won': self.stats['games_won'],
            'win_percentage': self.get_win_percentage(),
            'average_guesses': self.get_average_guesses(),
            'best_guesses': self.get_best_guesses()
        } 