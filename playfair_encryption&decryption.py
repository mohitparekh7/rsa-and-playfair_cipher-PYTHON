key=input("Enter key ") # initializing the key
key=key.upper()
key=key.replace(" ", "")

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=[]
for ch in key: # storing the key into the matrix
    if ch not in result:
        if ch=='J':
            result.append('I')
        else:
            result.append(ch)
flag=0
for i in range(65,91): #storing all the other characters into the matrix
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))

k=0
encryptedMatrix=matrix(5,5,0) #initialize the matrix
for i in range(0,5): # creating the 5x5  matrix with the input
    for j in range(0,5):
        encryptedMatrix[i][j]=result[k]
        k+=1

def locationIndex(c): # get location of each character
    loc=[]
    if c=='J':
        c='I'
    for i ,j in enumerate(encryptedMatrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  # Encryption
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'Z'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'Z'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=[]
        loc=locationIndex(msg[i])
        loc1=[]
        loc1=locationIndex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(encryptedMatrix[(loc[0]+1)%5][loc[1]],encryptedMatrix[(loc1[0]+1)%5][loc1[1]]).lower(),end='')
        elif loc[0]==loc1[0]:
            print("{}{}".format(encryptedMatrix[loc[0]][(loc[1]+1)%5],encryptedMatrix[loc1[0]][(loc1[1]+1)%5]).lower(),end='')  
        else:
            print("{}{}".format(encryptedMatrix[loc[0]][loc1[1]],encryptedMatrix[loc1[0]][loc[1]]).lower(),end='')    
        i=i+2        
                 
def decrypt():  # Decryption
    msg=str(input("ENTER CIPHER TEXT: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT: ",end=' ')
    i=0
    while i<len(msg):
        loc=[]
        loc=locationIndex(msg[i])
        loc1=[]
        loc1=locationIndex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(encryptedMatrix[(loc[0]-1)%5][loc[1]],encryptedMatrix[(loc1[0]-1)%5][loc1[1]]).lower(),end='')
        elif loc[0]==loc1[0]:
            print("{}{}".format(encryptedMatrix[loc[0]][(loc[1]-1)%5],encryptedMatrix[loc1[0]][(loc1[1]-1)%5]).lower(),end='')  
        else:
            print("{}{}".format(encryptedMatrix[loc[0]][loc1[1]],encryptedMatrix[loc1[0]][loc[1]]).lower(),end='')    
        i=i+2        

while(1):
    print("\n1.Encryption \n2.Decryption \n3.Exit \n")
    choice = int(input("Enter your choice: "))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")