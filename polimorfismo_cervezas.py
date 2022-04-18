class Drink:
  def __init__(self, name, brand):
    self.name = name
    self.brand = brand
  
  def print_data(self):
    print(f"La bebida es {self.name} de la marca {self.brand}")

class SoftDrink(Drink):
  def __init__(self, name, brand, type, kal, ml):
    super().__init__( name, brand)
    self.type = type
    self.kal = kal
    self.ml = ml
    
  def print_data(self):
    super().print_data()
    print(f"Tipo: {self.type}")
    print(f"Calorias: {self.kal}")
    print(f"Cantidad: {self.ml} ml")

class Cerveza(Drink):    
  def __init__(self, name:str, brand:str, alcohol:float, ml:float):
    super().__init__(name, brand)
    self.alcohol = alcohol
    self.ml = ml
    
  def print_data(self):
    super().print_data()
    print(f"Porcentaje de alcohol: {self.alcohol}")
    print(f"Cantidad: {self.ml} ml")

coca_ligth = SoftDrink("Coca", "Cocacola", "ligth", 156, 355)
coca_ligth.print_data()

modelo = Cerveza("Modelo", "Modelo", 4.5, 355)
modelo.print_data()