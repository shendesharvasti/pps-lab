""" Write a Python program to print the following pattern.

Sample Input and Output:
Enter a number : 6
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* """

def print_pattern(n):
	for i in range(n,0,-1):
		print('* '*i)

num = int(input("Enter a number : "))
print_pattern(num)
