import string

def create_cipher(shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return str.maketrans(alphabet, shifted_alphabet)

def encrypt_file(input_file, output_file, shift):
    cipher = create_cipher(shift)
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            encrypted_line = line.lower().translate(cipher)
            outfile.write(encrypted_line)

def decrypt_file(input_file, output_file, shift):
    cipher = create_cipher(-shift)  # Use negative shift for decryption
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            decrypted_line = line.lower().translate(cipher)
            outfile.write(decrypted_line)

def main():
    while True:
        print("\n1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_file = input("Enter the name of the file to encrypt: ")
            output_file = input("Enter the name for the encrypted file: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypt_file(input_file, output_file, shift)
            print("File encrypted successfully!")
        elif choice == '2':
            input_file = input("Enter the name of the file to decrypt: ")
            output_file = input("Enter the name for the decrypted file: ")
            shift = int(input("Enter the shift value used for encryption (1-25): "))
            decrypt_file(input_file, output_file, shift)
            print("File decrypted successfully!")
        elif choice == '3':
            print("Thank you for using the encryption/decryption tool!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()