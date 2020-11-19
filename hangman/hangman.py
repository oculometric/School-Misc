from tkinter import Tk, Canvas, Frame, BOTH
import time

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
        
def DrawCharacter ():
    # TODO

root = Tk()
ex = Window()
root.geometry("400x350+100+100")
ex.drawCharacter()
while (True):
    root.update_idletasks()
    root.update()
    time.sleep (1)
    lives -= 1
    ex.drawCharacter()

    
