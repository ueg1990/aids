'''
In this module, we implement quicksort
Time complexity (average case) : O(n * log n)
Time complexity (worse case) : O(n ^ 2)

'''


def quicksort(arr, left, right):
    '''
    Sort array using  quicksort
    
    '''
    if left < right:
		pivot = partition(arr, left,right)
		quick_sort(arr, left,pivot - 1)
		quick_sort(arr, pivot + 1, right)
    

def partition(arr, left, right):
    '''
    Partition array around pivot value such that all values
    less than the pivot value are to the left of the pivot value
    and all values greater than the pivot value are to the right
    
    Three ways to choose pivot:
    1) First value in the array
    2) A random value in the array
    3) Median of 3 where the median of the first value, last 
       value and the middle value is chose as the pivot
    
    '''
    pivot_value = arr[left]
	index = left + 1
	for j in range(left + 1, right+1):
		if arr[j] < pivot_value:
			arr[index], arr[j] = arr[j], arr[index]
			index += 1
	arr[index - 1], arr[left] = arr[left], arr[index-1]
	return index-1
	
# Alternate implementation of the partition method
# def partition(alist, left, right):
# 	pivot_value = alist[left]
# 	left_mark = left + 1
# 	right_mark = right
# 	while left_mark < right_mark:
# 		while alist[left_mark] < pivot_value:
# 			left_mark += 1
# 		while alist[right_mark] > pivot_value:
# 			right_mark -=1
# 		if left_mark < right_mark:
# 			alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
# 	alist[left], alist[right_mark] = alist[right_mark], alist[left]
# 	return right_mark
