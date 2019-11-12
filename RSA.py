"""
Universidad del Valle de Guatemala
Matematica discreta
Seccion: 10
Jennifer Sandoval  18962
Esteban del Valle  18221
Luis Quezada		18028
"""

import random, argparse

letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

# FUNCTIONS
def isPrime(num):
    for i in range(2,(num)):
        if (num%i == 0):
            return False   
    return True
  
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)

def xgcd(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
    return a, old_x, old_y

def chooseE(totient):
    while (True):
        e = random.randrange(2, totient)
        if (gcd(e, totient) == 1):
            return e

def chooseKeys():
        # choose two random numbers within the range of lines where 
        # the prime numbers are not too small and not too big
        rand1 = random.randint(100, 300)
        rand2 = random.randint(100, 300)

        # store the txt file of prime numbers in a python list
        fo = open('primes.txt', 'r')
        lines = fo.read().splitlines()
        fo.close()

        # store our prime numbers in these variables
        prime1 = int(lines[rand1])
        prime2 = int(lines[rand2])

        # compute n, totient, e
        n = prime1 * prime2
        totient = (prime1 - 1) * (prime2 - 1)
        e = chooseE(totient)

        # compute d, 1 < d < totient such that ed = 1 (mod totient)
        # e and d are inverses (mod totient)
        gcd, x, y = xgcd(e, totient)

        # make sure d is positive
        if (x < 0):
            d = x + totient
        else:
            d = x

        # write the public keys n and e to a file
        f_public = open('public_keys.txt', 'w')
        f_public.write(str(n) + '\n')
        f_public.write(str(e) + '\n')
        f_public.close()

        f_private = open('private_keys.txt', 'w')
        f_private.write(str(n) + '\n')
        f_private.write(str(d) + '\n')
        f_private.close()

def encrypt(message, file_name = 'public_keys.txt', block_size = 2):
    try:
        fo = open(file_name, 'r')

    # check for the possibility that the user tries to encrypt something
    # using a public key that is not found
    except FileNotFoundError:
        print('That file is not found.')
    else:
        n = int(fo.readline())
        e = int(fo.readline())
        fo.close()

        encrypted_blocks = []
        ciphertext = -1

        if (len(message) > 0):
            # initialize ciphertext to the ASCII of the first character of message
            ciphertext = ord(message[0])

        for i in range(1, len(message)):
            # add ciphertext to the list if the max block size is reached
            # reset ciphertext so we can continue adding ASCII codes
            if (i % block_size == 0):
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            # multiply by 1000 to shift the digits over to the left by 3 places
            # because ASCII codes are a max of 3 digits in decimal
            ciphertext = ciphertext * 1000 + ord(message[i])

        # add the last block to the list
        encrypted_blocks.append(ciphertext)

        # encrypt all of the numbers by taking it to the power of e
        # and modding it by n
        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str((encrypted_blocks[i]**e) % n)

        # create a string from the numbers
        encrypted_message = " ".join(encrypted_blocks)

        return encrypted_message

def decrypt(blocks, block_size = 2):

    fo = open('private_keys.txt', 'r')
    n = int(fo.readline())
    d = int(fo.readline())
    fo.close()

    # turns the string into a list of ints
    list_blocks = blocks.split(' ')
    int_blocks = []

    for s in list_blocks:
        int_blocks.append(int(s))

    message = ""

    # converts each int in the list to block_size number of characters
    # by default, each int represents two characters
    for i in range(len(int_blocks)):
        # decrypt all of the numbers by taking it to the power of d
        # and modding it by n
        int_blocks[i] = (int_blocks[i]**d) % n

        tmp = ""
        # take apart each block into its ASCII codes for each character
        # and store it in the message string
        for c in range(block_size):
            tmp = chr(int_blocks[i] % 1000) + tmp
            int_blocks[i] //= 1000
        message += tmp

    return message


# MAIN _______________________________________________________________

parser = argparse.ArgumentParser()
parser.add_argument('command',help='encrypt o decrypt')
args = parser.parse_args()

chooseKeys()

if (args.command == 'encrypt'):
    msg = input("MSG: ")
    print(encrypt(msg))

elif (args.command == 'decrypt'):
    msg = input("MSG: ")
    print(decrypt(msg))









