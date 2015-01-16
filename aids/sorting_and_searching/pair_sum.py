'''
Given an integer array, output all pairs that sum up to a specific value k

'''

from binary_search import binary_search_iterative

def pair_sum_sorting(arr, k):
	'''
	Using sorting - O(n logn)

	'''
	number_of_items = len(arr)
	if number_of_items < 2:
		return 
	arr.sort()
	for index, item in enumerate(arr):
		index_pair = binary_search_iterative(arr, index, number_of_items - 1, k - item)
		if index_pair and index_pair > index:
			print item, arr[index_pair]

def pair_sum_set(arr, k):
	'''
	Using set - O(n) (time - average case), O(n) (space)

	'''
	if len(arr) < 2:
		return
	seen = set()
	output = set()
	for item in arr:
		target = k - item
		if target not in seen:
			seen.add(target)
		else:
			output.add(item, target) # print item, target
			# for output with non-duplicate i.e. (1,3) and (3,1) are the samw thing
			# output.add((min(num, target), max(num, target)))
	print '\n'.join([str(item) for item in output])