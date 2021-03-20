class Car:
    def __init__(self, manufacturer, model, year, engineSize, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.engineSize = engineSize
        self.price = price 


bmw3 = Car("BMW", "328d", 2018, 2.0, 24000.00)
audi3 = Car("Audi", "A3", 2010, 1.8, 7999.99)
ford2 = Car("Ford", "Mustang", 2010, 3.5, 27999.99)

cars = [bmw3, audi3, ford2]

for car in cars:
    print(car.manufacturer) 
    print(car.model) 
    print(car.year) 
    print(car.engineSize) 
    print(car.price)
    print("--------------")
