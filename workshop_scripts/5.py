def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

with open('encrypted_data/5.txt', 'r') as f:
    encrypted_data = f.read()

decoded_5 = decrypt(encrypted_data, 5)

with open('workshop_data/5.txt', 'w') as f:
    f.write(decoded_5)
