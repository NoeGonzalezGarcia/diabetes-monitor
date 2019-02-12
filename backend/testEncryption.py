from .encryption import *

def main():
    print("Generating keys")
    e, keyCombo = generateKeys()
    pri, pub = keyCombo
    print("Public key: ", pub, " Private key: ", pri, " E value: ", e)
    message = input("Enter a message to encrypt: ")
    encrypted = encrypt(pub, e, message)
    print("Encrypted message: ", encrypted)
    decrypted = decrypt(pri, e, encrypted)
    print("Decrypted message: ", decrypted)

if __name__ == '__main__':
    main()