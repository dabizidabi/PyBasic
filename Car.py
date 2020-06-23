class Car():
    """Class create car"""
    def __init__(self, model, color, price):
        """initiate car"""
        self.mark = 'Zaporojec'
        self.model = model
        self.color = color
        self.price = price

    def show_car(self):
        """print all parameters of car"""
        dicription = (self.mark + " Model is: " + self.model + " color: " + str(self.price) + "$")
        print(dicription)

    def price_up(self):
        """Upgrade price"""
        self.price += 1000

    def mileage(self):
        """Start mileage"""
        print("Car: " + self.mark + self.model + " start running...")

    def set_marka(self, new_mark):
        self.mark = new_mark