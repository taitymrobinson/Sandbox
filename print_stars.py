def main():
    minimum_length = 6
    password = get_valid_password(minimum_length)
    print_asterisks(password)


def get_valid_password(minimum_length):
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))

main()
