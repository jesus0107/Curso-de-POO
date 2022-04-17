class Circulo:
  __radio: float
  
  def __init__(self, radio):
    self.__radio = radio
    self.__pi = 3.1416
    
  def getPerimeter(self):
    per = 2*self.__pi * self.__radio
    return print(f"El perimetro del circulo el {round(per, 2)}")
    
  def setRadio(self, value):
    if type(value) == int or type(value) == float:
      if value < 0:
        print("Por favor ingresa un numero mayor a 0")
      else:
        self.__radio = value
        print(f"El valor del radio es {self.__radio}")
    else:
      print("Por favor ingresa un tipo de dato numerico")
        
  def getPi(self):
    return self.__pi
  
  