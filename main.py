#Used for Graphical user interface
from tkinter import *
import random
#used for binary data as printable text
import base64

root = Tk()

root.geometry("800x398")

root.title("Encrypt or Decrypt")

Tops = Frame(root, width=800, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=RIGHT)

# ==============================================


lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="Encrypt or Decrypt",
                fg="Black", bd=4, anchor='w')

lblInfo.grid(row=0, column=0)


# Initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# labels for the message
lblMsg = Label(f1, font=('arial', 13, 'bold'),
               text="MESSAGE", bd=4, anchor="w")

lblMsg.grid(row=1, column=0)
# Entry box for the message
txtMsg = Entry(f1, font=('arial', 13, 'bold'),
               textvariable=Msg, bd=4, insertwidth=2,
               bg="white", justify='center')


txtMsg.grid(row=1, column=1)
# labels for the key
lblkey = Label(f1, font=('arial', 13, 'bold'),
               text="KEY(Integer)", bd=4, anchor="w")

lblkey.grid(row=2, column=0)


# Entry box for the key
txtkey = Entry(f1, font=('arial', 13, 'bold'),
               textvariable=key, bd=4, insertwidth=2,
               bg="white", justify='center')

txtkey.grid(row=2, column=1)

# labels for the mode
lblmode = Label(f1, font=('arial', 13, 'bold'),
                text="MODE(e)(d)",
                bd=4, anchor="w")

lblmode.grid(row=3, column=0)
# Entry box for the mode
txtmode = Entry(f1, font=('arial', 13, 'bold'),
                textvariable=mode, bd=4, insertwidth=2,
                bg="white",justify='center')

txtmode.grid(row=3, column=1)

# labels for the result
lblResult = Label(f1, font=('arial', 13, 'bold'),
                  text="The Result-", bd=4, anchor="w")

lblResult.grid(row=4, column=0)

# Entry box for the result
txtResult = Entry(f1, font=('arial', 13, 'bold'),
                  textvariable=Result, bd=4, insertwidth=2,
                  bg="white", justify='center')

txtResult.grid(row=4, column=1)

# For Encryption

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# For Decryption

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():
    # print("Message= ", (Msg.get()))

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))

# exit function


def qExit():
    root.destroy()

# Function to reset the window


def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# Show message button
btnTotal = Button(f1, padx=16, pady=2, bd=4, fg="black",
                  font=('arial', 13, 'bold'), width=10,
                  text="Show Message", bg="white",
                  command=Results).grid(row=7, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=2, bd=4,
                  fg="black", font=('arial', 13, 'bold'),
                  width=10, text="Reset", bg="white",
                  command=Reset).grid(row=7, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=2, bd=4,
                 fg="black", font=('arial', 13, 'bold'),
                 width=10, text="Exit", bg="white",
                 command=qExit).grid(row=7, column=3)

# keeps window alive
root.mainloop()
