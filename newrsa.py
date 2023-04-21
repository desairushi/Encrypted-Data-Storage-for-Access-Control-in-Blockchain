from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def generate_keys():

    keyPair = RSA.generate(1024)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

    return pubKeyPEM ,privKeyPEM


def load_keys(public ,private):

    public_key= public.decode()
    private_key= private.decode()
    return public_key, private_key
    
def import_public(public_key):
    
    pub=RSA.import_key(public_key.encode())
    return pub

def import_private(private_key):
    
    private_key=private_key.encode()
    priv=RSA.import_key(private_key)
    return priv


def encrypt_message(public_key, message):

    encryptor = PKCS1_OAEP.new(public_key)
    message=message.encode()
    encrypted = encryptor.encrypt(message)
    #print("Encrypted:", binascii.hexlify(encrypted))
    encrypted = binascii.hexlify(encrypted)
    cipher=encrypted.decode()
    return cipher


def decrypt(private_key, cipher):
    
    decryptor = PKCS1_OAEP.new(private_key)
    prl=binascii.unhexlify(cipher)
    decrypted = decryptor.decrypt(prl).decode('utf-8')
    return decrypted



