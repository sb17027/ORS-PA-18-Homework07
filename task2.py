
"""
===================   TASK 2  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def recursiveSum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursiveSum(arr[1:])

def main():
    arr = [3, 5, 1, 6]
    print("Sum is: ", recursiveSum(arr))

main()
