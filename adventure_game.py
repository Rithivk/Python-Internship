import time

# Function to prompt user for choices
def make_choice(options):
    while True:
        print("\nChoose your action:")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice. Please enter a number corresponding to your action.")

# Game introduction
def intro():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest...")
    time.sleep(1)
    print("Your mission is to find a hidden treasure!")
    time.sleep(1)

# Game storyline and logic
def forest_path():
    print("\nYou're standing at a crossroad in the forest.")
    time.sleep(1)
    choice = make_choice(["Go left", "Go right", "Go straight"])

    if choice == 1:
        print("\nYou encounter a pack of wolves!")
        time.sleep(1)
        print("You fight the wolves and barely escape.")
        return "dangerous_path"
    elif choice == 2:
        print("\nYou discover a hidden cave!")
        time.sleep(1)
        print("Inside the cave, you find a map.")
        return "cave_path"
    else:
        print("\nYou continue on the path.")
        time.sleep(1)
        print("You stumble upon a peaceful village.")
        return "village_path"

def dangerous_path():
    print("\nYou chose the dangerous path and faced the wolves!")
    time.sleep(1)
    print("Despite the danger, you survived.")
    time.sleep(1)
    return "game_over"

def cave_path():
    print("\nYou found a map in the cave.")
    time.sleep(1)
    print("The map leads you to a treasure chest!")
    time.sleep(1)
    return "victory"

def village_path():
    print("\nYou discover a peaceful village.")
    time.sleep(1)
    print("The villagers guide you to the treasure location.")
    time.sleep(1)
    return "victory"

# Game ending
def game_over():
    print("\nGame Over. Try again!")

def victory():
    print("\nCongratulations! You found the hidden treasure and won the game!")

# Main game function
def start_game():
    intro()
    current_location = forest_path

    while True:
        if current_location == forest_path:
            current_location = globals()[forest_path()]
        elif current_location == dangerous_path:
            current_location = globals()[dangerous_path()]
        elif current_location == cave_path:
            current_location = globals()[cave_path()]
        elif current_location == village_path:
            current_location = globals()[village_path()]
        elif current_location == "game_over" or current_location == "victory":
            globals()[current_location]()
            break

# Start the game
start_game()
