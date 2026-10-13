import random




def choose_word():
    #Selects and returns a secret word.
    wordle_words = [
    "apple", "crane", "slate", "trace", "pride",
    "shine", "globe", "brick", "plant", "storm",
    "light", "frame", "bread", "mouse", "chair",
    "dream", "cloud", "river", "stone", "flame",
    "grape", "smile", "beach", "crown", "heart",
    "lemon", "tiger", "zebra", "candy", "maple",
    "frost", "quiet", "vivid", "ocean", "dance"
    ]
    return random.choice(wordle_words)


def get_guess():
#Gets and validates the player’s guess.
    guess = input("Please enter your guess: ")
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        return get_guess()
    
    return guess

def evaluate_guess(player_guess, computer_guess): 
# Compares the guess with the secret word and returns feedback.
    player_guess_list = list(player_guess)
    computer_guess_list = list(computer_guess)
    result = ["-", "-", "-", "-", "-"]
    for i in range(5):
        if player_guess_list[i] == computer_guess_list[i]:
            result[i] = "G"
        elif player_guess_list[i] in computer_guess_list:
            result[i] = "Y"
        else:
            result[i] = "-"

    return result

    
def display_guess(result, player_guess): 
#Displays the guess and its feedback.
    print(f"Your guess: {player_guess}")
    print(f"Feedback: {result}")

def has_won(result):
#Determines whether the player has guessed the word.
    if result == ["G", "G", "G", "G", "G"]:
        return True
    return False