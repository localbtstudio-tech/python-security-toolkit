import secrets
import string
import hashlib
import base64
import binascii
import socket
import ipaddress


def display_menu():
    print("-------------------------------------")
    print("|      PYTHON SECURITY TOOLKIT      |")
    print("|              V1.3                 |")
    print("-------------------------------------")

    print("1. Password Generator")
    print("2. Password Strength Checker")
    print("3. Hash Generator")
    print("4. File Hashing")
    print("5. Encode / Decode")
    print("6. Port Scanner")
    print("7. IP Information")
    print("8. Exit")


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


def file_hash():
    file_name = input("Enter file name: ")

    try:
        with open(file_name, "rb") as file:
            data = file.read()

        hash_value = hashlib.sha256(data).hexdigest()

        print("SHA-256:", hash_value)

    except FileNotFoundError:
        print("File not found.")


def encode_decode():
    while True:
        print("\n--- Encode / Decode ---")
        print("1. Encode")
        print("2. Decode")
        print("3. Back")

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                text = input("Enter text: ")

                encoded = base64.b64encode(
                    text.encode()
                ).decode()

                print("Encoded:", encoded)

            elif option == 2:
                text = input("Enter Base64: ")

                try:
                    decoded = base64.b64decode(
                        text
                    ).decode()

                    print("Decoded:", decoded)

                except (binascii.Error, UnicodeDecodeError):
                    print("Invalid Base64 input.")

            elif option == 3:
                break

            else:
                print("Invalid option")

        except ValueError:
            print("Please enter a number.")


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False


def scan_port(ip, port):
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()


def port_scanner():
    try:
        ip = input("Enter target IP: ")

        if not is_valid_ip(ip):
            print("Invalid IP address.")
            return

        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range.")
            return

        for port in range(start_port, end_port + 1):
            scan_port(ip, port)

    except ValueError:
        print("Please enter valid numbers for ports.")

def ip_information():
    ip = input("Enter IP address: ")

    try:
        address = ipaddress.ip_address(ip)

        print("IP Address:", address)
        print("Version:", address.version)
        print("Private:", address.is_private)
        print("Loopback:", address.is_loopback)
        print("Global:", address.is_global)

    except ValueError:
        print("Invalid IP address.")

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
                file_hash()

            elif option == 5:
                encode_decode()

            elif option == 6:
                port_scanner()
                
            elif option == 7:
                ip_information()
                
            elif option == 8:
                print("Goodbye!")
                break
            
            else:
                print("Invalid option")

        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()