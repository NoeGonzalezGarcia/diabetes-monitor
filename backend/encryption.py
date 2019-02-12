import math
import random

MAXNUM = 10000
#MINNUM must be odd
MINNUM = 1001
LOWESTN = 1000

def encrypt(key, n, message):
    text = []
    for char in message:
        i = ord(char) #character to unicode
        j = pow(i, key, n)
        text.append(j)
    return ' '.join(text)

def decrypt(key, n, message):
    text = []
    for char in message:
        i = pow(char, key, n)
        j = chr(i)
        text.append(j)
    return ''.join(text)

def generateKeys():
    k = 2
    while is_Prime(k):
        n = 1
        while n < LOWESTN:
            p1 = getLargePrime(MAXNUM)
            p2 = getLargePrime(MAXNUM)
            while p1 == p2:
                p2 = getLargePrime(MAXNUM)
            n = p1 * p2

        print("P1: ", p1)
        print("P2: ", p2)
        nn = (p1 - 1) * (p2 - 1)
    
        k = nn + 1
        
        d, e = mi2(k)

    return (n), (d, e)

def mi2(v):
    n = v
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)

    d = 1
    for x in factors:
        d *= x
    e = factors[len(factors) - 1]
    d /= e

    return int(d), int(e)

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