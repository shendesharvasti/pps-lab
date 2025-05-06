# Write a Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid. If the digits are valid, the program generates all possible combinations of these three digits and prints them. Each combination is formed by arranging the digits in different orders. If the input is not valid (digits are not between 0 and 9), the program should display as "Invalid".

d1 = input("digit1 (0-9): ")
d2 = input("digit2 (0-9): ")
d3 = input("digit3 (0-9): ")
if d1.isdigit() and d2.isdigit() and d3.isdigit() and (0 <= int(d1) <= 9) and (0 <= int(d2) <= 9) and (0 <= int(d3) <= 9):
	digits = [d1, d2, d3]
	print(d1 + d2 + d3)
	print(d1 + d3 + d2)
	print(d2 + d1 + d3)
	print(d2 + d3 + d1)
	print(d3 + d1 + d2)
	print(d3 + d2 + d1)
else:
	print("Invalid")
