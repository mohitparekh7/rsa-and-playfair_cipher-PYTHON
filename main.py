import sympy as sp
from tkinter import *

# RSA KEYS
# Public Key
p = sp.randprime(30,1000)
q = sp.randprime(30,1000)
# First number in Public Key
n = p * q
phi = (p - 1) * (q - 1)
# Private Key
for e in range(2,phi):
    for i in range(1,e + 1):
        if ((phi % i == 0) and (e % i == 0)):
            gcd = i
    if gcd == 1:
        break
# Second number in Public Key
d = 0
for k in range(1,10):
    x = 1 + k * phi
    if x % e == 0:
        d = int(x / e)
        break

#Function to calculate and print the encrypted result
def runRSAEncryption(number,result):
    print(number)
    encrypted = (number ** e) % n
    result.set('Encrypted code: ' + str(encrypted) + '\n\nDetails:\nPublic Key: ' + str(n) + " & " + str(
        d) + '\nPrivate Key: ' + str(e) + '\nPhi: ' + str(phi) + '\nP: ' + str(p) + '\nQ: ' + str(q) + '\nk: ' + str(k))

#Function to make GUI window andc all function to run encrypt entered data
def encryptRSA():
    global encryptRSAWindow
    encryptRSAWindow = Tk()
    encryptRSAWindow.title('Encrypt')

    result = StringVar(encryptRSAWindow)
    l1 = Label(encryptRSAWindow,text='Number to encrypt:')
    l1.grid(row=1,column=1)
    l2 = Label(encryptRSAWindow,textvariable=result)
    l2.grid(row=2,column=1)

    mssg_text = IntVar(encryptRSAWindow)
    e1 = Entry(encryptRSAWindow,textvariable=mssg_text)
    e1.grid(row=1,column=2)

    b1 = Button(encryptRSAWindow,text='Submit',width=12,pady=5,
                command=lambda: runRSAEncryption(mssg_text.get(),result))
    b1.grid(row=5,column=5)

    encryptRSAWindow.mainloop()

#Function to calculate and print the decrypted result
def runRSADecryption(code,result):
    decrypted = (code ** d) % n
    result.set('Decrypted code: ' + str(decrypted) + '\n\nDetails:\nPublic Key: ' + str(n) + " & " + str(
        d) + '\nPrivate Key: ' + str(e) + '\nPhi: ' + str(phi) + '\nP: ' + str(p) + '\nQ: ' + str(q) + '\nk: ' + str(k))

#Function to make GUI window andc all function to run decrypt entered data
def decryptRSA():
    global decryptRSAWindow
    decryptRSAWindow = Tk()
    decryptRSAWindow.title('Encrypt')

    result = StringVar(decryptRSAWindow)
    l1 = Label(decryptRSAWindow,text='Code to decrypt:')
    l1.grid(row=1,column=1)
    l2 = Label(decryptRSAWindow,textvariable=result)
    l2.grid(row=2,column=1)

    code_text = IntVar(decryptRSAWindow)
    e1 = Entry(decryptRSAWindow,textvariable=code_text)
    e1.grid(row=1,column=2)

    b1 = Button(decryptRSAWindow,text='Submit',width=12,pady=5,
                command=lambda: runRSADecryption(code_text.get(),result))
    b1.grid(row=5,column=5)

    decryptRSAWindow.mainloop()

#Function to make GUI to give option of encrypting or decrypting
def rsaExecute():
    print("In RSA")
    t.destroy()
    global rsaWindow
    rsaWindow = Tk()
    rsaWindow.title('RSA')

    encryptionButton = Button(text='Encrypt',command=encryptRSA,width=50,height=5)
    decryptionButton = Button(text='Decrypt',command=decryptRSA,width=50,height=5)
    backButton = Button(text='Back',command=backToStartRSA,width=50,height=5)
    encryptionButton.grid(column=1,row=1)
    decryptionButton.grid(column=1,row=2)
    backButton.grid(column=1,row=3)

#Function to destroy RSA window and go back to start window
def backToStartRSA():
    rsaWindow.destroy()
    start()


def matrix(x,y,initial):
    return [ [ initial for i in range(x) ] for j in range(y) ]


def locationIndex(c,encryptedMatrix):  # get location of each character
    #     print("IN location Index")
    loc = [ ]
    if c == 'J':
        c = 'I'
    for i,j in enumerate(encryptedMatrix):
        #         print("IN location Index ,first for")
        for k,l in enumerate(j):
            #             print("IN location Index ,second for")
            if c == l:
                #                 print("in location index , in if")
                #                 print(loc)
                loc.append(i)
                loc.append(k)
                #                 print(loc)
                return loc


