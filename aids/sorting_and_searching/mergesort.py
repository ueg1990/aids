'''
In this module, we implement merge sort
Time complexity: O(n * log n)
'''


def mergesort(arr, left, right):
    '''
    Sort array using  mergesort
    
    '''
    if left < right:
        middle = left + (right - left) /2
        mergesort(arr, left, middle)
        mergesort(arr, middle+1, right)
        return merge(arr, left, mid, right)
    

def merge(arr, left, mid, right):
    '''
    Merge sorted arrays
    
    '''
    pass
