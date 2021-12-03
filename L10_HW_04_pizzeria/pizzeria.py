###################################################################
###                                                             ###
###   TITLE       : Pizzeria program v0.2                       ###
###   AUTHOR      : Dmitry Ivanov                               ###
###   DESCRIPTION : This program simulates a working pizzeria   ###
###                                                             ###
###################################################################

from packages.pizza import pizza        

pizzeria = pizza.Order()

# make order
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('margherita', 40), ('mafia', 20)]:
    try:
        pizzeria.make_pizza(pz, ch)
    except pizza.TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except pizza.PizzaError as pe:
        print(pe, ':', pe.pizza)
print("\n")
# add pizza
for pz in ["pepperoni", "calzone", "mafia", "margharita"]:
    try:
        pizzeria.add_pizza(pz)
    except pizza.PizzaError as pe:
        print(pe, ':', pe.pizza)
print("\n")
# remove pizza
for pz in ["pepperoni", "calzone", "mafia", "margharita", "monty"]:
    try:
        pizzeria.remove_pizza(pz)
    except pizza.PizzaError as pe:
        print(pe, ':', pe.pizza)

pizzeria.close()
