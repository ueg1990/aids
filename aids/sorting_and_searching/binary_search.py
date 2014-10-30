'''
In this module, we implement binary search in Python both
recrusively and iteratively

Assumption: Array is sorted

Time complexity: O(log n)

'''


def binary_search_recursive(arr, left, right, value):
    '''
    Recursive implementation of binary search of a sorted array
    Return index of the value found else return None
    '''
    if left <= right:
        middle = (left + right) / 2
        if arr[middle] == value:
            return middle
        if arr[middle] > value:
            return binary_search_recursive(arr, left, middle - 1, value)
        return binary_search_recursive(arr, middle + 1, right, value)
    return None


def binary_search_iterative(arr, left, right, value):
    '''
    Iterative implementation of binary search of a sorted array
    Return index of the value of found else return None
    
    '''
    while left <= right:
        middle = (left + right) / 2
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    return None
