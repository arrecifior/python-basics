from os import strerror
from datetime import datetime

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, cheese, message):
        PizzaError.__init__(self, cheese, message)
        self.cheese = cheese

class Pizza():
    list_of_pizza = ['margherita', 'capricciosa', 'calzone']
    def __init__(self):
        pass
    def add_pizza(self, pizza): # add pizza to the list
        if pizza in self.list_of_pizza: # check if pizza is already in the list
            raise PizzaError(pizza, "Pizza already in the list")
        else:
            self.list_of_pizza.append(pizza)
        print(pizza, ": Successfully added to the list of pizza!")
        print("List of pizzas:", self.list_of_pizza)

    def remove_pizza(self, pizza): # removed pizza from the list
        if pizza in self.list_of_pizza: # check if pizza is in the list
            self.list_of_pizza.remove(pizza)
        else:
            raise PizzaError(pizza, "Pizza not in the list")
        print(pizza, ": Successfully removed from the pizza list!")
        print("List of pizzas:", self.list_of_pizza)

class Order(Pizza):
    def __init__(self):
        super().__init__()
        self.orders = {}
        self.counter = 1
        try:
            self.__f = open("pizza_order.log", 'a') # orders are logged into the pizza_order.log file
            self.__f.write("Pizzeria started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
            print("Session start time written to a file!")
        except IOError as e:
            print("I/O error occured: ", strerror(e.errno))

    def close(self):
        try:
            self.__f.write("Pizzeria closed: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
            print("Session end time written to a file!")
        except IOError as e:
            print("I/O error occured: ", strerror(e.errno))
        self.__f.close()

    def make_pizza(self, pizza, cheese):
        if pizza not in self.list_of_pizza:
            raise PizzaError(pizza, "no such pizza on the menu")
        if cheese > 100:
            raise TooMuchCheeseError(cheese, "too much cheese")
        self.orders.update({self.counter: pizza + ' ' + str(cheese)})
        print(self.counter, self.orders[self.counter], ": Has successfuly created!")
    
        try:
            self.__f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ' + str(self.counter) + '. '+ self.orders.get(self.counter) + '\n')
            print("File successfully written!")
        except IOError as e:
            print("I/O error occured: ", strerror(e.errno))

        self.counter += 1
