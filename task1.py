"""
===================   TASK 1   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You can use `rand` module to simulate dice
* rolling.
===================================================
"""

# Write your script here
from random import randint

def main():
    n = int(input("Insert number of times for rolling the dice: "))
    i = 0
    numberOfOnes = 0
    numberOfTwos = 0
    numberOfThrees = 0
    numberOfFours = 0
    numberOfFives = 0
    numberOfSixes = 0
    while i <= n:
        num = randint(1, 6)
        if num == 1:
            numberOfOnes = numberOfOnes + 1
        if num == 2:
            numberOfTwos = numberOfTwos + 1
        if num == 3:
            numberOfThrees = numberOfThrees + 1
        if num == 4:
            numberOfFours = numberOfFours + 1
        if num == 5:
            numberOfFives = numberOfFives + 1
        if num == 6:
            numberOfSixes = numberOfSixes + 1
        i = i + 1
    print("Number of ones: ", numberOfOnes)
    print("Number of twos: ", numberOfTwos)
    print("Number of threes: ", numberOfThrees)
    print("Number of fours: ", numberOfFours)
    print("Number of fives: ", numberOfFives)
    print("Number of sixes: ", numberOfSixes)
main()