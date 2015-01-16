'''
In this module we remove duplicates in a string

'''


def remove_duplicates(string):
	'''
	Remove duplicated characters in string

	'''
    result = []
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)