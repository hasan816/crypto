from helpers import rotate_character


def encrypt(text, rot):
    result = ''
    for item in text:
        result += rotate_character(item, rot)
    return result


def main():
    message = input("Type a message: ")
    print(message)
    rotate = int(input("Rotate by: "))
    print(encrypt(message, rotate))


if __name__ == "__main__":
    main()



