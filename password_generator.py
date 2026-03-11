import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    # Add letters (a-z, A-Z)
    if use_letters:
        characters += string.ascii_letters

    # Add numbers (0-9)
    if use_numbers:
        characters += string.digits

    # Add symbols (!@#$ etc.)
    if use_symbols:
        characters += string.punctuation

    # If no character type selected
    if not characters:
        return "Error: Please select at least one character type!"

    # Generate random password
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# ---- Main Program ----
print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

letters = input("Include letters? (yes/no): ").lower() == "yes"
numbers = input("Include numbers? (yes/no): ").lower() == "yes"
symbols = input("Include symbols? (yes/no): ").lower() == "yes"

password = generate_password(length, letters, numbers, symbols)

print("\nGenerated Password:", password)