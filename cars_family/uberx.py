from car import Car

class UberX(Car):
  brand: str
  model: str
  
  def __init__(self, license = "", driver = "", brand = "", model = ""):
    super().__init__(self, license, driver)
    self.brand = brand
    self.model = model
    
  def print_data_uber_x(self):
    print("\nCreacion de Uberx\n")
    self.print_data_car()
    print(f"Brand: {self.brand} \nModel: {self.model}")  
    
  def set_passengers(self, value):
    if type(value) == int:
      if value != 4:
        return print("\nPor favor ingresa la cantidad de 4 pasajeros\n")
    else:
      return super().set_passengers(value)

