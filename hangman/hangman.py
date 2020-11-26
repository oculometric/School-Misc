from tkinter import Tk, Canvas, Frame, BOTH
import time

guessLetters = []
phantomWord = []
correctWord = ""
lives = 10

root = Tk()
ex = Window()

class Window(Frame):

    def __init__(self):
        super().__init__()

        self.master.title("Hangman")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        

    def drawCharacter (self):
        global lives

        if lives > 9:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(50, 300, 250, 300)
        if lives > 8:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(93, 300, 93, 50)
        if lives > 7:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(93, 50, 200, 50)
        if lives > 6:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(200, 50, 200, 80)
        if lives > 5:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_oval(180, 80, 220, 120)
        if lives > 4:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(200, 120, 200, 200)
        if lives > 3:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(200, 200, 230, 260)
        if lives > 2:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(200, 200, 170, 260)
        if lives > 1:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(200, 120, 230, 180)
        if lives > 0:
            self.canvas.pack(fill=BOTH, expand=1)
            return
        self.canvas.create_line(200, 120, 170, 180)
        
        self.canvas.pack(fill=BOTH, expand=1)


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
            print("Invalid input")

def InitialiseInterface ():
    global root
    global ex
    root.geometry("400x350+100+100")
    ex.drawCharacter()
    while (True): # TODO REMOVE
        root.update_idletasks()
        root.update()
        time.sleep (1)
        lives -= 1
        ex.drawCharacter()

def RequestParameters():
    guessLetters = []
    lives = 10
    while True:
        print ("What difficulty do you want? (hard, normal, easy)")
        choice = input (">>> ").strip().lower()
        if choice == "hard":
            GenerateWord (2)
            break
        elif choice == "normal":
            GenerateWord (1)
            break
        elif choice == "easy":
            GenerateWord (0)
            break
        else:
            print ("Invalid input")
    InitialiseInterface()
    PlayLoop()

def DrawCharacter ():
    # TODO



def __main__():
    print ("Welcome to the program.")
    RequestParameters ()


    
