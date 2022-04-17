from ejemplo_encapsulamiento import Circulo

def run():
  my_circle = Circulo(2)
  print(f"El valor del radio es {my_circle._Circulo__radio}")
  my_circle._Circulo__radio = 34
  print(f"El nuevo valor de radio es {my_circle._Circulo__radio}")
  
if __name__ == "__main__":
  run()