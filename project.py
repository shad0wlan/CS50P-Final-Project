class CoffeeMachine:

    def __init__(self):
        self.materials = dict(water=400, milk=540,
                              coffee_beans=120, money=550, cups=9)
        self.state = True
        self.coffee_types = {1: "espresso", 2: "latte", 3: "cappuccino"}
        self.coffee_requirements = {
            "espresso": {
                "water": 250,
                "coffee_beans": 16,
                "milk": 0,
                "money": 4,
                "cups": 1
            },
            "latte": {
                "water": 350,
                "milk": 75,
                "coffee_beans": 20,
                "money": 7,
                "cups": 1
            },
            "cappuccino": {
                "water": 200,
                "milk": 100,
                "coffee_beans": 12,
                "money": 6,
                "cups": 1
            }
        }

    def set_water(self, quantity):
        '''
            Set quantity water.
            :param quantity: Number of water to add
            :type quantity: int
            :return: False if quantity is not an int
            :return: True if quantity is an int
            :rtype: bool
        '''
        if self.amounts_validator(quantity):
            self.materials["water"] += quantity
            return True
        return False

    def get_water(self):
        """Returns coffee machice water ammount"""

        return self.materials["water"]

    def set_milk(self, quantity):
        """
            Set quantity milk.
            :param quantity: Number of milk to add
            :type quantity: int
            :return: False if quantity is not an int
            :return: True if quantity is an int
            :rtype: bool
        """
        if self.amounts_validator(quantity):
            self.materials["milk"] += quantity
            return True
        return False

    def get_milk(self):
        """Returns coffee machice milk ammount"""

        return self.materials["milk"]

    def set_coffee_beans(self, quantity):
        """
            Set quantity coffee_beans.
            :param quantity: Number of coffee_beans to add
            :type quantity: int
            :return: False if quantity is not an int
            :return: True if quantity is an int
            :rtype: bool
        """
        if self.amounts_validator(quantity):
            self.materials["coffee_beans"] += quantity
            return True
        return False

    def get_coffee_beans(self):
        """Returns coffee machice coffee_beans ammount"""

        return self.materials["coffee_beans"]

    def set_cash(self, quantity):
        """
            Set quantity cash.
            :param quantity: Number of cash to add
            :type quantity: int
            :return: False if quantity is not an int
            :return: True if quantity is an int
            :rtype: bool
        """
        if self.amounts_validator(quantity):
            self.materials["money"] += quantity
            return True
        return False

    def get_cash(self):
        """Returns coffee machice cash ammount"""

        return self.materials["money"]

    def set_cups(self, quantity):
        """
            Set quantity cups.
            :param quantity: Number of cups to add
            :type quantity: int
            :return: False if quantity is not an int
            :return: True if quantity is an int
            :rtype: bool
        """
        if self.amounts_validator(quantity):
            self.materials["cups"] += quantity
            return True
        return False

    def get_cups(self):
        """Returns coffee machice cups ammount"""
        return self.materials["cups"]

    def buy(self, kind_of_coffee, cups_amount=1):
        """
            Buy coffee.
            :param kind_of_coffee: Id of coffee to buy
            :type kind_of_coffee: int
            :param cups_amount: Amount of cups to buy
            :type cups_amount: int
            :return: False if not valid kind_of_coffee or not enough ingredients to make the coffee
            :return: True if valid kind_of_coffee and enough ingradients
            :rtype: bool
        """
        if not self.amounts_validator(cups_amount):
            print("Invalid cups")
            return False
        try:
            coffee_choice = self.coffee_requirements[self.coffee_types[int(
                kind_of_coffee)]]
        except (ValueError, KeyError):
            print("Wrong input format - choose a correct index for coffee")
            return False
        for i, j in coffee_choice.items():
            if self.materials[i] - (j * cups_amount) >= 0:
                if i == "money":
                    self.materials[i] += j
                else:
                    self.materials[i] -= j * cups_amount
            else:
                ingredient = i.replace("_", " ")
                print(f"Sorry, not enough {ingredient}!\n")
                return False
        print("I have enough resources, making you a coffee!\n")
        return True

    def fill_machine(self, water_amount, milk_amount, beans_amount, money_amount, cups_amount):
        """
            Fill coffee machine.
            :params water_amount, milk_amount, beans_amount, cups_amount: amounts to add
            :type params: int
            :return: False if not valid type
            :return: True if valid type
            :rtype: bool
        """
        validation = self.amounts_validator(
            water_amount, milk_amount, beans_amount, money_amount, cups_amount)
        if validation:
            self.set_water(water_amount)
            self.set_milk(milk_amount)
            self.set_coffee_beans(beans_amount)
            self.set_cups(cups_amount)
            self.set_cash(money_amount)

            return True
        return False

    def amounts_validator(self, *args):
        """Validates int instance for args"""
        for i in args:
            if not isinstance(i, int):
                print(f"Not valid input for {i}")
                return False
            if i < 0:
                return False
        return True

    def __str__(self):
        water_string = f'{self.materials["water"]} ml of water\n'
        milk_string = f'{self.materials["milk"]} ml of milk\n'
        beans_string = f'{self.materials["coffee_beans"]} g of coffee beans\n'
        cups_string = f'{self.materials["cups"]} disposable cups\n'
        money_string = f'${self.materials["money"]} of money\n'

        return f'The coffee machine has:\n{water_string + milk_string + beans_string + cups_string + money_string}'

    def take_money(self):
        """Takes all the earnings from the coffee machine"""
        earnings = self.materials["money"]
        self.materials["money"] -= earnings
        print(f"I gave you ${earnings}\n")
        return earnings

    def switch_state(self):
        """Changes machine state for main"""
        if self.state:
            self.state = False
        else:
            self.state = True
        return True


def main():
    machine = CoffeeMachine()
    while machine.state:
        action_to_do = input(
            "Choose index of action (1. Buy a coffee, 2. Fill the machine, 3. Remaining ingredients, 4. Take machine money, 5. Exit):\n").strip()
        if action_to_do in {"1", "2", "3", "4", "5"}:
            if action_to_do == "1":
                print()
                what_to_buy = input(
                    "What do you want to buy? 1. espresso, 2. latte, 3. cappuccino, 4. back:\n")
                if what_to_buy == "4":
                    continue
                else:
                    try:
                        coffee = int(what_to_buy)
                        quantity = int(input("How many cups? ").strip())
                    except ValueError:
                        print("Only integers allowed")
                        continue
                    machine.buy(coffee, quantity)
                    continue
            elif action_to_do == "2":
                print()
                try:
                    water = int(
                        input("Write how many ml of water you want to add:\n"))
                    milk = int(
                        input("Write how many ml of milk you want to add:\n"))
                    beans = int(
                        input("Write how many grams of coffee beans you want to add:\n"))
                    money = int(
                        input("Write how many cash you want to add:\n"))
                    cups = int(
                        input("Write how many disposable cups you want to add:\n"))
                    machine.fill_machine(water, milk, beans, money, cups)
                    print()
                    continue
                except ValueError as f:
                    print(f"Wrong input value in {f}")
                    continue
            elif action_to_do == "3":
                print()
                print(machine)
                continue
            elif action_to_do == "4":
                print()
                machine.take_money()
                continue
            else:
                machine.switch_state()
        else:
            print("Wrong action. Choose between 1-5 for example by inputting '1' for buy.")


if __name__ == "__main__":
    main()
