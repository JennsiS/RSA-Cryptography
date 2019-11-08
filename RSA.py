#Universidad del Valle de Guatemala
#Matemática discreta
#Sección: 10
#Jennifer Sandoval  18962
#Esteban del Valle  18221
#Luis Quezada		18028

from random import *

def primalidad (num):
    for i in range (2,(num-1)):
        if ((num%i)==0):
            return False
            break   
    return True


#Crear funcion que genere un numero primo de la longitud de bits que se requiera
#numero=(randint(10000,50000))
#primo=False
#while (primo==False):
  # primo=primalidad(numero)
   # if (primo==True):
    #    num=numero
     #   break
        

