"""
Main entry point for the application.
A simple command-line utility example.
"""

from src.utils.utils import greet_user


def main():
    print("Welcome to My Python Project!")

    name = input("What is your name? ").strip()

    if not name:
        print("You didn't enter a name.")
        return

    message = greet_user(name)
    print(message)


if __name__ == "__main__":
    main()
