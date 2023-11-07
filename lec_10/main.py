from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,seat,year=2012,color="Black"):
        super().__init__(year,color)
        self.seat=seat

    def car_seats(self):
        return f"This car has {self.seat} seats."
    
class Boat(Vehicle):
    def __init__(self, name, year=2019, color="White"):
        super().__init__(year, color)
        self.name = name

    def boat_name(self):
        return f"The name of this boat is {self.name}."

class Plane(Vehicle):
    def __init__(self,airport,year=2020,color="White"):
        super().__init__(year,color)
        self.airport=airport

    def plane_airport(self):
        return f"This plane can land at the airport: {self.airport}."
    
class RaceCar(Car):
    def __init__(self, seat, speed, year=2018, color="Red"):
        super().__init__(seat, year, color)
        self.speed = speed

    def racecar_speed(self):
        return f"This race car can reach a top speed of {self.speed} mph."
    def car_seats(self):
        if self.seat>=1 and self.seat<=2:
            return super().car_seats()
        else:
            return "Race cars must have 1 or 2 seats."

if __name__=="__main__":
    car1=Car(4)
    print(car1.car_seats(),car1.vehicle_color())
    #print(Car.__mro__)
    boat1=Boat("Titanic",1911)
    print(boat1.boat_name(),boat1.vehicle_year())
    #print(Boat.__mro__)
    racecar1=RaceCar(4,220)
    print(racecar1.car_seats(),racecar1.vehicle_color(),racecar1.racecar_speed())