def encode_message(message, shift):
    """Encodes the given message using a Caesar cipher with the specified shift."""
    encoded = []
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encoded_char = chr((ord(char) - base + shift) % 26 + base)
            encoded.append(encoded_char)
        else:
            encoded.append(char)  # Non-letter characters are added unchanged
    return ''.join(encoded)

def decode_message(encoded_message, shift):
    """Decodes the given message using a Caesar cipher with the specified shift."""
    return encode_message(encoded_message, -shift)  # Decoding is just encoding with negative shift

def display_menu():
    """Displays the menu options for the user."""
    print("\nMenu:")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")
    
def get_shift():
    """Gets a valid shift value from the user."""
    while True:
        try:
            shift = int(input("Enter shift number: "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    """Main function to run the secret code generator."""
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            message = input("Enter the message to encode: ")
            shift = get_shift()
            encoded_message = encode_message(message, shift)
            print(f"Encoded message: {encoded_message}")

        elif choice == '2':
            encoded_message = input("Enter the message to decode: ")
            shift = get_shift()
            decoded_message = decode_message(encoded_message, shift)
            print(f"Decoded message: {decoded_message}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
