import secrets
import string
import hashlib


def display_menu():
    print("-------------------------------------")
    print("|      PYTHON SECURITY TOOLKIT      |")
    print("|              V1.1                 |")
    print("-------------------------------------")

    print("1. Password Generator")
    print("2. Password Strength Checker")
    print("3. Hash Generator")
    print("4. Exit")


def password_generator():
    characters = string.ascii_letters + string.digits + string.punctuation

    try:
        length = int(input("Enter password length: "))

        if length < 4 or length > 128:
            print("Length must be between 4 and 128.")
            return

        password = ""

        for i in range(length):
            password += secrets.choice(characters)

        return password

    except ValueError:
        print("Please enter a number.")


def password_strength_checker():
    password = input("Enter your password: ")

    score = 0

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for character in password:

        if character.islower():
            has_lower = True

        elif character.isupper():
            has_upper = True

        elif character.isdigit():
            has_digit = True

        else:
            has_special = True

    if len(password) >= 8:
        score += 1

    if has_lower:
        score += 1

    if has_upper:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if score <= 2:
        print("Password Strength: Weak")

    elif score <= 4:
        print("Password Strength: Medium")

    else:
        print("Password Strength: Strong")


def hash_generator():
    text = input("Enter text to hash: ")

    hash_value = hashlib.sha256(text.encode()).hexdigest()

    print("SHA-256:", hash_value)


def main():
    while True:
        display_menu()

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                password = password_generator()

                if password:
                    print("Generated Password:", password)

            elif option == 2:
                password_strength_checker()

            elif option == 3:
                hash_generator()

            elif option == 4:
                print("Goodbye!")
                break

            else:
                print("Invalid option")

        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()