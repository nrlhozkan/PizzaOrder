import datetime
import pandas as pd
import csv 

class Pizza:
    def __init__(self, pizza_type):
        self.pizza_type = pizza_type

    def get_description(self):
        pass
    
    def get_cost(self):
        pass

class ClassicPizza(Pizza):
    def __init__(self, pizza_type):
        super().__init__(pizza_type)
        self.cost = 10
        self.description = f"{self.pizza_type} pizza" 

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class MargheritaPizza(Pizza):
    def __init__(self, pizza_type):
        super().__init__(pizza_type)
        self.cost = 12
        self.description = f"{self.pizza_type} pizza"

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class TurkishPizza(Pizza):
    def __init__(self, pizza_type):
        super().__init__(pizza_type)
        self.cost = 15
        self.description = f"{self.pizza_type} pizza"

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class SadePizza(Pizza):
    def __init__(self, pizza_type):
        super().__init__(pizza_type)
        self.cost = 8
        self.description = f"{self.pizza_type} pizza"

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class PizzaDecorator(Pizza):
    def __init__(self, topping):
        self.topping = topping
    
    def get_description(self):
        return self.topping.get_description() +  " with " + Pizza.get_description(self)
    
    def get_cost(self):
        return self.topping.get_cost() + Pizza.get_cost(self)
    
class Cheese(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 2
        self.description = "cheese"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost
    
class Pepperoni(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 3
        self.description = "pepperoni"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost
    
class Mushrooms(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 3
        self.description = "mushrooms"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost
    
class Olives(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 3
        self.description = "olives"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost
    
class Meat(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 4
        self.description = "meat"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost
    
class Onion(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 1
        self.description = "onion"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost
    
class Corn(PizzaDecorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.cost = 1
        self.description = "corn"
    
    def get_description(self):
        return self.topping.get_description() + " with " + self.description
    
    def get_cost(self):
        return self.topping.get_cost() + self.cost

def main(menu):
    # menu = open("menu.txt", "r")
    menu = menu.read()
    print(menu)
    try_again = True
    while try_again == True:
        pizza_type = input("What type of pizza would you like? \n")
        pizza_type = pizza_type.lower()
        pizza, try_again = chose_pizza(pizza_type, try_again)
        if try_again == False:
            print("Your order in not valid. Please try again.")
            break
        total_cost = pizza.get_cost()

        name = input("What is your name? \n")

        ID_number = input("What is your ID number? \n ID number must be 5 digits. \n ID number:")
        i = 1
        while len(ID_number) != 5:
            print("Your ID number is not valid. Please try again.")
            ID_number = input("What is your ID number? \n ID number must be 5 digits. \n ID number:")
            i += 1
            if i == 3:
                print("You have tried 3 times. Your order is cancelled. Please try again later.")
                break
        if i == 3:
            break

        credit_card = input("What is your credit card number? \n Credit card number must be 5 digits. \n Credit card number:")
        k = 1
        while len(credit_card) != 5:
            print("Your credit card number is not valid. Please try again.")
            credit_card = input("What is your credit card number? \n Credit card number must be 5 digits. \n Credit card number:")
            k += 1
            if k == 3:
                print("You have tried 3 times. Your order is cancelled. Please try again later.")
                break

        if k == 3:
            break 

        password = input("What is your password? \n") # password is not validated. It can be anything.

        save_order(name, ID_number, credit_card, password, pizza, total_cost)

        if try_again == True:
            print("Your order is: " + pizza.get_description() + ". The total cost is: " + str(total_cost) + "TL")
            print("You gave your order successfully. Thank you for ordering from us. Your order will be ready in 30 minutes. Have a nice day!")
            break

def save_order(name, ID_number, credit_card, password, pizza, total_cost):
    date = datetime.datetime.now()
    row = [name, ID_number, credit_card, password, pizza.get_description(), total_cost, date]
    database = open("Order_Database.csv", "a", newline = "") # newline = "" is to avoid blank lines between rows in the csv file. a is to append to the file.
    writer = csv.writer(database)
    writer.writerow(row)
    
def add_topping(pizza, try_again):
    mm = input("Would you like to add a topping? \n Please press 1: Yes, 0: No \n")
    if int(mm) == 1:
        topping = input("What topping would you like? \n")
        topping = topping.lower()
        if topping == "cheese" or int(topping) == 13:
            if int(topping) == 13:
                topping = "cheese"
            pizza = Cheese(pizza)
            return pizza, try_again
        elif topping == "pepperoni" or int(topping) == 17:
            if int(topping) == 17:
                topping = "pepperoni"
            pizza = Pepperoni(pizza)
            return pizza, try_again
        elif topping == "mushrooms" or int(topping) == 12:
            if int(topping) == 12:
                topping = "mushrooms"
            pizza = Mushrooms(pizza)
            return pizza, try_again
        elif topping == "olives" or int(topping) == 11:
            if int(topping) == 11:
                topping = "olives"
            pizza = Olives(pizza)
            return pizza, try_again
        elif topping == "meat" or int(topping) == 14:
            if int(topping) == 14:
                topping = "meat"
            pizza = Meat(pizza)
            return pizza, try_again
        elif topping == "onion" or int(topping) == 15:
            if int(topping) == 15:
                topping = "onion"
            pizza = Onion(pizza)
            return pizza, try_again
        elif topping == "corn" or int(topping) == 16:
            if int(topping) == 16:
                topping = "corn"
            pizza = Corn(pizza)
            return pizza, try_again
        else:
            print("Sorry, we don't have that topping")
            try_again = False
            return pizza, try_again
        
    elif int(mm) == 0:
        return pizza, try_again

def chose_pizza(pizza_type, try_again):
    if pizza_type == "classic" or int(pizza_type) == 1:
        if int(pizza_type) == 1:
            pizza_type = "classic"
        pizza = ClassicPizza(pizza_type)
        pizza, try_again = add_topping(pizza, try_again)
        return pizza, try_again
    elif pizza_type == "margherita" or int(pizza_type) == 2:
        if int(pizza_type) == 2:
            pizza_type = "margherita"
        pizza = MargheritaPizza(pizza_type)
        pizza, try_again = add_topping(pizza, try_again)
        return pizza, try_again    
    elif pizza_type == "turkish" or int(pizza_type) == 3:
        if int(pizza_type) == 3:
            pizza_type = "turkish"
        pizza = TurkishPizza(pizza_type)
        pizza, try_again = add_topping(pizza, try_again)
        return pizza, try_again
    elif pizza_type == "sade" or int(pizza_type) == 4:
        if int(pizza_type) == 4:
            pizza_type = "sade"
        pizza = SadePizza(pizza_type)
        pizza, try_again  = add_topping(pizza, try_again)
        return pizza, try_again
    else:
        print("Sorry, we don't have that pizza")
        pizza = None
        try_again = False
        return pizza, try_again

if __name__ == "__main__":
    menu = open("menu.txt", "r")
    main(menu)
    database = pd.read_csv("Order_Database.csv")
    print(database)
