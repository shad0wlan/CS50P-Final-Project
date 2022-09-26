from project import CoffeeMachine

# dict(water=400, milk=540,
#      coffee_beans=120, money=550, cups=9)


def test_get_water():
    machine = CoffeeMachine()
    assert machine.get_water() == 400


def test_set_water():
    machine = CoffeeMachine()
    assert machine.set_water(100) == True
    assert machine.get_water() == 500
    assert machine.set_water("c") == False
    assert machine.set_water(-1) == False


def test_get_milk():
    machine = CoffeeMachine()
    assert machine.get_milk() == 540


def test_set_wmilk():
    machine = CoffeeMachine()
    assert machine.set_milk(100) == True
    assert machine.get_milk() == 640
    assert machine.set_milk("c") == False
    assert machine.set_milk(-1) == False


def test_get_coffee_beans():
    machine = CoffeeMachine()
    assert machine.get_coffee_beans() == 120


def test_set_coffee_beans():
    machine = CoffeeMachine()
    assert machine.set_coffee_beans(100) == True
    assert machine.get_coffee_beans() == 220
    assert machine.set_coffee_beans("c") == False
    assert machine.set_coffee_beans(-1) == False


def test_get_cash():
    machine = CoffeeMachine()
    assert machine.get_cash() == 550


def test_set_cash():
    machine = CoffeeMachine()
    assert machine.set_cash(100) == True
    assert machine.get_cash() == 650
    assert machine.set_cash("c") == False
    assert machine.set_cash(-1) == False


def test_get_cups():
    machine = CoffeeMachine()
    assert machine.get_cups() == 9


def test_set_cups():
    machine = CoffeeMachine()
    assert machine.set_cups(100) == True
    assert machine.get_cups() == 109
    assert machine.set_cups("c") == False
    assert machine.set_cups(-1) == False

def test_amounts_validator():
    machine = CoffeeMachine()

    assert machine.amounts_validator(1) == True
    assert machine.amounts_validator(1, -1) == False
    assert machine.amounts_validator(1, -1, "cat") == False

def test_take_money():
    machine = CoffeeMachine()
    money = machine.get_cash()
    assert machine.take_money() == money
    assert machine.get_cash() == 0

def test_buy():
    machine = CoffeeMachine()
    assert machine.buy(1, 3) == False
    assert machine.buy(1, 1) == True
    machine.fill_machine(1000, 1000, 1000, 1000, 0)
    assert machine.buy(1, 3) == True
    assert machine.buy("cat") == False
    assert machine.buy(4) == False
    assert machine.buy(2, -1) == False
    assert machine.buy(1, "cat") == False














