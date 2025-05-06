# Write a program to print the sum of digits of a number.
#For example: If the number is 1234, then the sum of digits, 1 + 2 + 3 + 4 = 10 should be printed.

num = input("num: ")
sum=0

for i in num:
	sum = sum + int(i)

print("sum:",sum)
