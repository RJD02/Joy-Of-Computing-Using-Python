'''
Bubble Sort
You are required to sort a given list of integers in ascending order using Bubble sort algorithm. Determine the
number of swaps that occur in the process.

Input Format

A single line of the input contains space separated integers

Output Format

Print an integer value corresponding to the number of swaps. (No newline after the output)

Example

Input

3 4 2 1 5

Output

5
'''
def bubbleSort(arr):
    swap_count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return swap_count

arr = input().split(" ")
print(bubbleSort(arr))