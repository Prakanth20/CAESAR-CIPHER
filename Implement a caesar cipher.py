def caesar_cipher_encrypt(text, shift):
    """Encrypts the text using Caesar Cipher with a given shift value."""
    encrypted_text = ""
    
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabet characters unchanged
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypts the text using Caesar Cipher with a given shift value."""
    decrypted_text = ""
    
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabet characters unchanged
        else:
            decrypted_text += char
    
    return decrypted_text

def main():
    print("Caesar Cipher Encryption & Decryption")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the message
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
