alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# The alphabet is copied again to account for the letters towards the end - e.g x, y, z. If we want to encode z for example, since it's at the end of the alphabet we go back to the beginning. After z is a and so forth.
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

def encrypt_func(normal_text, shift_amount):

    encrypted_word_list = []
    for e in normal_text:
        if e in alphabet:
            position = alphabet.index(e) # This returns the position of the specified value
            new_position = position + shift_amount # This shifts the position of each letter in the word by the shift value inputed
            encrypted_word_list += alphabet[new_position] # The new letters are added to the empty list on line 5
        else:
            encrypted_word_list += e

    encrypted_word = "".join(encrypted_word_list) # This converts the letters in the list to one whole string
    print(f"The encrypted text is {encrypted_word}.")

def decrypt_func(crypted_text, shift_amount):
    decrypted_word_list = []
    for d in crypted_text:
        if d in alphabet:
            position = alphabet.index(d)
            new_position = position - shift_amount
            decrypted_word_list += alphabet[new_position]
        else:
            decrypted_word_list += d

    decrypted_word = "".join(decrypted_word_list)
    print(f"The decrypted text is {decrypted_word}.")


print(logo)
repeat = True

while repeat == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt_func(normal_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt_func(crypted_text = text, shift_amount = shift)

    code_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if code_again == "no":
        repeat = False
        print("Goodbye!")
