# secret_code_generator
**1.Encoding Function (encode_message):**
Takes a message and a shift value as inputs.
Iterates through each character in the message.
Shifts alphabetic characters while ignoring non-alphabetic characters.
Uses modular arithmetic to handle wrapping around the alphabet.

**2.Decoding Function (decode_message):**
Similar to the encoding function, but shifts characters in the opposite direction.

**3.Main Menu Function (main_menu):**
Presents the user with options to encode, decode, or exit the program.
Collects user input and calls the appropriate functions based on the choice.

**4.Edge Case Handling:**
The program ignores non-alphabetic characters and properly handles shifts that go beyond the alphabet.
