#Test simple class
from Car import *


Mycar1 = Car("T1000", "red", 100000)
Mycar2 = Car("T500", "blue", 80000)

Mycar1.price_up()
Mycar2.show_car()
Mycar1.show_car()
Mycar1.mileage()
Mycar1.set_marka("Tavria")
Mycar1.show_car()