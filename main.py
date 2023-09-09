#opens mo pin file
mopinfile = open("mopin.txt", "r")
#reads mo pin
mopinfilecontents = mopinfile.read()
#imports time module for making the game pause
import time
#imports os module to execute system commands e.g.  clearing screen
import os
#imports maths functions
import operator
#creates points variables
pointint = int(0)
strpointint = str(0)
#prepoint handler
def prepoints(preintsetup):
    global pointint
    #makes string version of points integer with new points
    pointint = int(operator.add(preintsetup, pointint))
    pass
#handles points
def points():
    global pointint
    global strpointint
    strpointint = str(pointint)
    #clears the screen
    os.system('cls')
    #displays the points
    print("You have "+ strpointint + "point(s)")
    #continues with code
    pass
#question handler
def question(qnumber: str):
    if qnumber == '1':
        print("Would you buy anything that says sustainably sourced if you were tryting to be sustainable? [yes/no]")
        q1answer = input()
        if q1answer == 'yes':
            prepoints(1)
            points()
            pass
        elif q1answer == 'mo':
            mo('1')
            pass
        else:
            prepoints(-1)
            points()
            pass
    elif qnumber == '2':
        print("Does being sustainable have a positive effect on the environment? [yes/no]")
        q2answer = input()
        if q2answer == 'yes':
            prepoints(1)
            points()
            pass
        elif q2answer == 'mo':
            mo('2')
            pass
        else:
            prepoints(-1)
            points()
            pass
    elif qnumber == '3':
        print("Is planting trees a sustainable way to improve air quality?")
        q3answer = input()
        if q3answer == 'yes':
            prepoints(1)
            points()
            pass
        elif q3answer == 'mo':
            mo('3')
            pass
        else:
            prepoints(-1)
    else:
        print("error")
#creates manual overide
def mo(question):
    global mopinfilecontents
    os.system("cls")
    print("MANUAL OVERIDE: ENTER PIN")
    EnteredPin = input()
    if EnteredPin == mopinfilecontents:
        destination = input()
        question(destination)
        pass
    else:
        print("INCORRECT PIN")
        question(question)
question('1')
question('2')
question('3')
print("thankyou")
time.sleep(5)
