import wordle_functions 
play_again= True
print("Welcome to Josh's Wordle!")
did_win = false
while play_again:
    computer_guess = wordle_functions.choose_word()
    
    #this is purely for testing REMOVE BEFORE SUBMITION
    print(computer_guess)

    for i in range(7):
        player_guess = wordle_functions.get_guess()
        result = wordle_functions.evaluate_guess(player_guess, computer_guess)
        
        print(f"Round {i}")
        print(wordle_functions.display_guess(result, player_guess))
        if wordle_functions.has_won(result):
                print("Congratulations! You've won!")
                did_win = True
                break
        if not did_win:
            print("Sorry, you didn't guess the word.")
    play_again = input("Would you like to play again? (y/n): ").lower() == "y"
