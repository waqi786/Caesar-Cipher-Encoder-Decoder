alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction = input("Type: 'encode' to encrept, and type: 'decode' to decrept: ")
text = input("Enter a message here: ").lower()
shift = int(input("Enter a shift number: "))

def encrept(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabets[new_position]
    print(f"The encode text is {cipher_text}")

def decrept(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        plain_text += alphabets[new_position]
    print(f"The decode text is {plain_text}")

if direction == "encode":
    encrept(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrept(cipher_text=text,shift_amount=shift)
