# workshop_scripts/2.py

def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

def main():
    input_path = "../encrypted_data/2.txt"
    output_path = "../workshop_data/2.txt"
    key = 2 # Assigned key

    # Read the encrypted file
    with open(input_path, "r") as f:
        encrypted_text = f.read()

    # Decrypt
    decrypted_text = decrypt(encrypted_text, key)

    # Write decrypted output
    with open(output_path, "w") as f:
        f.write(decrypted_text)
    print(f"Decryption complete! Output written to {output_path}")

if __name__ == "__main__":
    main()
