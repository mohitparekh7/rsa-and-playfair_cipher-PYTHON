import sympy as sp

#Public Key
p=sp.randprime(30,100)
q=sp.randprime(30,100)
#First number in Publc Key
n=p*q
phi=(p-1)*(q-1)

#Private Key
for e in range(2,phi):
    for i in range(1, e + 1):
        if ((phi % i == 0) and (e % i == 0)):
            gcd = i
    if gcd== 1:
        break

#Second number in Public Key
d=0
for k in range(1,10):
    x = 1 + k*phi
    if x % e == 0:
        d = int(x/e)
        break

#Input
data=int(input("Enter number to encrypt:"))

#Encryption
encrypted=(data**e)%n
print("\nEncrypted Message:",encrypted)

#Decryption
decrypted=int((encrypted**d)%n)
print("\nDecrypted Message:",decrypted)

print("\nDetails:")
print("Public Key:",n,"&",d)
print("Private Key:",e)
print("Phi:",phi,"\nP:",p,"\nQ:",q,"\nk:",k)
