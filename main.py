def encoder():
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!\n")
    encoded = ""
    for char in password:
        encoded += str(int(char) + 3)
    return encoded

def decoder(password):
    pass

def main():
    while True:
        print ("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu = int(input("Please enter an option: "))
        if menu == 1:
            password = encoder()
        elif menu == 2:
            decoder(password)
        elif menu == 3:
            break

if __name__ == "__main__":
    main()