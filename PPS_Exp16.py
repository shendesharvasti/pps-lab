# Write a Python program that prints prime numbers less than n which represents the upper limit.

def is_prime(num):
	if num<2:
		return False
	for i in range(2,int(num ** 0.5)+1):
		if num%i==0:
			return False
	return True

def print_primes(n):
	for num in range(2,n):
		if is_prime(num):
			print(num)

upper_limit = int(input("Enter upper limit: "))
print_primes(upper_limit)
