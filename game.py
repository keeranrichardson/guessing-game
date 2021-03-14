import random

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
    print("you have", guesses,"guesses left")
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
            print("That is not a valid input")
        guess=input(prompt)
            
    return guess

def checkGuess(guess, answer):
    if guess==answer:
        print("you got it right")
        return True
    else:
        print("you got it wrong")
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
        
    print("you got",correctGuesses,"guesses right")

def chooseLevel():

    difficulty={"easy":15,"medium":10,"hard":5}
 
    return difficulty[getValidAnswer("Do you want easy, medium or hard difficulty?\n", difficulty)]

while True:   
    crimeScene=generateMurder(characters, weapons, rooms)
    print(crimeScene)
    guesses = chooseLevel()
    guessCrime(crimeScene, characters, weapons, rooms, guesses)
    playAgain=input("do you want to play again? y/n")
    if playAgain == "y":
        continue
    else:
        break
