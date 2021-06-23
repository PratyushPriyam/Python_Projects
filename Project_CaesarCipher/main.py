from art import logo


def cipher(text_txt, shift_number, direction_dir):
    encryption_text = ""
    shift_number = shift_number % 26
    if "decode" in direction_dir:
        shift_number *= -1
    for lett in text_txt:
        if lett in alphabet:
            index_of_letter = alphabet.index(lett)
            new_pos = shift_number + index_of_letter
            encryption_text += alphabet[new_pos]
        else:
            encryption_text += lett
    print(f"Your {direction_dir}d code is : {encryption_text}")


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

continue_code = True
while continue_code:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if ("encode" in direction) or ("decode" in direction):
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        cipher(text_txt=text, shift_number=shift, direction_dir=direction)
        continue_code = input("Do you wish to run the program again ?")
        if "yes" in continue_code:
            continue_code = True
        else:
            print("Terminating Program...Good Bye")
            continue_code = False
            break
    else:
        print("Invalid KEYWORD Used. Run the program again to encrypt or decrypt")
        break
