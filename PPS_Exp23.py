""""Write a Python program that functions as a simple phone book manager with a menu-driven interface. The program prompts the user to choose from the following options:

Add Contact
Remove Contact
Display
Quit


The program uses a dictionary to store contact information, where the contact name serves as the key and the associated phone number as the value. The user can add a contact, remove a contact, display the current contacts, or exit the program."""

contacts = {}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")

	choice = int(input("Enter choice (1-4): "))

	if choice == 1:
		name = input("Name: ")
		phone = input("Phone number: ")
		contacts[name] = phone
	elif choice == 2:
		name = input("Name: ")
		if name in contacts:
			del contacts[name]
		else:
			print("Not found")
	elif choice == 3:
		print(contacts)
	elif choice == 4:
		break
	else:
		print("Invalid")
