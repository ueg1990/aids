'''
In this module, we implement a function which gets the intersection
of two sorted arrays. 

'''

def intersection_sorted_arrays(arr_1, arr_2):
	'''
	Return the intersection of two sorted arrays

	'''
	result = []
	i,j = 0,0
	while i < len(arr_1) and j < len(arr_2):
		if arr_1[i] == arr_2[j]:
			result.append(arr_1[i])
			i += 1
			j+=1
		elif arr_1[i] < arr_2[j]:
			i += 1
		else:
			j += 1
	return result