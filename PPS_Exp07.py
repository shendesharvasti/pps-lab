# Write a program to read temperature in Celsius and print the temperature in fahrenheit.

def cel(celcius):
	return(celcius*9/5)+32

celcius = float(input("celsius: "))

fahrenheit = cel(celcius)

print(f"fahrenheit: {fahrenheit}")
