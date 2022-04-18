from car import Car

class UberX(Car):
  brand: str
  model: str
  
  def __init__(self, license = "", driver = "", brand = "", model = ""):
    super().__init__(self, license, driver)
    self.brand = brand
    self.model = model
    
  def print_data_car(self):
    """Reescribiendo el metodo print data car heredado del padre, agregando una instruccion mas
    
    agregamos la marca (self.brand) y el modelo (self.model)
    debajo de estas declaraciones mandamos a llamar el metodo de la superclase con las instrucciones que nos manda por default
    """
    print("\nCreacion de Uberx\n")
    print(f"Brand: {self.brand} \nModel: {self.model}")  
    super().print_data_car()
    
  def set_passengers(self, value):
    # Sobreescritura de metodo: "Polimorfismo"
    if type(value) == int:
      if value != 4:
        return print("\nPor favor ingresa la cantidad de 4 pasajeros\n")
   
    return super().set_passengers(value)

