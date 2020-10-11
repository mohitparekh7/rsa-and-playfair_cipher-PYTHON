import sympy as sp
from tkinter import *

#RSA KEYS
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


def runRSAEncryption(number,result):
    print(number)
    encrypted = (number ** e) % n
    result.set('Encrypted code: '+str(encrypted)+'\n\nDetails:\nPublic Key: '+str(n)+" & "+str(d)+'\nPrivate Key: '+str(e)+'\nPhi: '+str(phi)+'\nP: '+str(p)+'\nQ: '+str(q)+'\nk: '+str(k))


def encryptRSA():
    global encryptRSAWindow
    encryptRSAWindow = Tk()
    encryptRSAWindow.title('Encrypt')

    result = StringVar(encryptRSAWindow)
    l1 = Label(encryptRSAWindow, text='Number to encrypt:')
    l1.grid(row=1, column=1)
    l2 = Label(encryptRSAWindow, textvariable=result)
    l2.grid(row=2, column=1)

    mssg_text = IntVar(encryptRSAWindow)
    e1 = Entry(encryptRSAWindow, textvariable=mssg_text)
    e1.grid(row=1, column=2)

    b1 = Button(encryptRSAWindow, text='Submit', width=12, pady=5,
                command=lambda: runRSAEncryption(mssg_text.get(), result))
    b1.grid(row=5, column=5)

    encryptRSAWindow.mainloop()

def runRSADecryption(code,result):
    decrypted = (code ** d) % n
    result.set('Decrypted code: ' + str(decrypted) + '\n\nDetails:\nPublic Key: ' + str(n) + " & " + str(
        d) + '\nPrivate Key: ' + str(e) + '\nPhi: ' + str(phi) + '\nP: ' + str(p) + '\nQ: ' + str(q) + '\nk: ' + str(k))

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

def rsaExecute():
    print("In RSA")
    t.destroy()
    global rsaWindow
    rsaWindow = Tk()
    rsaWindow.title('RSA')

    encryptionButton = Button(text='Encrypt', command=encryptRSA, width=50, height=5)
    decryptionButton = Button(text='Decrypt', command=decryptRSA, width=50, height=5)
    backButton = Button(text='Back', command=backToStart, width=50, height=5)
    encryptionButton.grid(column=1, row=1)
    decryptionButton.grid(column=1, row=2)
    backButton.grid(column=1, row=3)


def runPFEncryption(key,message,output):
    print("Encrypting Playfair..........")
    print(key,message)
    output.set(message)

def encryptPlayfair():
    global encryptPlayfairWindow
    encryptPlayfairWindow = Tk()
    encryptPlayfairWindow.title('Encrypt')

    output = StringVar(encryptPlayfairWindow)
    l1 = Label(encryptPlayfairWindow, text='Key:')
    l1.grid(row=1,column=1)
    l2 = Label(encryptPlayfairWindow, text='Message:')
    l2.grid(row = 2, column = 1)
    l3 = Label(encryptPlayfairWindow, textvariable=output)
    l3.grid(row=3, column=1)

    key_text = StringVar(encryptPlayfairWindow)
    e1 = Entry(encryptPlayfairWindow, textvariable=key_text)
    e1.grid(row=1,column=2)

    message_text = StringVar(encryptPlayfairWindow)
    e2 = Entry(encryptPlayfairWindow, textvariable=message_text)
    e2.grid(row=2,column=2)

    b1 = Button(encryptPlayfairWindow,text='Submit',width=12,pady=5,command =lambda: runPFEncryption(key_text.get(),message_text.get(),output))
    b1.grid(row=5,column=5)

    encryptPlayfairWindow.mainloop()


def playfairExecute():
    print("In PLayfair")
    t.destroy()
    global playfairWindow
    playfairWindow = Tk()
    playfairWindow.title('Playfair')

    encryptionButton = Button(text = 'Encrypt',command= encryptPlayfair, width = 50 , height = 5 )
    decryptionButton = Button(text = 'Decrypt',command= backToStart, width = 50 , height = 5 )
    backButton = Button(text = 'Back',command= backToStart, width = 50 , height = 5 )
    encryptionButton.grid(column = 1 , row =  1)
    decryptionButton.grid(column = 1 , row =  2)
    backButton.grid(column = 1 , row =  3)

    playfairWindow.mainloop()

def backToStart():
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
