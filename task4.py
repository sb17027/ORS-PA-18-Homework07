"""
===================   TASK 4  ====================
* Name: Number of Appearances
*
* Write a function that will return which element
* of integer list has the greatest number of
* appearances in that list.
* In case that multiple elements have the same
* number of appearances return any.
*
* Note: You are not allowed to use built-in
* functions.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def mostOccurences(arr):
    mostNumber = arr[0]
    maxNumberOfOccurences = 1
    currNumberOfOccurences = 0
    currNumber = 0
    i = 1
    while i < len(arr):
        currNumber = arr[i]
        currNumberOfOccurences = 0
        j = 0
        while j < len(arr):
            if(arr[j] == currNumber):
                currNumberOfOccurences = currNumberOfOccurences + 1
            j = j + 1
        if currNumberOfOccurences > maxNumberOfOccurences:
            maxNumberOfOccurences = currNumberOfOccurences
            mostNumber = currNumber
        i = i + 1
    return mostNumber

def main():
    arr = [1, 3, 4, 6, 1, 1, 12, 12, 12, 12, 12, 12, 12]
    mostNumber = mostOccurences(arr)
    print("Number with most occurences: ", mostNumber)
main()
