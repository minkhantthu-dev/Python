# name = "kk"
# print(type(name))
# print(name)
# print(name.upper())

# class Car : 
#     def __init__(self):
#         self.name="Mercedes"
#         self.wheels=4
        
#     def drive(self):
#         print(f'{self.name} is driving')
        
# Merce = Car()
# Merce.drive()
# print(Merce.name)
class Car : 
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels
        
    def drive(self):
        print(f'{self.name} is driving')
        
Merce = Car("Mercedes", 4 )
Merce.drive()

Lambo = Car("Lamborghini", 4 )
Lambo.drive()



class Bicycle : 
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels
        
    def drive(self):
        print(f'{self.name} is driving')
        
Bic = Bicycle("BMX", 2)
Bic.drive()