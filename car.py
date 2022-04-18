from account import Account

class Car:
  def __init__(self, id = 0, license = "", driver = Account.name, passanger = 0):
    self.id = id
    self.license = license
    self.driver = driver
    self.__passegenger = passanger
  
  def print_data_car(self):
    print(f"License: {self.license} \nDriver: {self.driver}\nPassengers: {self.__passegenger}")
    
  def get_passengers(self):
    print(f"La cantidad de pasajeros permitida es de: {self.__passegenger}")
    
  def set_passengers(self, value):
      if type(value) != int:
        return print("\npor favor ingresa un tipo de dato numerico entero\n")
      
      self.__passegenger = value
      print(f"\nEl numero de pasajeros es de {self.__passegenger}\n")

    
