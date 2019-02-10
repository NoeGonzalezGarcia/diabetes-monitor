import math
import random

MAXNUM = 1000000
LOWESTN = 1000

#https://gist.github.com/JonCooperWorks/5314103
def encrypt(key, n, message):
    text = [chr((char) ** key) % n for char in message]
    return text

#https://gist.github.com/JonCooperWorks/5314103
def decrypt(key, n, message):
    text = [chr((char) ** key) % n for char in message]
    return ''.join(text)

def generateKeys():
    n = 1
    while n < LOWESTN:
        p1 = getLargePrime(MAXNUM)
        p2 = getLargePrime(MAXNUM)
        while p1 == p2:
            p2 = getLargePrime(MAXNUM)
        n = p1 * p2

    nn = (p1 - 1) * (p2 - 1)
    e = random.randrange(1, nn)

    g = gcd(1, nn)
    while g != 1:
        e = random.randrange( 1, nn)
        g = gcd(e, nn)

    d = multiplicative_inverse(e, nn)
        
    return n, e, d

#https://gist.github.com/JonCooperWorks/5314103
#Used to find the private key 
def multiplicative_inverse(e, nn):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_nn = nn

    while e > 0:
        temp 1 = temp_nn / e
        temp2 = temp_nn - temp1 * e
        temp_nn = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y2
        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_nn == 1
    return d + nn

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#https://inventwithpython.com/hacking/chapter23.html
def getLargePrime(n):
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        pointer = i * 2
        while pointer < n:
            sieve[pointer] = False
            pointer += 1

    primes = []
    for i in range(n):
        if sieve[i] == True:
            primes.append(i)

    return random.choice(primes)

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