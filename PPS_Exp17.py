# Write a program to count the number of vowels using sets in a given string.

def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	count = sum(1 for char in str if char in vowel)
	return count
str = input()
vowel_count(str)
print(vowel_count(str))
