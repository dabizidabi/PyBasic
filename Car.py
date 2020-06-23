class Car():
    """Class create car"""
    def __init__(self, mark, model, color, price):
        """initiate car"""
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def show_car(self):
        """print all parameters of car"""
        dicription = (self.mark + " Model is: " + self.model + " color: " + self.color + ", price is : " + str(self.price) + "$")
        print(dicription)

    def price_up(self):
        """Upgrade price"""
        self.price += 1000

    def mileage(self):
        """Start mileage"""
        print("Car: " + self.mark + self.model + " start running...")

    def set_marka(self, new_mark):
        self.mark = new_mark

#Chield class
class electro_car(Car):
    """Class to create eletro car"""
    def __init__(self, mark, model, color, price):
        """Initiate electo car"""
        super().__init__(mark, model, color, price)
        self.__engine_class = 'Electro engine'
        self.__battery = 100

    def make_battery(self):
        """Use battery"""
        self.__battery -= 10

    def show_car(self):
        dicription = (self.mark + " Model is: " + self.model + " color: " + self.color + ", price is: " + str(self.price) + "$ ," + self.__engine_class + " battery: " + str(self.__battery))
        print(dicription)


