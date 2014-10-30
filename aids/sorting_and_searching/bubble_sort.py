'''
In this module, we implement bubble sort

Time complexity: O(n ^ 2)

'''


def bubble_sort(arr):
    '''
    Sort array using bubble sort

    '''
    for index_x in xrange(len(arr)):
        for index_y in xrange(len(arr) - 1, index_x, -1):
            if arr[index_y] < arr[index_y - 1]:
                arr[index_y], arr[index_y - 1] = arr[index_y - 1], arr[index_y]	
