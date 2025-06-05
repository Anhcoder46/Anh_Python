class Car:
    num_wheels = 4
    
    def __init__(self, color, style):
        self.color = color
        self.style = style
        self.speed = 0
        
    def change_speed(self, speed):
        self.speed = speed
    
    def change_color(self, color):
        self.color = color
        
my_car = Car(color = "black", style = "Macsadec")
print(my_car.color)