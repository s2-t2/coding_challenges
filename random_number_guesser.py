#!/usr/bin/python
from random import randrange, uniform

# 1. Total number of guesses required to find a target (hidden) value within a range of 0-100. 
totalGuesses = 0
def MyNumber(target):
    guess = None 
    global totalGuesses
    while (guess != target):
        guess = randrange(0,100)
        totalGuesses+=1
    return totalGuesses
#The target value is 80
print (MyNumber(80))


#2. Total number of guesses it takes until all the possible values are guessed. 

myList = ['None'] 
numberOfGuess = 0

while (len(myList) != 101):
    value = randrange(0,100)
    numberOfGuess = numberOfGuess + 1
    for i in range(0,len(myList)):
        if (value not in myList):
            myList.append(value )

print (numberOfGuess)


#generate random numbers between 1 - 100 until all the possible values have
#been guessed.
#Get the number of guesses it took until all the possible values were guessed

#print (myList) 
#print (randrange(0,10 ) )
