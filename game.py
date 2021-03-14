import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext as st 

characters=["Professor Plum", "Mrs.White", "Mr Green", "Mrs.Peacock", "Miss Scarlett", "Colonel Mustard"]
weapons=["Wrench", "Candlestick", "Lead Pipe", "Rope", "Revolver", "Knife"]
rooms=["Study", "Kitchen", "Hall", "Conservatory", "Lounge", "Ballroom", "Dining Room", "Library", "Billiard Room"]



def generateMurder(characters, weapons, rooms):
    murderer=random.choice(characters)
    weapon=random.choice(weapons)
    room=random.choice(rooms)
    crime=[murderer, weapon, room]
    return crime

def inputGuess(guesses, options, question):
    tkinterPrint("you have "+str(guesses)+" guesses left")
    prompt = question + "\n"
    questionNumber = 1
    for option in options:
        prompt += str(questionNumber) + ". " + option + "\n" 
        questionNumber += 1
    
    return getValidAnswer(prompt, options)

def getValidAnswer(prompt, options):

    guess=""
    while guess not in options:
        if guess != "":
            tkinterPrint("That is not a valid input")
        guess=tkinterInput(prompt)
            
    return guess

def tkinterInput(prompt, title="Input"):
    global application_window

    answer = simpledialog.askstring(title, prompt)

    return answer

def tkinterPrint(message):
    global application_window
    print(message)
    text_area.insert(tk.INSERT, message)
    text_area.insert(tk.INSERT, "\n")
    text_area.see(tk.END)

def checkGuess(guess, answer):
    if guess==answer:
        tkinterPrint("you got it right")
        return True
    else:
        tkinterPrint("you got it wrong")
        return False

def guessCrime(crimeScene, characters, weapons, rooms, guesses):
    correctGuesses=0

    questions=("Who do you think the murderer was?", "What do you think the weapon was?", "Which room do you think it was?")
    crimeList=(characters, weapons, rooms)
    questionNumber=0

    while guesses>0:
        guessAnswer=inputGuess(guesses, crimeList[questionNumber], questions[questionNumber])
        guesses-=1
        if checkGuess(guessAnswer, crimeScene[questionNumber]):
            correctGuesses+=1
            questionNumber+=1
        if correctGuesses == 3:
            break
        
    tkinterPrint("you got "+str(correctGuesses)+" guesses right")

def chooseLevel():

    difficulty={"easy":15,"medium":10,"hard":5}
 
    return difficulty[getValidAnswer("Do you want easy, medium or hard difficulty?\n", difficulty)]

application_window = tk.Tk()
application_window.title("cluedo")
text_area = st.ScrolledText(application_window, width = 30, height = 8) 
  
text_area.grid(column = 0, pady = 10, padx = 10) 

while True:   
    crimeScene=generateMurder(characters, weapons, rooms)
    print(crimeScene)
    guesses = chooseLevel()
    guessCrime(crimeScene, characters, weapons, rooms, guesses)
    playAgain=tkinterInput("do you want to play again? y/n")
    if playAgain == "y":
        continue
    else:
        break
