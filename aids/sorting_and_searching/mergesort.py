'''
In this module, we implement merge sort
Time complexity: O(n * log n)
'''


def mergesort(arr):
    '''
    Sort array using  mergesort
    
    '''
    if len(arr) > 1:		
		mid = len(arr) / 2
		left = mergesort(arr[:mid])
		right = mergesort(arr[mid:])
		return merge(left, right)
	return arr
    

def merge(left, right):
    '''
    Merge sorted arrays
    
    '''
    result = []
	i,j = 0,0
	while i <= len(left) - 1 and j <= len(right) - 1:
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result