def runPFEncryption(key,msg,output):
    print("Encrypting Playfair..........")

    key = key.upper()
    key = key.replace(" ","")

    result = [ ]
    for ch in key:  # storing the key into the matrix
        if ch not in result:
            if ch == 'J':
                result.append('I')
            else:
                result.append(ch)
    flag = 0
    for i in range(65,91):  # storing all the other characters into the matrix
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    k = 0
    encryptedMatrix = matrix(5,5,0)  # initialize the matrix
    for i in range(0,5):  # creating the 5x5  matrix with the input
        for j in range(0,5):
            encryptedMatrix[ i ][ j ] = result[ k ]
            k += 1

    msg = msg.upper()
    msg = msg.replace(" ","")
    print(key,msg)

    i = 0
    for s in range(0,len(msg) + 1,2):
        if s < len(msg) - 1:
            if msg[ s ] == msg[ s + 1 ]:
                msg = msg[ :s + 1 ] + 'Z' + msg[ s + 1: ]
    if len(msg) % 2 != 0:
        msg = msg[ : ] + 'Z'
    print("CIPHER TEXT:",end=' ')
    ans = ''
    while i < len(msg):
        loc = [ ]
        loc = locationIndex(msg[ i ],encryptedMatrix)
        loc1 = [ ]
        loc1 = locationIndex(msg[ i + 1 ],encryptedMatrix)
        if loc[ 1 ] == loc1[ 1 ]:
            ans = ans + encryptedMatrix[ (loc[ 0 ] + 1) % 5 ][ loc[ 1 ] ] + encryptedMatrix[ (loc1[ 0 ] + 1) % 5 ][
                loc1[ 1 ] ]
        #             print("{}{}".format(encryptedMatrix[(loc[0]+1)%5][loc[1]],encryptedMatrix[(loc1[0]+1)%5][loc1[1]]).lower(),end='')
        elif loc[ 0 ] == loc1[ 0 ]:
            ans = ans + encryptedMatrix[ loc[ 0 ] ][ (loc[ 1 ] + 1) % 5 ] + encryptedMatrix[ loc1[ 0 ] ][
                (loc1[ 1 ] + 1) % 5 ]
        #             print("{}{}".format(encryptedMatrix[loc[0]][(loc[1]+1)%5],encryptedMatrix[loc1[0]][(loc1[1]+1)%5]).lower(),end='')
        else:
            ans = ans + encryptedMatrix[ loc[ 0 ] ][ loc1[ 1 ] ] + encryptedMatrix[ loc1[ 0 ] ][ loc[ 1 ] ]
        #             print("{}{}".format(encryptedMatrix[loc[0]][loc1[1]],encryptedMatrix[loc1[0]][loc[1]]).lower(),end='')
        i = i + 2
    print(ans)
    output.set(ans)


def runPFDecryption(key,msg,output):
    print("Decrypting Playfair..........")

    key = key.upper()
    key = key.replace(" ","")

    result = [ ]
    for ch in key:  # storing the key into the matrix
        if ch not in result:
            if ch == 'J':
                result.append('I')
            else:
                result.append(ch)
    flag = 0
    for i in range(65,91):  # storing all the other characters into the matrix
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    k = 0
    encryptedMatrix = matrix(5,5,0)  # initialize the matrix
    for i in range(0,5):  # creating the 5x5  matrix with the input
        for j in range(0,5):
            encryptedMatrix[ i ][ j ] = result[ k ]
            k += 1

    msg = msg.upper()
    msg = msg.replace(" ","")
    print(key,msg)

    i = 0
    print("PLAIN TEXT:",end=' ')
    ans = ''
    while i < len(msg):
        loc = [ ]
        loc = locationIndex(msg[ i ],encryptedMatrix)
        loc1 = [ ]
        loc1 = locationIndex(msg[ i + 1 ],encryptedMatrix)
        if loc[ 1 ] == loc1[ 1 ]:
            ans = ans + encryptedMatrix[ (loc[ 0 ] - 1) % 5 ][ loc[ 1 ] ] + encryptedMatrix[ (loc1[ 0 ] - 1) % 5 ][
                loc1[ 1 ] ]
        #             print("{}{}".format(encryptedMatrix[(loc[0]-1)%5][loc[1]],encryptedMatrix[(loc1[0]-1)%5][loc1[1]]).lower(),end='')
        elif loc[ 0 ] == loc1[ 0 ]:
            ans = ans + encryptedMatrix[ loc[ 0 ] ][ (loc[ 1 ] - 1) % 5 ] + encryptedMatrix[ loc1[ 0 ] ][
                (loc1[ 1 ] - 1) % 5 ]
        #             print("{}{}".format(encryptedMatrix[loc[0]][(loc[1]-1)%5],encryptedMatrix[loc1[0]][(loc1[1]-1)%5]).lower(),end='')
        else:
            ans = ans + encryptedMatrix[ loc[ 0 ] ][ loc1[ 1 ] ] + encryptedMatrix[ loc1[ 0 ] ][ loc[ 1 ] ]
        #             print("{}{}".format(encryptedMatrix[loc[0]][loc1[1]],encryptedMatrix[loc1[0]][loc[1]]).lower(),end='')
        i = i + 2
    #     print(ans)
    output.set(ans)


