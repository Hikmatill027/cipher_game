import number_guesser.art as art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrype:\n")
    text = input("Type your message here:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    def ceasar(beginning_text, cipher_direction, shift_amount):
        end_text = ''
        if direction == 'decode':
            shift_amount *= -1
        for char in beginning_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d code is: {end_text}")

    ceasar(beginning_text=text, cipher_direction=direction, shift_amount=shift)
    
    continuation = input("Type 'yes' if want to restart, otherwise 'no'\n").lower().strip()
    if continuation == "no":
        should_continue = False
        print("Goodbye!")