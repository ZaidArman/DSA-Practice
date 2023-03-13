# Bubble Sort Question: 
"""
Bubble sort is a simple comparison-based sorting algorithm. It repeatedly iterates through the array, compares adjacent elements, and swaps them if they are in the wrong order. 
The algorithm gets its name from the way smaller or larger elements "bubble" to the top of the array during each iteration.

Here's how the algorithm works:

   -- Start at the beginning of the array and compare the first two elements.
   -- If the first element is greater than the second element, swap them.
   -- Move to the next pair of adjacent elements and repeat step 2.
   -- Repeat this process for each pair of adjacent elements until the end of the array is reached.
   -- At this point, the largest element will be at the end of the array.
   -- Repeat steps 1 through 5 for each element in the array, except for the last one.
   -- The array should now be sorted in ascending order.
    
It is mainly used for educational purposes or for sorting small arrays.

# complexity
Bubble Sort has a time complexity of O(n^2), which makes it inefficient for large arrays. 

"""



#Example:
"""
A program that uses the Bubble Sort algorithm to sort an array of 50 integers in ascending order, 
and a separate function to sort them in descending order.
"""

import random
def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Create an array of 50 random integers
arr = [random.randint(1, 100) for _ in range(50)]
print("Original Array:", arr)

# Sort the array in ascending order using Bubble Sort
bubble_sort_ascending(arr)
print("Array in Ascending Order:", arr)

# Sort the array in descending order using the sorting function
bubble_sort_descending(arr)
print("Array in Descending Order:", arr)
