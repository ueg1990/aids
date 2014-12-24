'''
In this module we find the subarray which has the largest sum

'''

def max_subarray(arr):
    '''
    Return the value of largest sum in an array along with the start index
    and finish index of the subarray

    '''
    if not len(arr):
        raise Exception('Array is empty')
    running_sum = max_sum = arr[0]
    index_max_sum, start_index, finish_index = 0, 0, 0
    for index in range(1, len(Arr)):
        if arr[index] > running_sum + arr[index]:
            running_sum = arr[index]
            index_max_sum = index
        else:
            running_sum += arr[index]
        if running_sum > max_sum:
            max_sum = running_sum
            start_index = index_max_sum
            finish_index = index
    return max_sum, start_index, finish_index
   
# Alternate implementation
# 1) Return maximum positive sum in subarray
# def max_subarray(arr):
#     max_ending_here = max_sum = 0
#     for item in arr:
#         max_ending_here = max(0, max_ending_here + item)
#         max_sum = max(max_sum, max_ending_here)
#     return max_sum
# 2) Return maximun sum in subarray (non-zero sum)        
# def max_subarray(arr):
#     max_ending_here = max_sum = arr[0]
#     for item in arr[1:]:
#         max_ending_here = max(item, max_ending_here + item)
#         max_sum = max(max_sum, max_ending_here)
#     return max_sum
