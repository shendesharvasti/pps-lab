# Write a Python program to find whether a given string is a palindrome or not.

def is_palindrome(s):
	return "palindrome" if s==s[::-1] else "not a palindrome"

input_string = input("")
print(is_palindrome(input_string))
