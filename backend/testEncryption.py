from encryption import *

def main():
    print("Generating keys")
    publicCombo, privateCombo = generateKeys()
    n, e = publicCombo
    d, e = privateCombo
    print("Public key: ", e, " Private key: ", d, " E value: ", n)
    message = input("Enter a message to encrypt: ")
    encrypted = encrypt(e, n, message)
    print("Encrypted message: ", encrypted)
    decrypted = decrypt(d, n, encrypted)
    print("Decrypted message: ", decrypted)

if __name__ == '__main__':
    main()