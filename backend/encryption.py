import math
import random

MAXNUM = 1000000
LOWESTN = 1000

def encrypt(key, message):
    return ''

def decrypt(key, message):
    return ''

def generateKeys():
    n = 1
    while n < LOWESTN:
        p1 = getLargePrime(MAXNUM)
        p2 = getLargePrime(MAXNUM)
        while p1 == p2:
            p2 = getLargePrime(MAXNUM)
        n = p1 * p2

    nn = lcm(p1 - 1, p2 - 1)
    e = 3

    #This is not how you make a private key. The internet is confusing me.
    d = math.pow(e, -1)%nn
        
    return n, e, d

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