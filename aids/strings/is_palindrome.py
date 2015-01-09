'''
In this module, we determine if a given string is a palindrome

'''

def is_palindrome(string):
	'''
	Return True if given string is a palindrome

	'''
	if len(string) < 2:
		return True
	if string[0] == string[-1]:
		return is_palindrome(string[1:-1])
	return False
