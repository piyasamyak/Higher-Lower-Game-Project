from art import logo, vs
from game_data import data
import random, os

# Main Game Screen
def game_screen(optionA, optionB):
    print(
        f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}."
    )
    print(vs)
    print(
        f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}."
    )


# Tidies up game screen
def game_header():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


# Returns the follower count for an item from game data
def follower_count(option):
    return option["follower_count"]


# Starts game
def play_game(optionA, optionB):
    score = 0
    isCorrect = False
    continueGame = True
    while continueGame == True:
        game_header()
        if isCorrect:
            print(f"That's right! Current Score: {score}")
        game_screen(optionA, optionB)

        answer = input("Who has more followers? Type 'A' or 'B'? ").upper()
        if (answer == "A" and follower_count(optionA) < follower_count(optionB)) or (
            answer == "B" and follower_count(optionB) < follower_count(optionA)
        ):
            game_header()
            print(f"Sorry, that's wrong. Final Score: {score}")
            continueGame = False
        else:
            score += 1
            isCorrect = True
            if follower_count(optionB) > follower_count(optionA):
                optionA = optionB
            optionB = random.choice(data)
    ask_to_restart()


# Restarts game
def ask_to_restart():
    print()
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()

    if play_again == "y":
        optionA, optionB = generate_options()
        play_game(optionA, optionB)
    elif play_again == "n":
        print("Thank you for playing! See you next time.")


# Generates two unique options
def generate_options():
    optionA = random.choice(data)
    optionB = random.choice(data)
    while optionA == optionB:
        optionB = random.choice(data)
    return optionA, optionB


optionA, optionB = generate_options()
play_game(optionA, optionB)
