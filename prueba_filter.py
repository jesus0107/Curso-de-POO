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

found_car = list(filter_car(cars_acepted, "Acura"))

for dict in found_car:
  for key, value in dict.items():
    print(f"{key}: {value}")
