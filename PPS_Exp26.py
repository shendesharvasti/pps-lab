""""Follow the instructions to create a Python program modeling cars with specific types: Car1 and Car2. Begin by defining a base class Car with attributes brand, price, model, and color. Subsequently, create two derived classes, Car1 and Car2, both inheriting from the Car class. Each derived class should introduce its attributes, and:

Implement a method display_details in the base class Car to print the common attributes (brand, price, model, color).
Override the display_details method in each derived class (Car1 and Car2) to print the brand, price, model, and color respectively."""

class Car:
	def __init__(self, brand, price, model, color):
		self.brand = brand
		self.price = price
		self.model = model
		self.color = color

	def display_details(self):
		print(self.brand)
		print(self.price)
		print(self.model)

		print(self.color)
def get_car_details():
	brand = input("brand: ")
	price = float(input("price: "))
	model = input("model: ")
	color = input("color: ")
	return brand, price, model, color

print("Details for Car 1:")
car1_brand, car1_price, car1_model, car1_color = get_car_details()
car1 = Car(car1_brand, car1_price, car1_model, car1_color)
print("Details for Car 2:")
car2_brand, car2_price, car2_model, car2_color = get_car_details()
car2 = Car(car2_brand, car2_price, car2_model, car2_color)
print("Car 1 Details:")
car1.display_details()
print("Car 2 Details:")
car2.display_details()
