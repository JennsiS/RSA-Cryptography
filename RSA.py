'''
Universidad del Valle de Guatemala
Matemática discreta
Sección: 10
Jennifer Sandoval  18962
Esteban del Valle  18221
Luis Quezada		18028
'''

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

# MAIN _______________________________________________________________
parser = argparse.ArgumentParser()
parser.add_argument('command',help='encrypt o decrypt')
parser.add_argument('p',help='p')
parser.add_argument('q',help='q')
parser.add_argument('msg',help='Mensaje a encriptar o decriptar')
args = parser.parse_args()

# Get the data
command = args.command
p = int(args.p)
q = int(args.q)
msg = args.msg

n = p * q 
t = (p-1) * (q-1) 

for e in range(2,t): 
    if gcd(e,t)== 1: 
        break
  
for i in range(1,10): 
    x = 1 + i*t 
    if x % e == 0: 
        d = int(x/e) 
        break
ctt = Decimal(0) 
ctt =pow(no,e) 
ct = ctt % n 
  
dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 
  
print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 








