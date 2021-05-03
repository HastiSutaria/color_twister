from tkinter import *
import tkinter.font as font
import random
colors = ["Red", "Yellow", "Green", "Blue", "White", "Black", "Pink", "Purple", "Cyan", "Magenta", "Light blue", "Orange"]
timer = 60
score = 0
dwc = ''
def startGame():
    global dwc
    if(timer == 60):
        startCountDown()
        dwc = random.choice(colors).lower()
        display_wordwc.config(text=random.choice(colors), fg=dwc)
        color_entry.bind('<Return>', displayNextWord)

def resetGame():
    global timer, score, dwc
    timer = 60
    score = 0
    dwc = ''
    game_score.config(text = "Your Score : " + str(score))
    display_wordwc.config(text = '')
    time_left.config(text="Game Ends in : -")
    color_entry.delete(0, END)

def startCountDown():
    global timer
    if(timer >= 0):
        time_left.config(text = "Game Ends in : " + str(timer) + "s")
        timer -= 1
        time_left.after(1000,startCountDown)
        if (timer == -1):
            time_left.config(text="Game Over!!!")

def displayNextWord(event):
    global dwc
    global score
    if(timer > 0):
        if(dwc == color_entry.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        color_entry.delete(0, END)
        dwc = random.choice(colors).lower()
        display_wordwc.config(text = random.choice(colors), fg = dwc)
root = Tk()
root.title("Color Twister")
root.geometry("500x300")
root.configure(bg = 'aquamarine2')
app_font = font.Font(family='Helvetica', size = 14)
game_rules = "Game Description \n Enter the color of the words displayed below. \n And  not to enter the word text itself."
myFont = font.Font(family='Helvetica')
game_des = Label(root, text = game_rules, font = app_font, fg= "DarkOrchid4")
game_des.pack()
game_score = Label(root, text = "Your Score : " + str(score), font = (font.Font(size=18)), fg = "DeepPink3")
game_score.pack()
display_wordwc = Label(root , font = (font.Font(size=28)), pady = 10)
display_wordwc.pack()
time_left = Label(root, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "Red")
time_left.pack()
color_entry = Entry(root, width = 30)
color_entry.pack(pady = 10)
btn_frame = Frame(root, width= 80, height = 40, bg= 'red')
btn_frame.pack(side = BOTTOM)
start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "DarkOliveGreen1", bd = 2,padx = 20, pady = 10 , command = startGame)
start_button.grid(row=0, column= 0)
reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "DarkOliveGreen1", bd = 2,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)

root.mainloop()