from art import logo
import random
# Include an ASCII art logo.
print(logo)
lives_remaining = 10

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def set_difficulty():
    global lives_remaining
    game_difficulty = input(f"Select a game difficulty: 'easy' or 'hard' ")
    if game_difficulty == "easy":
        lives_remaining = 10
        return lives_remaining
    else:
        lives_remaining = 5
        return lives_remaining

def play_game(): 
    global lives_remaining
    num_to_guess = random.randint(0, 101)
    #print(f"Your number to guess is {num_to_guess}")   Was used during testing
    is_game_over = False

    while not is_game_over:
        # Allow the player to submit a guess for a number between 1 and 100.
        user_guess = int(input("Guess a number between 0 and 100. "))
        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
        if user_guess == num_to_guess:
            is_game_over = True
            # If they got the answer correct, show the actual answer to the player.
            print(f"Your guess was {user_guess}, the correct answer was {num_to_guess}. You Win")
        elif user_guess > num_to_guess:
            lives_remaining -= 1
            print(f"Your guess was {user_guess}, that number was too high. You have {lives_remaining} guesses remaining.")        
        else:
            lives_remaining -= 1
            print(f"Your guess was {user_guess}, that number was too low. You have {lives_remaining} guesses remaining.")
    # Track the number of turns remaining.
    # If they run out of turns, provide feedback to the player.
        if lives_remaining == 0:
            is_game_over = True
            print(f"You have {lives_remaining} guesses remiaing, your guess was {user_guess} the correct answer was {num_to_guess}.")

while input(f"Would you like to play again? 'y' or 'n'") == "y":
    print("\033c", end='')
    print(logo)
    set_difficulty()
    play_game()