import math
import random

MAXNUM = 10000
MINNUM = 1001
LOWESTN = 1000

#https://gist.github.com/JonCooperWorks/5314103
def encrypt(key, n, message):
    #text = [chr((char) ** key) % n for char in message]
    text = [(ord(char) ** key) % n for char in message]
    return text

#https://gist.github.com/JonCooperWorks/5314103
def decrypt(key, n, message):
    #text = [chr((char) ** key) % n for char in message]
    text = [chr((char ** key) % n) for char in message]
    return ''.join(text)

def generateKeys():
    n = 1
    while n < LOWESTN:
        print("Getting prime 1")
        p1 = getLargePrime(MAXNUM)
        print("P1: ", p1)
        print("Getting prime 2")
        p2 = getLargePrime(MAXNUM)
        print("P2: ", p2)
        while p1 == p2:
            print ("P2 was equal to P1 getting new P2")
            p2 = getLargePrime(MAXNUM)
        n = p1 * p2

    nn = (p1 - 1) * (p2 - 1)
    e = random.randrange(1, nn)

    g = gcd(e, nn)
    while g != 1:
        e = random.randrange(1, nn)
        g = gcd(e, nn)

    d = multiplicative_inverse(e, nn)
        
    return (n, e), (d, e)

#https://gist.github.com/JonCooperWorks/5314103
#Used to find the private key 
def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b 
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob 
    if ly < 0:
        ly += oa
    return lx

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#https://inventwithpython.com/hacking/chapter23.html
def getLargePrime(n):
    isPrime = False
    while not isPrime:
        possibleNum = random.choice(range(MINNUM, MAXNUM, 2))
        isPrime = is_Prime(possibleNum)
    return possibleNum

def is_Prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for n in range(3, int(number ** 0.5) + 2, 2):
        if number % n == 0:
            return False
    return True

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
      
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

def main():
    print("Generating keys")
    publicCombo, privateCombo = generateKeys()
    n, e = publicCombo
    d, e = privateCombo
    print("Public key: ", n, " Private key: ", d, " E value: ", e)
    message = input("Enter a message to encrypt: ")
    encrypted = encrypt(n, e, message)
    print("Encrypted message: ", encrypted)
    decrypted = decrypt(d, e, encrypted)
    print("Decrypted message: ", decrypted)

if __name__ == '__main__':
    main()