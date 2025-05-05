from .word_list import WordList
from .game_state import GameState
from .player import Player
from .display import Display

def main():
    # Initialize game components
    word_list = WordList()
    game_state = GameState()
    player = Player()
    display = Display()
    
    # Display welcome message
    display.display_welcome()
    
    # Main game loop
    while not game_state.is_game_over():
        # Get player's guess
        guess = display.display_board(
            game_state.get_guesses(),
            len(game_state.get_guesses())
        )
        
        # Validate guess
        if not word_list.is_valid_word(guess):
            display.display_error("Invalid word. Please try again.")
            continue
    
        # Process guess
        result = game_state.make_guess(guess)
        
        # Get feedback for the guess
        feedback = display.get_word_feedback(guess, game_state.get_correct_word())
        game_state.guesses[-1] = feedback  # Replace the guess with its feedback
        
        # Check game result
        if result is True:
            display.display_win_message(game_state.get_correct_word())
            player.record_game(True, len(game_state.get_guesses()))
            break
        elif result is False:
            display.display_loss_message(game_state.get_correct_word())
            player.record_game(False, len(game_state.get_guesses()))
            break
    
    # Display player statistics
    display.display_stats(player.get_stats())

if __name__ == "__main__":
    main()