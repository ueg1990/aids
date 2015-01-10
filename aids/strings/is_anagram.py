'''
In this module, we determine if two given strings are anagrams

'''

def is_anagram_sort(string_1, string_2):
	'''
	Return True if the two given strings are anagrams using sorting

	'''
	return sorted(string_1) == sorted(string_2)

def is_anagram_counter(string_1, string_2):
	'''
	Return True if the two given strings are anagrams using Counter

	'''
	from collections import Counter
	return Counter(string_1) == Counter(string_2)

def is_anagram(string_1, string_2):
	'''
	Return True if the two given strings are anagrams using dictonaries

	'''
    from collections import defaultdict
    if len(string_1) != len(string_2):
    	return False
    char_count = defaultdict(int)
    for char in string_1:
    	char_count[char] += 1
    for char in string_2:
    	char_count[char] -= 1
    	if char_count[char] < 0:
    		return False
    return True




