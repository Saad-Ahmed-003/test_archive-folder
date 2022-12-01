alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def caesar( direction , plain_text, shift_number ):
    if direction == 'encode':
        f_out = ""
        for i in plain_text:
            out = alphabet.index(i)
            f_out += alphabet[out + shift_number]
        print(f_out)
    elif direction == 'decode':
        x_out = ""
        for i in plain_text:
            out = alphabet.index(i)
            x_out += alphabet[out - shift_number]
        print(x_out)

caesar(direction=direction, plain_text=text, shift_number=shift)
