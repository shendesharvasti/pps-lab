# Write a python program to print factorial of given number.
#Note: If user enters a negative number as input prompt the message "Enter a positive number"

def factorial(n):
	if n<0:
		return "Enter a positive number"
	elif n==0 or n==1:
		return 1
	else:
		fact = 1
		for i in range(2,n+1):
			fact*=i
		return fact

num = int(input("Enter a number : "))
if num<0:
	print("Enter a positive number")
else:
	print("Factorial of given number is :",factorial(num))
