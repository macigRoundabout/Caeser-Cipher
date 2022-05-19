from time import sleep


def encode(message: str, shift: int) -> str:
    message = [m for m in message]
    encoded = str()

    for i in message:
        if i .isupper():
            num = (((ord(i) + shift) - 65) % 26) + 65
            encoded += chr(num)
        elif i.islower():
            num = (((ord(i) + shift) - 97) % 26) + 97
            encoded += chr(num)
        else:
            encoded += i

    return encoded


def decode(message: str, shift: int) -> str:
    shift *= -1
    return encode(message, shift)

def brute_force(message: str) -> tuple[str, int]:
    key = 0
    orig_msg = ""
    best_match = 0
    match = 0

    for shift in range(1, 27):
        match = 0
        decoded = decode(message, shift)
        result = [item for item in decoded.lower().split()]
        for item in result:
            with open("words.txt") as lines:
                for line in lines:
                    if item in line[:-1].strip():
                        match += 1
                if match > best_match:
                    best_match = match
                    orig_msg = decoded
                    key = shift
    return orig_msg, key


def options() -> tuple[str, int]:
    message = input("Type your message here: ")
    try:
        shift = int(input("Type the cipher shift here: "))
    except ValueError:
        print("Invalid option")
        sleep(2)
        main()

    return message, shift


def main():
    print("[*] Option 1: Encode message")
    print("[*] Option 2: Decode message")
    print("[*] Option 3: Brute Force")

    try:
        option = int(input("Type option number here: "))
    except ValueError:
        print("Invalid option")
        sleep(2)
        main()

    if option == 1:
        message, shift = options()
        result = encode(message, shift)
        print(result)
    elif option == 2:
        message, shift = options()
        result = decode(message, shift)
        print(result)
    elif option == 3:
        message = input("Type your message here: ")
        result, key = brute_force(message)
        print(f"Key: {key}")
        print(f"The decoded string is: \n{result}")


if __name__ == "__main__":
    main()
    
