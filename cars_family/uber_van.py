from car import Car

class UberVan(Car):
  type_car_accepted = ["Acura - MDX", "Audi - Q7", "Ford - Expedition", "Chevrolet - Tahoe", "GMC - Yukon"]
  seats_material = []
  
  def __init__(self, license, driver, type_car):
    super().__init__(license, driver)
    self.select_car(type_car)
  
  def select_car(self, type_car):
    c = [car for car in self.type_car_accepted if self.type_car_accepted.__contains__(type_car)]
    return print(f"Carro agregado con exito: {c}")
  
  def set_passengers(self, value):
    if value != 6:
      print("Por favor ingresa la cantidad de 6 pasajeros")
    else:
      return super().set_passengers(value)