# Insertion Sort Question: 
"""
Insertion Sort is another simple comparison-based sorting algorithm that works by iteratively building a sorted portion of the array, while moving unsorted elements into their correct position within the sorted portion.

Here's how the algorithm works:

    Start with the second element of the array and compare it with the first element.
    If the second element is smaller than the first element, swap them.
    Move to the next unsorted element and compare it with the sorted elements until it is in its correct position.
    Repeat steps 2 and 3 for each unsorted element in the array.
    
# Complexity:
Insertion Sort also has a time complexity of O(n^2), which makes it inefficient for large arrays. 
However, it can be more efficient than Bubble Sort for small or partially sorted arrays.
"""



# Example: 
"""
A program in Python that uses the Insertion Sort algorithm for an array of size 20 
and sorts the elements in descending order.
"""

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == '__main__':
    # Initialize array of size 20
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65, 14, 12, 99, 88, 73, 19, 23, 72, 49, 38]
    
    # Sort array using insertion sort in descending order
    insertion_sort_desc(arr)
    
    # Print sorted array
    print("Sorted array in descending order: ", arr)
