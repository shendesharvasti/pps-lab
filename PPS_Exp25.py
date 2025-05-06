""""Implement a Python program using a class named Complex to perform operations on complex numbers. The class has the following methods:

initComplex(): A method that takes user input for the real and imaginary parts to initialize a complex number.
display(): A method that displays the complex number in the form "a + bi".
sum(): A method that computes the sum of two complex numbers and stores the result in the current instance.


The program creates three instances of the Complex class, initializes two complex numbers, displays them, computes their sum, and displays the result."""

class Complex ():
	def __init__(self, real=0, imag=0):
		self.real = real
		self.imag = imag
	def initComplex(self, num):
		print(f"complex number {num}")
		self.real = int(input("Real Part: "))
		self.imag = int(input("Imaginary Part: "))
	def display(self):
		print(f"{self.real}+{self.imag}i")
	def sum(self, c1, c2):
		self.real = c1.real + c2.real
		self.imag = c1.imag + c2.imag
		print("Sum: ", end="") 
c1 = Complex()
c2 = Complex()
c3 = Complex()
c1.initComplex(1)
c1.display()
c2.initComplex(2)
c2.display()
c3.sum(c1,c2)
c3.display()
