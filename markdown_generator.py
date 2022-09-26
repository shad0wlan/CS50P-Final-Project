# write your code here

def plain():
    input_text = input("Text: ")
    if len(input_text) <= 78:
        return input_text + " "
    else:
        new_text = []
        for i, j in enumerate(input_text):
            if i >=78 and i % 78 == 0:
                if j == " ":
                    new_text.append(" \n")
                    continue
            new_text.append(j)
        return "".join(new_text) + " "



def bold():
    input_text = input("Text: ")
    return f'**{input_text}** '


def italic():
    input_text = input("Text: ")
    return f'*{input_text}* '


def header():
    while True:
        try:
            input_level = int(input("Level: "))
            if input_level < 1 or input_level > 6:
                print("The level should be within the range of 1 to 6")
                continue
            break
        except ValueError:
                print("The level should be within the range of 1 to 6 in integer format")
                continue
    input_text = input("Text: ")
    return f'{"#" * int(input_level)} {input_text}\n'


def inline_code():
    input_text = input("Text: ")
    return f"`{input_text}` "


def new_line():
    return f'\n'


def link():
    input_label = input("Label: ")
    input_text = input("URL: ")
    return f'[{input_label}]({input_text}) '


def rows_checker():
    while True:
        try:
            input_rows = int(input("Number of rows: "))
            if input_rows <= 0:
                print("The number of rows should be greater than zero")
                continue
        except ValueError:
                print("The number of rows should be greater than zero in integer format")
                continue

        return input_rows


def ordered_list():
    list_array = []
    rows = rows_checker()
    for i in range(1, rows + 1):
        row = input(f'Row #{i}: ')
        list_array.append(f'{i}. {row}\n')
    return list_array


def unordered_list():
    list_array = []
    rows = rows_checker()
    for i in range(1, rows + 1):
        row = input(f'Row #{i}:')
        list_array.append(f'* {row}\n')
    return list_array



formatters = {"1": plain,  "2": bold, "3": italic, "4": header, "5": link, "6": inline_code, "7": new_line, "8": unordered_list, "9": ordered_list}

def main():
    string_saver = []
    while True:
        x = input(f"Choose a formatter by inputting its index ex. 1 for plain text:\n{' '.join([f'{i}. {formatters[i].__name__}' for i in formatters])}\n")
        if x == "!done":
            with open("README.md", "a+") as f:
                f.write("".join(string_saver))
            break
        if x not in formatters.keys():
            print("Unknown formatting type or command")
            continue
        answer = formatters[x]()
        string_saver += answer
        print("".join(string_saver))


if __name__ == "__main__":
    main()