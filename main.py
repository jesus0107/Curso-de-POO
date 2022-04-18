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
  uber_x_a.print_data_car()
  uber_x_a.set_passengers(4)
  uber_x_a.print_data_car()
  
  
  print("\nCreando una instancia de uber van\n")
  uber_van_x = UberVan("ASD2345", "Jesus", "Acura")
  uber_van_x.print_data_car()
  uber_van_x.set_passengers(6)
  uber_van_x.print_data_car()
  
  

if __name__ == "__main__":
    print("Clases en python")
    main()