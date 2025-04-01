def caesar_encrypt(message, shift):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():
            # Shift within uppercase or lowercase letters
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            # If it's not a letter, we don't change it (punctuation, spaces, etc.)
            encrypted_message += char

    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    
    for char in encrypted_message:
        if char.isalpha():
            # Shift within uppercase or lowercase letters
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            # If it's not a letter, we don't change it (punctuation, spaces, etc.)
            decrypted_message += char

    return decrypted_message

def main():
    print("Caesar Cipher Program")
    
    while True:
        # Ask the user for the type of operation
        operation = input("Would you like to (E)ncrypt or (D)ecrypt? (or Q to quit): ").upper()
        
        if operation == 'Q':
            print("Exiting the program.")
            break
        
        if operation not in ['E', 'D']:
            print("Invalid choice. Please choose either 'E' to Encrypt or 'D' to Decrypt.")
            continue
        
        # Get the message and shift value from the user
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if operation == 'E':
            # Encrypt the message
            encrypted = caesar_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted}")
        
        elif operation == 'D':
            # Decrypt the message
            decrypted = caesar_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
