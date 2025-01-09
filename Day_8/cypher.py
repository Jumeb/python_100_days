alphabet = ['a', 'b', 'c', 'd', 'e', 'f' , 'g' , 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f' , 'g' , 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            end_text += alphabet[position+shift_amount]
        else:
            end_text += letter
    print(f'The {cipher_direction}d text is {end_text}')

from art import logo

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n")) % 26
    ceasar(text, shift, direction)
    continue_cipher = input("Type 'yes' if you want to go again. Other wise type 'no' \n")
    if continue_cipher == 'no':
        print('Goodbye')
        should_continue = False