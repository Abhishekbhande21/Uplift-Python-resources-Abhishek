class Vehicle:
    def __init__(self, Brand, Model, Price, Mfgyear):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear



class Car(Vehicle):
    def __init__(self, Brand, Model, Price, Mfgyear, TotalSeats):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear
        self.TotalSeats = TotalSeats
        
        
    def DiscountCar(self):
         Dis = self.Price * 0.2
         print(Dis)


    def age(self):
        age = 2021 - self.Mfgyear
        if age>5:
            Print("Car is older than 5 Years")
        if age<=5:
            print("Car is yonger than 5 years")


class Electric(Car):
    def __init__(self, Brand, Model, Price, Mfgyear, TotalSeats, ChargingTime):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear
        self.TotalSeats = TotalSeats
        self.ChargingTime = ChargingTime


class Petrol(Car):
    def __init__(self, Brand, Model, Price, Mfgyear, TotalSeats, PetrolMil):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear
        self.TotalSeats = TotalSeats
        self.PetrolMil = PetrolMil


class Diesel(Car):
    def __init__(self, Brand, Model, Price, Mfgyear, TotalSeats, DieselMil):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear
        self.TotalSeats = TotalSeats
        self.DieselMil = DieselMil




class Bike(Vehicle):
    def __init__(self, Brand, Model, Price, Mfgyear, DiskBreak, EngineCap):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear
        self.DiskBreak = DiskBreak
        self.EngineCap = EngineCap

    def DiscountBike(self):
         Disc = self.Price * 0.3
         print(Disc)



class Truck(Vehicle):
    def __init__(self, Brand, Model, Price, Mfgyear, WeighingCap):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Mfgyear = Mfgyear
        self.WeighingCap = WeighingCap

    def DiscountTruck(self):
         Discount = self.Price * 0.3
         print(Discount)


A = Car("Mercedes", "Petrol-M1C", 1000000, 2017, 45)
A.DiscountCar()


B = Bike("BMW", "Bike-C2D", 300000, 2015, True, 1200)
B.DiscountBike()

C = Truck("Hindustan", "Truck-T1P", 200000, 2019, 1000)
C.DiscountTruck()


D = Car("Mercedes", "Petrol-M1C", 1000000, 2017, 45)
D.age()