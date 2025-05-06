# Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.

import string

def remove_punctuation(sentence):
	return ''.join(char for char in sentence if char not in string.punctuation)

input_sentence = input("")
print(remove_punctuation(input_sentence))
