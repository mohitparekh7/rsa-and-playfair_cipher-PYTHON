# import sympy as sp
from tkinter import *


def rsaExecute():
    print("In RSA")

def runPFEncryption():
    print("Encrypting Playfair..........")

def encryptPlayfair():
    global encryptPlayfairWindow
    encryptPlayfairWindow = Tk()
    encryptPlayfairWindow.title('Encrypt')

    l1 = Label(encryptPlayfairWindow, text='Key:')
    l1.grid(row=1,column=1)
    l2 = Label(encryptPlayfairWindow, text='Message:')
    l2.grid(row = 2, column = 1)

    key_text = StringVar()
    e1 = Entry(encryptPlayfairWindow, textvariable=key_text)
    # e1 = Entry(encryptPlayfairWindow)
    e1.grid(row=1,column=2)
    key = key_text.get()

    message_text = StringVar()
    e2 = Entry(encryptPlayfairWindow, textvariable=message_text)
    e2.grid(row=2,column=2)

    b1 = Button(encryptPlayfairWindow,text='Submit',width=12,pady=5,command = runPFEncryption)
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
