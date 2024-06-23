class Car :
    steeringWheel = 1    # class level attribute
    def __init__(self,name,wheels):
        self.name=name  # instance level attrubute
        self.wheels=wheels
        
    def drive(self):        # instance Method
        print(f'{self.name} is driving')
        
    @classmethod
    def common(cls):
        print(f'All car has only {cls.steeringWheel} steering Wheel')
        
# Merce = Car("Mercedes", 4 )
# print(Merce.steeringWheel)
# Merce.common()

# Merce.drive()

# print(Car.steeringWheel)
# print(Car.common())
# Car.common()