import wordle_functions 
play_again= True
print("Welcome to Josh's Wordle!")
did_win = False
previous_guesses = []
while play_again:
    computer_guess = wordle_functions.choose_word()
    
    

    for i in range(6):
        player_guess = wordle_functions.get_guess()

        #Checks for repeated guesses
        
        while player_guess in previous_guesses:
            print("You have already guessed that word.")
            player_guess = wordle_functions.get_guess()
        
        previous_guesses.append(player_guess)
        result = wordle_functions.evaluate_guess(player_guess, computer_guess)

        #Displays the current round and the player's guess with feedback.
        print(f"Round {i + 1}")
        wordle_functions.display_guess(result, player_guess)
        if wordle_functions.has_won(result):
                print("Congratulations! You've won!")
                did_win = True
                break
        if not did_win and i == 5:
            print("Sorry, you didn't guess the word.")
            print(f"The correct word was: {computer_guess}")
    #End of the current game loop
    play_again = input("Would you like to play again? (y/n): ").lower() == "y"
    previous_guesses = []
    did_win = False

print("Thanks for playing Josh's Wordle!")
