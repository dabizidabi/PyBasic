#Test simple class
from Car import *


Mycar1 = Car("Zaporojec", "T1000", "red", 100000)
Mycar2 = Car("Zaporojec", "T500", "blue", 80000)

Mycar1.price_up()
Mycar2.show_car()
Mycar1.show_car()
Mycar1.mileage()
Mycar1.set_marka("Tavria")
Mycar1.show_car()


MyElectroCAr = electro_car("Zaporojec", "v50", "White", 10000)

MyElectroCAr.show_car()
MyElectroCAr.make_battery()
MyElectroCAr.make_battery()
MyElectroCAr.battery = 30   #close to change argument with __variable (encapsul)
MyElectroCAr.make_battery()
MyElectroCAr.show_car()