"""
===================   TASK 3  ====================
* Name: Insertion Sort
*
* Write a function that will implement insertion sort
* algorithm. Generate list of 1000 random integer
* numbers and sort the list using your function.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def insertionSort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k <= arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

def main():

    arr = [5, 1, 12, 4, 7]
    print("Sorting the array....")
    insertionSort(arr)
    print("Sorted array: ")
    i = 0
    while i < len(arr):
        print("%d" %arr[i])
        i = i + 1
main()
