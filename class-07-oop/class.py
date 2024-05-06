#  Object Oriented Projct

class Car:
    def __init__(self, brand, model, year, offer, fipe):
        self.brand = brand
        self.model = model
        self.year = year
        self.offer = offer
        self.fipe = fipe

    def info(self):
        return (self.brand, self.model, self.year)
    
    def sale(self):
        if self.offer >= self.fipe:
            return"carro vendido!"
        else:
            return"ce acha q eu to liso!?"

myCar1 = Car("Toyota", "hillux", "2024", "345000", "350000")
myCar2= Car("Chevrolet", "Celta", "2006", "10000", "12000")

print(myCar1.brand)
print(myCar1.model)
print(myCar1.year)

print(myCar2.brand)
print(myCar2.info())
print(myCar2.sale())