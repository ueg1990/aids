'''
Reverse a string

'''

def reverse_string_iterative(string):
	result = ''
	for char in range(len(string) - 1, -1 , -1):
		result += char
	return result

def reverse_string_recursive(string):
    if string:
    	return reverse_string_recursive(string[1:]) + string[0]
    return ''

def reverse_string_pythonic(string):
	return string[::-1]
	