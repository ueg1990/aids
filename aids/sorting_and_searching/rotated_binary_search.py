'''
In this module, we implement binary search on a rotated array

'''


def rotated_binary_search(arr, value):
    '''
    Return index of value found else return None
    
    '''
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = (right + left) / 2
		if arr[mid] == value:
			return mid
		if arr[left] < arr[mid]:
			if arr[left] <= value and value < arr[mid]:
				right = mid - 1
			else:
				left = mid + 1
		else:
			if arr[mid] < value and value <= arr[right]:
				left = mid + 1
			else:
				right = mid - 1
	return None
