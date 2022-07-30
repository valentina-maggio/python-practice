# Caesar Cipher

from caesarart import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(action, start_text, shift_amount):
    end_text = ""
    if action == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            alphabet_position = alphabet.index(char)
            new_position = alphabet_position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {action}d text is: {end_text}\n")

should_continue = True
while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction, text, shift)

    user_choice = input("Would you like to restart the cipher program? Type 'yes' or 'no':\n")
    if user_choice == "no":
        should_continue = False
        print("Goodbye")