def decryptPLayfair():
    global decryptPlayfairWindow
    decryptPlayfairWindow = Tk()
    decryptPlayfairWindow.title('Decrypt')

    output = StringVar(decryptPlayfairWindow)
    l1 = Label(decryptPlayfairWindow,text='Key:')
    l1.grid(row=1,column=1)
    l2 = Label(decryptPlayfairWindow,text='Message:')
    l2.grid(row=2,column=1)
    l3 = Label(decryptPlayfairWindow,textvariable=output)
    l3.grid(row=3,column=1)

    key_text = StringVar(decryptPlayfairWindow)
    e1 = Entry(decryptPlayfairWindow,textvariable=key_text)
    e1.grid(row=1,column=2)

    message_text = StringVar(decryptPlayfairWindow)
    e2 = Entry(decryptPlayfairWindow,textvariable=message_text)
    e2.grid(row=2,column=2)

    b1 = Button(decryptPlayfairWindow,text='Submit',width=12,pady=5,
                command=lambda: runPFDecryption(key_text.get(),message_text.get(),output))
    b1.grid(row=5,column=5)

    decryptPlayfairWindow.mainloop()


def encryptPlayfair():
    global encryptPlayfairWindow
    encryptPlayfairWindow = Tk()
    encryptPlayfairWindow.title('Encrypt')

    output = StringVar(encryptPlayfairWindow)
    l1 = Label(encryptPlayfairWindow,text='Key:')
    l1.grid(row=1,column=1)
    l2 = Label(encryptPlayfairWindow,text='Message:')
    l2.grid(row=2,column=1)
    l3 = Label(encryptPlayfairWindow,textvariable=output)
    l3.grid(row=3,column=1)

    key_text = StringVar(encryptPlayfairWindow)
    e1 = Entry(encryptPlayfairWindow,textvariable=key_text)
    e1.grid(row=1,column=2)

    message_text = StringVar(encryptPlayfairWindow)
    e2 = Entry(encryptPlayfairWindow,textvariable=message_text)
    e2.grid(row=2,column=2)

    b1 = Button(encryptPlayfairWindow,text='Submit',width=12,pady=5,
                command=lambda: runPFEncryption(key_text.get(),message_text.get(),output))
    b1.grid(row=5,column=5)

    encryptPlayfairWindow.mainloop()


def playfairExecute():
    print("In PLayfair")
    t.destroy()
    global playfairWindow
    playfairWindow = Tk()
    playfairWindow.title('Playfair')

    encryptionButton = Button(text='Encrypt',command=encryptPlayfair,width=50,height=5)
    decryptionButton = Button(text='Decrypt',command=decryptPLayfair,width=50,height=5)
    backButton = Button(text='Back',command=backToStartPF,width=50,height=5)
    encryptionButton.grid(column=1,row=1)
    decryptionButton.grid(column=1,row=2)
    backButton.grid(column=1,row=3)

    playfairWindow.mainloop()


def backToStartPF():
    playfairWindow.destroy()
    start()

def start():
    global t
    t = Tk()
    t.title('Cryptography')
    t.resizable(width = False  , height = True)

    rsa_button = Button(text = 'RSA',command= rsaExecute, width = 50 , height = 5 )
    playfair_button = Button(text = 'PlayFair',command = playfairExecute, width = 50 , height = 5)
    rsa_button.grid(column = 1 , row =  1)
    playfair_button.grid(column = 1, row = 2)

    t.mainloop()

start()
