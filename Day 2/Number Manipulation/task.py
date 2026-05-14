alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
        else:
            new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    print(f"The decoded text is {cipher_text}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


encrypt(original_text = text, shift_amount = shift)