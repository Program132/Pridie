import itertools


def add_information(listOfInfo):
    info = input("Enter information: ")
    listOfInfo.append(info)
    print("Information added successfully!\n")
    return listOfInfo


def mixedListGenerator(currentList):
    replacements = {
        'a': '@',
        'e': '3',
        'h': '#',
        't': '7',
        'o': '0',
        'l': '|',
        's': '$',
        'i': '1',
        'g': '9',
        'z': '2',
        'b': '8',
        'c': '(',
        'd': '|)',
        'f': 'ph',
        'k': '|<',
        'm': '|\\/|',
        'n': '|\\|',
        'u': '|_|',
        'v': '\\/',
        'x': '><',
        'y': '`/',
        'w': '\\/\\/',
        'r': '|2',
        'j': '_|',
        'q': 'kw',
        'p': '|*',
        ',': '<',
        '.': '>',
        ';': ':',
        ':': ';',
        "'": '`',
        '"': '``',
        '(': ')',
        ')': '(',
        '{': '}',
        '}': '{',
        '[': ']',
        ']': '[',
        '<': ',',
        '>': '.',
        '?': '?!',
        '!': '!!',
        '@': '^',
        '#': '~',
        '$': '€',
        '%': '‰',
        '&': '+',
        '*': '_',
        '+': '&',
        '=': '≠',
        '-': '_',
        '_': '-',
        '/': '\\',
        '\\': '/',
        '|': '¦',
        '`': "'",
    }

    newList = []
    for i in range(len(currentList)):
        item = currentList[i].lower()
        variations = [item]
        item_without_spaces = ''.join(item.split())
        if item_without_spaces != item:
            variations.append(item_without_spaces)

        for char in item:
            if char.lower() in replacements:
                temp_variations = []
                for variant in variations:
                    temp_variations.append(variant.replace(char, replacements[char.lower()]))
                variations.extend(temp_variations)
        variations.extend([variant.upper() for variant in variations])
        variations.extend([prev + item for prev in currentList[:i]])

        newList.extend(variations)

    return newList


def save_and_get_dict(listOfInfo):
    mixedList = mixedListGenerator(listOfInfo)
    filename = input("Enter the name of the file to save the dictionary: ") + ".txt"
    file = open(filename, "w+")
    for i in mixedList:
        file.write(i)
        file.write("\n")
    file.close()
    return


def main():
    listOfInfo = []
    while True:
        print("Select the number:")
        print("1: Add information")
        print("2: Save and get the dict file")
        print("3: Quit/Cancel")

        choice = input()

        if choice == '1':
            listOfInfo = add_information(listOfInfo)
        elif choice == '2':
            save_and_get_dict(listOfInfo)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
