'''
In this module, we implement insertion sort
Time complexity (worst case): O(n ^ 2) (worst case is aray sorted in reverse order)
Time complexity (best case): O(n) (for nearly sorted and sorted arrays)

'''


def insertion_sort(arr):
    '''
    Sort array using insertion sort
    
    '''
    for index in range(1,len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position = position - 1
        arr[position] = current_value
