cars_acepted = [
  {"Bradn": "Acura", "Model": "MDX"},
  {"Bradn": "Audi", "Model": "Q7"}
  ]

def filter_car(list_cars, car):
  def iterartor_func(dict):
    for value in dict.values():
      if car in value:
        return True
    return False
  return filter(iterartor_func, list_cars)

found_car = filter_car(cars_acepted, "Acura")
print(list(found_car))