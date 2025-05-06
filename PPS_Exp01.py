# Write a program to calculate the area of a circle and print the result as shown in the displayed test cases.

radius = float(input("Enter the radius : "))

if radius < 0 or radius > 100:
	print("Enter a positive value upto 100")

else:
	area = 3.14 * radius ** 2
	print(f"Area of circle = {area:.6f}")
