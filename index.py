
from bank import bank_scene

def start_game():
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.")

    bank_scene()


def resolve_peacefully():
    print("You choose to try to resolve the situation peacefully.")

def main():
    start_game()

if __name__ == "__main__":
    main()
