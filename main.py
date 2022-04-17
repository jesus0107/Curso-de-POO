from car import Car
from cars_family.uberx import UberX
from cars_family.uber_van import UberVan

def main():
  car1 = Car(license="AWS125", driver="Jesus")
  # car1.license = "AWS123"
  # car1.driver = "Jesus Cruz"
  # print(f"Car license {car1.license}")
  # car1.print_data_car()

  print("\n \nCreando una instancia de uber x\n \n")
  uber_x_a = UberX("AWS145","Jesus","Honda", "Civic")
  uber_x_a.print_data_uber_x()
  uber_x_a.set_passengers(6)
  uber_x_a.print_data_uber_x()
  
  
  print("\nCreando una instancia de uber van\n")
  uber_van_x = UberVan("ASD2345", "Jesus Cruz", "Acura - MDX")
  

if __name__ == "__main__":
    print("Clases en python")
    main()