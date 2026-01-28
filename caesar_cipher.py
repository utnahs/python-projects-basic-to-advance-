alphabets = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

user_choice = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
user_message = input("Type your message to:\n").lower()
shift_value = int(input("Type the shift value:\n"))


def encrypt(user_message,shift_value):
    new_message = ''
    for ch in user_message:
        if ch in alphabets:
            index_of_ch = alphabets.index(ch)
            new_index = (index_of_ch+shift_value) % 26
            new_message += alphabets[new_index]
        else:
            new_message+=ch
    print(new_message)

def decrypt(user_message,shift_value):
    new_message = ''
    for ch in user_message:
        if ch in alphabets:
            index_of_ch = alphabets.index(ch)
            new_index = (index_of_ch-shift_value) % 26
            new_message += alphabets[new_index]
        else:
            new_message+=ch
    print(new_message)




if user_choice == 'encode':
    encrypt(user_message,shift_value)
elif user_choice == 'decode':
    decrypt(user_message,shift_value)
else:
    print("Invalid Input")