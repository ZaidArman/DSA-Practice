# Quick Sort Question: 
"""
Quick Sort is another divide-and-conquer algorithm that works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted using the same process, until the entire array is sorted.

Here's how the algorithm works:

    Choose a pivot element from the array. This can be done in various ways, such as selecting the first or last element, or choosing a random element.
    Partition the array into two sub-arrays: elements less than the pivot, and elements greater than or equal to the pivot.
    Recursively sort the two sub-arrays using the same process.
    Concatenate the sorted sub-arrays to produce the final sorted array.
    
# Complexity: 
Quick Sort has a time complexity of O(n log n) on average, but can have a worst-case time complexity of O(n^2) if the pivot element is not well-chosen, such as in the case of a sorted or nearly sorted array. 
However, in practice, Quick Sort is often faster than other sorting algorithms for large arrays.

"""

# Example:
"""
A program that uses the Quick Sort algorithm to sort an array of 50 integers in ascending order.
"""

# Ascending Order
import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

# Generate a random array of 50 integers
arr = [random.randint(1, 100) for i in range(50)]

print("Original array:")
print(arr)

# Sort the array using quick sort in ascending order
sorted_arr = quick_sort(arr)

print("Sorted array (ascending order):")
print(sorted_arr)


# Descending order
def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort_descending(left) + [pivot] + quick_sort_descending(right)

# Generate a random array of 50 integers
arr = [random.randint(1, 100) for i in range(50)]

print("Original array:")
print(arr)

# Sort the array using quick sort in descending order
sorted_arr = quick_sort_descending(arr)

print("Sorted array (descending order):")
print(sorted_arr)

