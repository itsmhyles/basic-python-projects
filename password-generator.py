import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nYour generated password is: {password}")

generate_password()