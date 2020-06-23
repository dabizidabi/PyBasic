car = {
    'mark': 'tesla',
    'model': 't1000',
    'year': 2020,
    'price': 202020,
    'colour': ['red', 'white', 'blue']
}

all_cars = []

all_cars.append(car)
all_cars.append(car)
all_cars.append(car)

for x in range(0, 5):
    all_cars.append(car.copy())

print(all_cars)

for x in all_cars:
    print(x)

print("----------------------------------")

all_cars[4]['year'] += 3
all_cars[3]['model'] = 'zaporojec'
for x in all_cars:
    print(x)

