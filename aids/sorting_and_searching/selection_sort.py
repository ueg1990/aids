'''
In this module, we implement selection sort

Time complexity: O(n ^ 2)

'''


def selection_sort(arr):
    '''
    Sort array using selection sort

    '''
    for index_x in range(len(arr)):
        min_index = index_x
        for index_y in range(index_x + 1, len(arr)):
            if arr[index_y] < arr[min_index]:
                min_index = index_y
        arr[min_index], arr[index_x] = arr[index_x], arr[min_index]
