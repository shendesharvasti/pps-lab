# Write a Python program that prompts the user to input a date (year, month, and day) and checks if it is a valid date. If the entered date is valid, the program should increment the date by one day and display the incremented date. The program should take into account leap years when determining the number of days in February.

days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
year=int(input("year: "))
month=int(input("month: "))
day=int(input("day: "))
if(year%4==0 and year%100!=0)or(year%400==0):
	days_in_month[1]=29
if 1<=month<=12 and 1<=day<=days_in_month[month-1]:
	print("valid")
	day+=1
	if day>days_in_month[month-1]:
		day=1
		month+=1
		if month>12:
			month=1
			year+=1
	print(f"incremented date: {year}-{month:02d}-{day:02d}")
else:
	print("invalid")
