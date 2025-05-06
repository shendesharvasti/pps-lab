# Write a python program to define a module to find Fibonacci Numbers and import the module to another program.

import fibonacci_module
n = int(input("Enter the max value: "))

if n > 0:
	result = fibonacci_module.generate_fibonacci_sequence(n)
	print(f"Fibonacci series upto {n} :")
	for num in result:
		print(num, end=" ")
else:
	print("Please enter a positive integer")
	
def generate_fibonacci_sequence(n):
	fib_series = []
	a, b = 0, 1
	for _ in range(n):
		fib_series.append(a)
		a, b = b, a + b
	return fib_series
