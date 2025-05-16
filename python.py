class Car:
    wheel=4
    def __init__(self,model,year):      #constructor
        self.model=model                   #Assign Attributes -value when fun call
        self.year=year                     #instance variable       
    @classmethod
    def drive(cls):    		 #methods  are operation/fun within class
        return f"you can drive{cls.wheel}"

car1 =Car("Lenovo",2024)                #Object
                        #method 
print(Car.drive())                                       
