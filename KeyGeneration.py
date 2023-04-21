import rsa
import sys

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

from tkinter import Tk
from tkinter import filedialog 
root = tk.Tk()
root.withdraw()


def generate_keys():
    (pubkey,privkey) = rsa.newkeys(1024)
    with open("public.pem","wb") as f:
        f.write(pubkey.save_pkcs1("PEM"))
    with open("private.pem","wb") as f:
        f.write(privkey.save_pkcs1("PEM"))
    print("Keys are generated")

def load_keys():
    with open('public.pem') as p:
        public_key = p.read()

    with open('private.pem') as p:
        private_key = p.read()
    return public_key, private_key

def encrypt_message():

    path = filedialog.askopenfilename()
    with open(path, 'r') as f:
        f_contents = f.read()
    pass

    string = f_contents
    value = string.encode().hex()
    print("String value has been converted to " + value + ".")
    with open("public.pem","rb") as f:
        pub_key = rsa.PublicKey.load_pkcs1(f.read())  

    cipher = rsa.encrypt(value.encode(),pub_key)
    with open("encrypted.message","wb") as f:
        f.write(cipher)
    print("Encryption Successfull , Please Locate the enrypted.message file!")
    return cipher

def decrypt():

    path = filedialog.askopenfilename()
    with open(path, 'r') as f:
        f_contents = f.read()
    pass

    with open(f_contents,"rb") as f:
        cipher=f.read()

    with open("private.pem","rb") as f:
        pri_key = rsa.PrivateKey.load_pkcs1(f.read())
   
    decry=rsa.decrypt(cipher, pri_key)
    decrypted=decry.decode()
    bytes_object = bytes.fromhex(decrypted)
    string = bytes_object.decode()
    print("found hex value:" + decrypted + ".")
    with open("Decrypted.txt","w") as f:
        f.write(string)

    return decrypted

#generate_keys()
#encrypt_message()
decrypt()

