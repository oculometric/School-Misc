guessLetters = []
phantomWord = []
correctWord = ""
lives = 10

def CheckUniqueness(guess):
    return guess not in guessLetters


def CheckCharacter(guess):
    for i in range(len(correctWord)):
        if correctWord[i] == guess:
            phantomWord[i] = guess
    simWord = ""
    for j in range(len(correctWord)):
        simWord += phantomWord[i]
    return simWord == correctWord  # Returns true if all characters have been guessed


def CheckWord(guess):
    return guess == correctWord


def LoseLife():
    global lives
    lives -= 1

def CheckWinCondition ()
    if lives <= 0:
        Lose()


def Win():
    print("You win!")
    RequestReplay()


def Lose():
    print("You lose...")
    RequestReplay()


def RequestReplay():
    while True:
        print("Do you wish to replay? (Y or N)")
        choice = input(">>> ").strip().lower()
        if choice == "y":
            RequestParameters()
            break
        elif choice == "n":
            System.exit (0)
        else:
            print("Invalid Input")


def RequestParameters():
    print("Hello, I am an empty subroutine.")
