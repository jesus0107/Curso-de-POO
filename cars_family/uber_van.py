from car import Car

class UberVan(Car):
  type_car_accepted = ["Acura - MDX", "Audi - Q7", "Ford - Expedition", "Chevrolet - Tahoe", "GMC - Yukon"]
  seats_material = []
  
  def __init__(self, license = "", driver = "", type_car = "Van"):
    super().__init__(self,license, driver)
    self.type_car = type_car
  
  def set_passengers(self, value):
    if type(value) == int:
      if value != 6:
        return print("\nPor favor ingresa la cantidad de 6 pasajeros\n")
   
    return super().set_passengers(value)
  
  def print_data_car(self):
    print("\nCreacion de UberVan\n")
    print(f"Type Car: {self.type_car}")  
    super().print_data_car()