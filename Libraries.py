
#   (key)    (value)

car = {
    'mark': 'tesla',
    'model': 't1000',
    'year': 2020,
    'price': 202020,
}

print(car)

print("Car is: " + car['mark'] + " " + (car['model']))

car['colour'] = 'red'

print(car)

del car['colour']
print(car)

car['year'] = car['year'] - 5
if car['year'] < 2019:
    car['model'] = 't500'
    car['price'] = 15000
print(car)

print(car.keys())
print(car.values())
