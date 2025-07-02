# Assignment 2: inventory management system

import sys


def show_product(product, price):
    print("\n")
    print("[?] product: {}".format(product))
    print("[?] cost   : {}".format(price))
    print("\n")


def usage():
    print("\n", "Usage")

    print("show: show all products")
    print("show <product> : show product")
    print(
        "update <product>: update a product (create a new product if it does not exist)"
    )
    print("quit: exit the program")
    print("\n")


products = {"mango": 3000}

while (command := input(" > ")) != "quit":
    if command.lower() == "q":
        break

    parsed_command = command.split(" ")

    if len(parsed_command) > 2:
        usage()
        continue

    if parsed_command[0] == "show":
        if len(parsed_command) == 2:
            name = parsed_command[1]
            if name in products:
                show_product(name, products[name])
            else:
                print("\n", "[-] Item not in the store", "\n")

            continue

        for name, price in products.items():
            show_product(name, price)

    elif parsed_command[0] == "update":
        if len(parsed_command) == 1:
            print("\n", "[!] Invalid command for updating a store item", "\n")
            continue

        print("\n")
        name = input("[+] Enter the name of the product: ")
        price = input(f'[+] Enter the price of "{name}" added: ')

        products[name] = price
        print("[+] Success")
        print("\n")

    else:
        print("\n", "[!] Command is not supported", "\n")
        usage()
