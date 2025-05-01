from .word_list import WordList

class GameState:
    def __init__(self, max_attempts=6):
        self.word_list = WordList()
        self.correct_word = self.word_list.get_random_word()
        self.max_attempts = max_attempts
        self.guesses = []
        self.game_over = False
        self.won = False
    
    def make_guess(self, guess):
        """Process a guess and update game state."""
        if self.game_over:
            return None
        
        self.guesses.append(guess)
        
        if guess == self.correct_word:
            self.game_over = True
            self.won = True
            return True
        
        if len(self.guesses) >= self.max_attempts:
            self.game_over = True
            return False
        
        return None
    
    def get_remaining_attempts(self):
        """Get the number of remaining attempts."""
        return self.max_attempts - len(self.guesses)
    
    def is_game_over(self):
        """Check if the game is over."""
        return self.game_over
    
    def has_won(self):
        """Check if the player has won."""
        return self.won
    
    def get_correct_word(self):
        """Get the correct word."""
        return self.correct_word
    
    def get_guesses(self):
        """Get all guesses made so far."""
        return self.guesses.copy() 