import random
from time import sleep
turns=7
WordList = ['sergeanty','amphipneustic','hypochil','grus','depressed','distortedly','unselected','crakow','preendorsing','convenient']
wor=(random.choice(WordList))
def mainimg(turns):
    if (turns == 7):
                    print ("_________")
                    print ("|	 |")
                    print ("|")
                    print ("|")
                    print ("|")
                    print ("|")
                    print ("|________\n\n")
    elif (turns == 6):
                    print ("_________")
                    print ("|	 |")
                    print ("|	 O")
                    print ("|")
                    print ("|")
                    print ("|")
                    print ("|________\n\n")
    elif (turns == 5):
                    print ("_________")
                    print ("|	 |")
                    print ("|	 O")
                    print ("|	 |")
                    print ("|	 |")
                    print ("|")
                    print ("|________\n\n")
    elif (turns == 4):
                    print ("_________")
                    print ("|	 |")
                    print ("|	 O")
                    print ("|	\|")
                    print ("|	 |")
                    print ("|")
                    print ("|________\n\n")
    elif (turns == 2):
                    print ("_________")
                    print ("|	 |")
                    print ("|	 O")
                    print ("|	\|/")
                    print ("|	 |")
                    print ("|	 ")
                    print ("|________\n\n")
    elif (turns == 1):
                    print ("_________")
                    print ("|	 |")
                    print ("|	 O")
                    print ("|	\|/")
                    print ("|	 |")
                    print ("|	/ ")
                    print ("|________\n\n")
    elif (turns == 0):
                    print ("_________")
                    print ("|	 |")
                    print ("|	 O")
                    print ("|	\|/")
                    print ("|	 |")
                    print ("|	/ \ ")
                    print ("|________/")
                    print ("\n")
                    print ("\n")
                    print ("The word was "+wor)
                    print ("\nYOU LOSE! TRY AGAIN!")
                    print ("\nWould you like to play again, type 1 for yes or 2 for no?")
def rules():
    print("The computer is the executioner.\n")
    sleep(1)
    print("The computer will think of a word or short phrase \nan mark out blanks (short lines) for each letter of each word.\n")
    sleep(2.5)
    print("Separate words with either a slash, a fairly wide \ngap, or place words on separate lines.\n")
    sleep(2.5)
    print("Then you will guess a letter.\n")
    sleep(2.5)
    print("If that letter is in the word(s) then write the letter \n in everywhere it would appear, an cross out that letter in the alphabet.\n")
    sleep(2.5)
    print("If the letter isn't in the word then add a body part \n to the gallows (head, body, left arm, right arm, left leg, right leg).\n")
    sleep(2.5)
    print("The player will continue guessing letters until they \ncan either solve the word (or phrase) or all six body parts are on the gallows.\n")
    sleep(2.5)

def playAgainvar():
    pavq1=input("Would you like to play again.")
    if pavq1=="Yes" or pavq1=="yes":
        playAgain=True
        #continue
    if pavq1=="No" or pavq1=="no":
        playAgain=False

playAgain=True

list("apple")=["a","p"

def maingame():
    turns=7
    mainimg(turns)
    worcounter=len(wor)
    guesses=""
    myList=[]

    wor2=list(wor)
    for x in range(0, worcounter):
        myList.append("_")
    " ".join(myList)
    while turns > 0:
        print (" ".join(myList))
        print("\n\nYou have "+str(turns)+" attempts left to guess the correct answer.\n")
        guesses=input("Guess a letter\n")
        correct = False
        for x in range(0,len(wor)):
            if guesses == wor2[x]:
                myList[x]=guesses
                correct = True
                print("You have got the right answer\n\n")
                if wor2==myList:
                    print("Congrats, you have won. After "+str(turns)+" guesses left.\n")
                    print("The word was "+wor)
                    return turns
        if not correct:
            print("You got the wrong answer.")
            turns = turns-1
            mainimg(turns)






while (playAgain):
    question = input("Hi, would you like to play hangman.\n")
    sleep(0.5)
    if question=="Yes" or question=="yes":
        question0=input("What is your name?\n")
        sleep(0.6)
        print(question0+", welcome to hangman.")
        sleep(0.75)
        print("The game will start in...")
        sleep(0.75)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        print("0")
        question2=input("Do you know how to play Hangman.\n")
        if question2=="Yes" or question2=="yes":

            sleep(0.75)
        elif question2=="No" or question2=="no":
            rules()
        else:
            print("You have entered an invalid input")

        print("Now that you know the rules...\n LETS PLAY")
        sleep(1)
        maingame()
#stuff to put in here
        timestop=False
        if timestop==False:
            playAgainvar()
        elif question=="No" or question=="no":
            print("Goodbye")
            playAgain=False
            exit()
        else:
            print("You have entered an invalid input")
