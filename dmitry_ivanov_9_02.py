############################
###   Pizzeria program   ###
############################

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

class Pizza():
    __menu = ['margherita', 'capricciosa', 'calzone']

    def __init__(self):
        self.__pizza_list = []

    def add_pizza(self, pizza, cheese):
        self.__pizza_list.append((pizza, cheese))

    def make_a_pizza(self, pizza, cheese):
        if pizza not in self.__menu:
            raise PizzaError(pizza, "no such pizza on the menu")
        if cheese > 100:
            raise TooMuchCheeseError(pizza, cheese, "too much cheese")
        print("Pizza is ready!")
    
    def make_pizza(self): 
        for (pz, ch) in self.__pizza_list:
            try:
                self.make_a_pizza(pz, ch)
            except TooMuchCheeseError as tmce:
                print(tmce, ':', tmce.cheese)
            except PizzaError as pe:
                print(pe, ':', pe.pizza)


# Main code
pizzeria = Pizza()

pizzeria.add_pizza('calzone', 0)
pizzeria.add_pizza('margherita', 150)
pizzeria.add_pizza('mafia', 20)

pizzeria.make_pizza()
