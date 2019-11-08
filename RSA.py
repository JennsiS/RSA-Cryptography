#Universidad del Valle de Guatemala
#Matemática discreta
#Sección: 10
#Jennifer Sandoval  18962
#Esteban del Valle  18221
#Luis Quezada		18028

import random

def isPrime(num):
    for i in range(2,(num)):
        if (num%i == 0):
            return False   
    return True

letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}


#Crear funcion que genere un numero primo de la longitud de bits que se requiera
#numero=(randint(10000,50000))
#primo=False
#while (primo==False):
  # primo=primalidad(numero)
   # if (primo==True):
    #    num=numero
     #   break
        