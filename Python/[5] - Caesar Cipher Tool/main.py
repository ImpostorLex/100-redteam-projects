message = input("Enter your message here: ")
shift = int(input("Enter the shift number: "))

if shift > 26:
    print("Shift number must be only from 1 to 26")
else:
    encrypted_msg = ""
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

    for letter in message:
        if letter.isnumeric() or not letter.isalnum():
            encrypted_msg += letter
        elif letter.isupper():
            index = uppercase_letters.index(letter)
            encrypted_msg += uppercase_letters[(index + shift) % 26]
        elif letter.islower():
            index = lowercase_letters.index(letter)
            encrypted_msg += lowercase_letters[(index + shift) % 26]

    print(encrypted_msg)
