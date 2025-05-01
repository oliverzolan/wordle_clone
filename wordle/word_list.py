import json
import random
from pathlib import Path

class WordList:
    def __init__(self, word_list_path='wordle/wordle-list'):
        self.word_list_path = word_list_path
        self.words = self._load_words()
    
    def _load_words(self):
        """Load words from the word list file."""
        try:
            with open(self.word_list_path, 'r') as wordle_library:
                return json.load(wordle_library)
        except (FileNotFoundError, PermissionError):
            return ["hello"]  # Default word if file not found
    
    def is_valid_word(self, word):
        """Check if a word is valid (exists in the list and is 5 letters)."""
        return word in self.words and len(word) == 5
    
    def get_random_word(self):
        """Get a random word from the word list."""
        return random.choice(self.words)
    
    def get_word_count(self):
        """Get the total number of words in the list."""
        return len(self.words)
    
    def reload_words(self):
        """Reload the word list from file."""
        self.words = self._load_words() 