# Assignment 4: error handling


if __name__=="__main__":
    while True:
        number_1 = input("number 1: ")
        number_2 = input("number 2: ")

        try:
            result = int(number_1) / int(number_2)
            print("division: ", result)
            break

        except ValueError as e:
            print("\n", f"[-] please enter a number not a string", "\n")

        except ZeroDivisionError as e:
            print("\n", f"[-] Error occured you cannot divide a number by zero", "\n")

    print("\n", "[+] Thank you for using this program", "\n")
