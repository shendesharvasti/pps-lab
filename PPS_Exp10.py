"""" Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system:

A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: Below 60

The program should display the average marks up to 2 decimal places and the assigned grade."""

s1 = float(input("subject 1: "))
s2 = float(input("subject 2: "))
s3 = float(input("subject 3: "))
s4 = float(input("subject 4: "))
s5 = float(input("subject 5: "))

a_marks = (s1+s2+s3+s4+s5)/5

if a_marks>=90:
	grade = "A"
elif a_marks>=80:
	grade="B"
elif a_marks>=70:
	grade="C"
elif a_marks>=60:
	grade="D"
else:
	grade="F"

print(f"Average Marks: {a_marks:.2f}")
print(f"Grade: {grade}")
