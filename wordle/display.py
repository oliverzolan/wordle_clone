class Display:
    GREEN = '\033[92m'  # Green text
    YELLOW = '\033[93m'  # Yellow text
    GREY = '\033[90m'   # Grey text
    RESET = '\033[0m'   # Reset to default color
    
    def __init__(self):
        self.clear_screen()
    
    def clear_screen(self):
        """Clear the terminal screen."""
        print("\033[H\033[J")
    
    def display_welcome(self):
        """Display the welcome message."""
        print("Welcome to Wordle")
        print("Try to guess the 5 letter word\n")
    
    def display_board(self, guesses, current_attempt, max_attempts=6):
        """Display the game board with previous guesses and input prompt."""
        for i in range(max_attempts):
            if i < len(guesses):
                print(f"{guesses[i]}")
            elif i == current_attempt:
                guess = input("□□□□□ > ").lower()
                return guess
            else:
                print("□□□□□")
        print("\n")
    
    def get_word_feedback(self, user_guess, correct_word):
        """Get color-coded feedback for a guess."""
        feedback = []
        used_letters = [False] * len(correct_word)
        
        # First pass: mark exact matches
        for i in range(len(user_guess)):
            if user_guess[i] == correct_word[i]:
                feedback.append(f"{self.GREEN}{user_guess[i]}{self.RESET}")
                used_letters[i] = True
            else:
                feedback.append(user_guess[i])
        
        # Count remaining letters in correct word
        remaining_letters = {}
        for i in range(len(correct_word)):
            if not used_letters[i]:
                letter = correct_word[i]
                remaining_letters[letter] = remaining_letters.get(letter, 0) + 1
        
        # Second pass: mark yellow letters
        for i in range(len(user_guess)):
            if feedback[i] == user_guess[i]:  # Not already marked green
                letter = user_guess[i]
                if letter in remaining_letters and remaining_letters[letter] > 0:
                    feedback[i] = f"{self.YELLOW}{letter}{self.RESET}"
                    remaining_letters[letter] -= 1
                else:
                    feedback[i] = f"{self.GREY}{letter}{self.RESET}"
        
        return ''.join(feedback)
    
    def display_win_message(self, correct_word):
        """Display the win message."""
        print(f"\n🎉 Congratulations! You found the word: {self.GREEN}{correct_word}{self.RESET}")
    
    def display_loss_message(self, correct_word):
        """Display the loss message."""
        print(f"\nGame Over! The word was: {self.GREEN}{correct_word}{self.RESET}")
    
    def display_error(self, message):
        """Display an error message."""
        print(f"\nError: {message}")
    
    def display_stats(self, stats):
        """Display player statistics."""
        print("\nPlayer Statistics:")
        print(f"Games Played: {stats['games_played']}")
        print(f"Games Won: {stats['games_won']}")
        print(f"Win Percentage: {stats['win_percentage']:.1f}%")
        print(f"Average Guesses per Win: {stats['average_guesses']:.1f}")
        print(f"Best Guesses: {stats['best_guesses']}") 