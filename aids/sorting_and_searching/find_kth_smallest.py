'''
In this module, we find the kth smallest element in an array in O(n) time

'''

from quicksort import partition

def find_kth_smallest(alist, left,right, k):
	if len(alist) == 1:
		return alist[0]
	pivot = partition(alist, left,right)
	if k == pivot:
		return alist[pivot]
	if pivot  > k:
		return find_kth_smallest(alist,left,pivot - 1,k)
	else:
		return find_kth_smallest(alist, pivot + 1, right, k - pivot)
