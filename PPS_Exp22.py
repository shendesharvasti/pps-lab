""""Take an integer n from the user. Your task is to Write a program to find out the sum of the digits of the given number using the process of recursion. Print the result as shown in the Test cases. 

The program defines the Sumof() function.
In the main program it takes the input n and sends it to the Sumof() function.
The Sumof() function contains base and recursive criterion.


Constraints:

1 <= integer <= 106



Sample Test Case:

4532 ----> Input integer

14 ----> Sum of the digits of the given number (4+5+3+2 = 14)"""

def Sumof(n):
	sum=0
	while(n!=0):
		sum=sum+n%10
		n=n//10
	return sum
n = int(input(""))
result = Sumof(n)
print(result)
