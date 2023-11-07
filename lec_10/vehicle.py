class Vehicle:
    def __init__(self, year,color):
        self.year = year
        self.color=color

    def vehicle_year(self):
        return f"Production year of Vehicle is {self.year}."
    
    def vehicle_color(self):
        return f"Color of Vehicle is {self.color}."