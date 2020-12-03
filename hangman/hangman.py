from tkinter import Tk, Canvas, Frame, BOTH
import random
import sys
import time

guessLetters = []
phantomWord = []
correctWord = ""
lives = 10

def ReadWordlist (path, i, j): # Read a word list file into a list of individual words (1 word per line)
    file = open (path, 'r')
    return [w.strip() for w in file.readlines() if len(w.strip()) <= j and len (w.strip()) >= i]

class Window(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Hangman")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)

root = Tk()
ex = Window()

def CheckUniqueness(guess): # Check to see if the user has already guessed this string
    return guess not in guessLetters


def CheckCharacter(guess): # Check to see if this character
    for i in range(len(correctWord)):
        if correctWord[i] == guess:
            phantomWord[i] = guess

    res = guess in correctWord
    print (("You guessed " + guess + " correctly!") if res else "That was an incorrect guess")
    return res


def CheckWord(guess):
    res = (guess == correctWord)
    print (("You guessed " + guess + " correctly!") if res else "That was an incorrect guess")
    return res


def LoseLife():
    global lives
    lives -= 1

def CheckWinCondition ():
    if lives <= 0:
        Lose()
    simWord = ''.join (phantomWord)
    if simWord == correctWord:
        Win()


def Win():
    print("You win!")
    RequestReplay()


def Lose():
    print("You lose...")
    RequestReplay()

def PlayLoop ():
    while True:
        CheckWinCondition()
        print ("Enter a letter, or a word")
        gu = input (">>> ").strip().lower()
        if not gu.isalpha():
            print ("Please don't enter numbers")
            continue
        
        Guess (gu)
        DrawCharacter()
        ShowCharacters()
        root.update_idletasks()
        root.update()

def Guess (st):
    if not CheckUniqueness (st):
        print ("You already guessed that!")
        return
    guessLetters.append (st)
    if len (st) > 1:
        if CheckWord (st):
            Win ()
        else:
            LoseLife()
    else:
        if not CheckCharacter (st):
            LoseLife ()
        
            

def ShowCharacters ():
    print (''.join (phantomWord))
    print ("You already guessed " + str(guessLetters))

def RequestReplay():
    while True:
        print("Do you wish to replay? (Y or N)")
        choice = input(">>> ").strip().lower()
        if choice == "y":
            RequestParameters()
            break
        elif choice == "n":
            sys.exit (0)
        else:
            print("Invalid input")

def InitialiseInterface ():
    global root
    global ex
    global lives
    root.geometry("400x350+100+100")
    root.resizable(False, False)
    DrawCharacter()
    ShowCharacters()
    root.update_idletasks()
    root.update()

def GenerateWord (l, d):
    global phantomWord
    global correctWord
    words = []
    if (d) == 0:
        words = ReadWordlist (l, 3, 4)
    if (d) == 1:
        words = ReadWordlist (l, 4, 6)
    if (d) == 2:
        words = ReadWordlist (l, 6, 8)

    word = words[random.randint (0, len(words)-1)]
    correctWord = word
    phantomWord = []
    for i in range (0, len (correctWord)):
        phantomWord.append ('_')

def RequestParameters():
    guessLetters = []
    lives = 10
    wlist = "words.txt"
    while True:
        print ("Would you like the Christmas version (Y or N)?")
        choice = input (">>> ").strip().lower()
        if choice == "y":
            wlist = "christmas_words.txt"
            break
        else:
            print ("Invalid input")
    
    while True:
        print ("What difficulty do you want? (hard, normal, easy)")
        choice = input (">>> ").strip().lower()
        if choice == "hard":
            GenerateWord (wlist, 2)
            break
        elif choice == "normal":
            GenerateWord (wlist, 1)
            break
        elif choice == "easy":
            GenerateWord (wlist, 0)
            break
        else:
            print ("Invalid input")
    InitialiseInterface()
    PlayLoop()

def DrawCharacter ():
    global lives

    if lives > 9:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(50, 300, 250, 300)
    if lives > 8:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(93, 300, 93, 50)
    if lives > 7:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(93, 50, 200, 50)
    if lives > 6:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(200, 50, 200, 80)
    if lives > 5:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_oval(180, 80, 220, 120)
    if lives > 4:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(200, 120, 200, 200)
    if lives > 3:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(200, 200, 230, 260)
    if lives > 2:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(200, 200, 170, 260)
    if lives > 1:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(200, 120, 230, 180)
    if lives > 0:
        ex.canvas.pack(fill=BOTH, expand=1)
        return
    ex.canvas.create_line(200, 120, 170, 180)
    
    ex.canvas.pack(fill=BOTH, expand=1)



print ("Welcome to the program.")
RequestParameters ()


    
