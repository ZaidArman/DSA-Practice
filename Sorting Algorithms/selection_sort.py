# Selection Sort Question: 
"""
Selection Sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. This process is repeated until the entire array is sorted.

Here's how the algorithm works:

    Set the first element of the array as the minimum value.
    Iterate through the remaining elements of the array, and if an element is smaller than the current minimum, set it as the new minimum.
    Swap the minimum element with the first element of the unsorted part of the array.
    Repeat the above process for the remaining unsorted part of the array until the entire array is sorted.
    
It is mainly used for educational purposes or for sorting small arrays.


# Complexity:
Selection Sort has a time complexity of O(n^2), which makes it inefficient for large arrays. 

"""



# Example:
"""
A program in Python that uses the Insertion Sort algorithm for an array of size 20 
and sorts the elements in descending order.
"""

import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# generate random array of size 10000
arr = [random.randint(0, 1000) for i in range(10000)]
# arr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65, 14, 12, 99, 88, 73, 19, 23, 72, 49, 38]

# calculate execution time
start_time = time.time()
sorted_arr = selection_sort(arr)
end_time = time.time()

# print sorted array and execution time
print("Sorted array:", sorted_arr)
print("Execution time:", end_time - start_time, "seconds")

