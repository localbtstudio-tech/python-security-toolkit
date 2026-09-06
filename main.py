def display_menu():
    print("-------------------------------------")
    print("|      PYTHON SECURITY TOOLKIT      |")
    print("|              V1.0                 |")
    print("-------------------------------------")

    print("1. Password Generator"pass)
    print("2. Password Strength Checker")
    print("3. Hash Generator")
    print("4. Exit")


def main():
    while True:
        display_menu()

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                print("Password Generator - Coming in V1.1")

            elif option == 2:
                print("Password Strength Checker - Coming in V1.1")

            elif option == 3:
                print("Hash Generator - Coming in V1.1")

            elif option == 4:
                print("Goodbye!")
                break

            else:
                print("Invalid option")

        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()