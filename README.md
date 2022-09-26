# Coffee Machine Simulator

#### Video Demo: (https://youtu.be/zSmUPinpmfo)
#### Description: Simulation of a user, a coffee machine and an employer responsible for that machine.

Hello, this project is about simulating a coffee machine. A coffee machine works
like this as you know:

1. We assume that the user has money. The user chooses a coffee and amount of cups to prepare. The machine instantiates with preconfigured coffees and materials
2. The coffee machine then calculates the ingredients based on the cups
3. if there are enough ingredients, it prepares the coffees by using those ingredients else it gives a message that there are not enough ingredients.
4. If there are not enough ingredients, the employee can fill the machine else the machine updates its cash and is giving the coffee.
5. At the end of the day the employee takes the available cash from the machine and then reffils it for the next day if he wants.

#### Coffee machine has the following functions:

* Function with the format `get_ingedient` that gets the value of the ingredient already in machine. No arguments required
* Function with the format `set_ingredient` that sets ingredient value. It takes a `quantity` argument that is integer > 0
* Function `amounts_validator` that gets `*args` as arguments and validates if the inputted quantity if valid.
* Function `buy` that takes `type of coffee` and `cups` as arguments and is doing the necessary calculations to check if it can make the coffee.
* Function `take_money` that empties the cash in the machine
* Function `switch_state` that turns the machine on/off. On by default
* Function `fill_machine` that fills the machine with the passed arguments with the following order: water, milk, beans, money, cups

Also the employee can print the machine ingredient status at any time by printing
the object itself

Finally, there is a `main` function that simulates the whole process of a client and a coffee machine and an employee with descriptive actions.

# Markdown generator module

The project also comes with a simple custom module that generates a README.md file based on the markdown format that you input.
#### Available format types:

1. Plain text function `plain` that adds plain text and new line if it exceeds 78 characters
2. Bold text function `bold` that makes a text bold
3. Italic text function `italic` that makes a text italic
4. Header function `header` that makes a text a header. The function asks for the Level of the heading then it validates it and applies it.
5. Link function `link` that asks for a label for the url and then for a url and it places it in ()
6. Inline code `inline_code` function that makes a text appear as code
7. New line function `new_line` that adds a new_line
8. Unordered list function `unordered_list` that prompts for the number of bullets/rows and then asks each row value seperately.
9. Ordered list function `ordered_list` that is same as `unordered_list` but it uses numbering instead of bullets.

New line is necessary if we want to add a new line because we dont know if the
user wants a new line between each input, except for the 8. and 9. functions that are adding a new line by themselves for every row
#### Main function:

* Asks for a user action by using indexes based on the index of formatter. For example if a user wants a plain text he must input `1`
* Validates the action and asks for the text. When the user inputs the text, it appends the text to a separate list and then it repeats the process.
* If the user inputs `!done`, a file named `README.md` is created in the same folder of the project with all the values written on it and then the program terminates. The write_mode is appending.

Finally, this markdown was generated with the `markdown_generator.py` module.
