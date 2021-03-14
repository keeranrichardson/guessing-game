import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext as st

characters=["Professor Plum", "Mrs White", "Mr Green", "Mrs Peacock", "Miss Scarlett", "Colonel Mustard"]
weapons=["Wrench", "Candlestick", "Lead Pipe", "Rope", "Revolver", "Knife"]
rooms=["Study", "Kitchen", "Hall", "Conservatory", "Lounge", "Ballroom", "Dining Room", "Library", "Billiard Room"]

application_window = tk.Tk()
application_window.title("cluedo")
application_window.config(bg = "Purple")
application_window.geometry("750x400")

gameState = "notStarted"
guesses = "N/A"

def generateMurder(characters, weapons, rooms):
    murderer=random.choice(characters)
    weapon=random.choice(weapons)
    room=random.choice(rooms)
    crime=[murderer, weapon, room]
    return crime

def tkinterPrint(message):
    global application_window
    print(message)
    text_area.insert(tk.END, message)
    text_area.insert(tk.END, "\n")
    text_area.see(tk.END)
    

def getValidAnswer(options):
    guess=entry.get()
    entry.delete(0, 'end')
    if guess not in options:
        tkinterPrint(guess+ " is not a valid input")
        return ""
        
    return guess

def inputGuess(options, question):
    prompt = question + "\n"
    questionNumber = 1
    for option in options:
        prompt += str(questionNumber) + ". " + option + "\n" 
        questionNumber += 1
    
    tkinterPrint(prompt)
    

def checkGuess(guess, answer):
    if guess.upper()==answer.upper():
        tkinterPrint("You got it right!")
        return True
    else:
        tkinterPrint("You got it wrong!")
        return False

def guessCrime(questions, crimeList, crimeScene, characters, weapons, rooms):
    global correctGuesses
    global questionNumber
    global gameState
    global guesses
    if guesses>0:
        guessAnswer=getValidAnswer(crimeList[questionNumber])
        if guessAnswer == "":
            return
        guesses-=1
        if checkGuess(guessAnswer, crimeScene[questionNumber]):
            correctGuesses+=1
            questionNumber+=1

def chooseLevel():

    difficulty={"easy":13,"medium":8,"hard":3}
    
    validAnswer = getValidAnswer(difficulty)
    if validAnswer != "":
        return difficulty[validAnswer]
    return ""

def playgame(event = None):
    global gameState
    global guesses
    global characters
    global weapons
    global rooms
    global crimeScene
    global correctGuesses
    global questionNumber
    global questions
    global crimeList

    if gameState=="notStarted":
        tkinterPrint("Click on the Start Game button!")
        return

    if gameState=="started":
        button2.config(text="Restart Game")
        tkinterPrint("Hello and welcome to Keeran's Cluedo!\nFirst you need to select a difficulty, do you want easy, medium or hard?")
        gameState = "chooseDificulty"
        crimeScene = generateMurder(characters, weapons, rooms)
        print(crimeScene)
        correctGuesses=0
        questionNumber=0
        return

    if gameState=="chooseDificulty":
        guesses = chooseLevel()  
        if guesses != "":
            label2.config(text = ("Guesses remaining:", guesses))
            gameState = "askQuestion1"
            questions=("Who do you think the murderer was?", "What do you think the weapon was?", "Which room do you think it was?")
            crimeList=(characters, weapons, rooms)
            inputGuess(crimeList[questionNumber], questions[questionNumber])
        return

    if gameState=="askQuestion1":
        guessCrime(questions, crimeList, crimeScene, characters, weapons, rooms)
        label2.config(text = "Guesses remaining: "+ str(guesses))
        if guesses == 0 and correctGuesses != 3:
            tkinterPrint("You lost the game!")
            gameState = "startGame"
            tkinterPrint("Click 'Restart Game' to restart!")
            return
        if questionNumber < 3:
            inputGuess(crimeList[questionNumber], questions[questionNumber])
        else:
            if correctGuesses == 3:
                tkinterPrint("You won the game!")
                gameState = "startGame"
                tkinterPrint("Click 'Restart Game' to restart!")
            else:
                tkinterPrint("You lost the game!")
                gameState = "startGame"
                tkinterPrint("Click 'Restart Game' to restart!")
        return
                       
def restart():
    global gameState
    global guesses
    guesses = "N/A"
    gameState = "started"
    playgame()

label1 = tk.Label(application_window, text="Keeran's Cluedo!", font =("Arial", 44), bg = "Purple", fg = "White")
label1.pack()

button2 = tk.Button(text="Start Game", command=restart, bg = "Yellow", fg = "Black")
button2.pack()

entry = tk.Entry(application_window)
entry.pack()

application_window.bind('<Return>', playgame)

button1 = tk.Button(text="Enter", command=playgame, bg = "Yellow", fg = "Black")
button1.pack()

label2 = tk.Label(application_window, text=guesses, bg = "Purple", fg = "White")
label2.pack()

text_area = st.ScrolledText(application_window) 
text_area.pack() 

application_window.mainloop()

    
