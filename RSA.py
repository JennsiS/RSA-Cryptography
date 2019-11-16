"""
Universidad del Valle de Guatemala
Matematica discreta
Seccion: 10
Luis Quezada       18028
Jennifer Sandoval  18962
Esteban del Valle  18221
"""

import random

# Para determinar si es primo (advertencia: tiene gran costo computacional con numeros grandes)
def isPrime(num):
    for i in range(2,(num)):
        if (num%i == 0):
            return False   
    return True

# Algoritmo de euclides
def gcd(a,b): 
    if b == 0: 
        return a 
    else: 
        return gcd(b,a % b)

# Algoritmo de euclides extendido
def gcdExt(a, b):
    x, coefX = 0, 1
    y, coefY = 1, 0

    while (b != 0):
        quot = a // b
        a, b = b, a - quot * b
        coefX, x = x, coefX - quot * x
        coefY, y = y, coefY - quot * y
    return a, coefX, coefY

# Generador de claves publicas y privadas
def getKeys():
        # seleccion de primos (los numeros 100 y 200 pueden editarse para aumentar la seguridad del cifrado)
        # estos indican el rango de lineas de 'primes.txt' del que se seleccionaran los primos
        r1 = random.randint(100, 200)
        r2 = random.randint(100, 200)

        # importar los primos como una lista
        primesFile = open('primes.txt', 'r')
        allPrimes = primesFile.read().splitlines()
        primesFile.close()

        # asignar los primos seleccionados
        prime1 = int(allPrimes[r1])
        prime2 = int(allPrimes[r2])

        # encontrar n y la clave publica (e)
        n = prime1 * prime2
        phiOfN = (prime1-1) * (prime2-1) # phi
        
        # Se calcula la clave publica
        # Es requisito que la clave publica sea coprimo (gcd == 1) con el resultante de phi (p-1)(q-1)
        while (True):
            e = random.randrange(2, phiOfN)
            if (gcd(e,phiOfN) == 1):
                break

        # determinar si e*d = 1 (mod phiOfN) primos relativos
        a, x, y = gcdExt(e, phiOfN)

        # Se calcula la clave privada
        # la clave privada (d) debe ser positiva como requisito
        if (x < 0):
            d = x + phiOfN
        else:
            d = x
        return [n, e, d] # claves: [n,publica,privada]

def encrypt(msg,n,e):
    # la encripcion se realiza agrupando en letras de 2 en 2 

    # Se convierte n y e a tipo 'int'
    n = int(n)
    e = int(e)

    encryptedBlocks = [] # array que guarda los pares de letras encriptados
    textASCII = -1 

    # convertir a ASCII por bloques 
    if (len(msg) > 0):
        textASCII = ord(msg[0]) # se utiliza ord() para convertir las letras a una clave numerica

    for i in range(1, len(msg)):
        if (i%2 == 0): # cada 2 letras se encripta
            encryptedBlocks.append(textASCII)
            textASCII = 0
        # mult por 1000 para correr crifras 3 veces (cantidad de digitos maxima)
        textASCII = textASCII * 1000 + ord(msg[i])
    encryptedBlocks.append(textASCII)

    # encriptar cada bloque del tamanio establecido al elevar a 'e' en mod n
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str((encryptedBlocks[i]**e) % n)

    # unir todos los bloques como un string con el msg encriptado
    encryptedMsg = " ".join(encryptedBlocks)
    return encryptedMsg


def decrypt(encryptedMsg,n,d):

    n = int(n)
    d = int(d)

    # separar los bloques
    allblocks = encryptedMsg.split(' ')
    intBlocks = []

    # regresar a valores numericos (enteros)
    for k in allblocks:
        intBlocks.append(int(k))

    msg = ""

    # convertir los numeros a letras
    for i in range(len(intBlocks)):
        # se decripta elevando los numeros a ^d en mod n
        intBlocks[i] = (intBlocks[i]**d) % n

        block = ""
        
        # revertir cada bloque (de tamanio 2) de ASCII a letras y concatenar en msg
        for c in range(2):
            block = chr(intBlocks[i] % 1000) + block
            intBlocks[i] //= 1000
        msg += block
    return msg


'''
_______________________________________________________________
                              MAIN
'''

print('\n||| CRYPT0GRAFIA RSA ||| \n 1. Generar claves \n 2. Encriptar \n 3. Decriptar')

# opciones del menu
options = ['1','2','3']
command = "nan" # contiene la opcion seleccionada

while (command not in options):
    command = input("\n>> Proceso a realizar? <1 / 2 / 3>: ")


# Opcion 1 para generar las llaves y se muestra el 'n' tambien
if command == '1':
    keys = getKeys() # claves: [n,publica,privada]
    print('\nn: {}\nClave Publica: {}\nClave Privada: {}\n'.format(keys[0],keys[1],keys[2]))

# Opcion 2 para encriptar un mensaje, requiere un 'n' y la clave publica (es la que tienen todas las personas)
if command == '2':
    msg = input("\nMSG: ")
    n = input("n: ")
    e = input("Clave publica: ")
    print("Encriptando...")
    print('>> MSG encriptado: {}\n'.format(encrypt(msg,n,e)))

# Opcion 3 para decriptar un mensaje, requiere un 'n' y la clave privada (es la que solo sabe la persona que genero las llaves)
elif (command == '3'):
    msg = input("\nMSG: ")
    n = input("n: ")
    d = input("Clave privada: ")
    print("Desencriptando...")
    print('>> MSG desencriptado: {}\n'.format(decrypt(msg,n,d)))




