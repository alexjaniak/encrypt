# PROJECT: encrypt - encrypts text files
# AUTHOR: alexjaniak
# FILE: helper functions

# IMPORTS
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# MAIN-FUNCTIONS 
def encrypt_file(read_file: str, password: str):
    """Reads read_file, encrypts data, and writes to write_file."""

    # read text from file
    text = ""
    with open(read_file, 'r') as rfile:
        for line in rfile: text += line 

    # encrypt text
    key, salt = _get_private_key(password)
    encrypted_bytes, iv = _encrypt_bytes(text.encode('UTF-8'), key)

    return salt + iv + encrypted_bytes

def decrypt_file(read_file: str, password: str):
    """Reads read_file, decryptes bytes, and writes as text to write_file."""

    # read bytes from file
    padded_bytes = b''
    with open(read_file, 'rb') as rfile:
        salt = rfile.read(32)
        iv = rfile.read(16)
        _bytes = rfile.read(16)
        while(_bytes):
            padded_bytes += _bytes
            _bytes = rfile.read(16)

    # decrypt encrypted bytes
    key, salt = _get_private_key(password, salt)
    text = _decrypt_bytes(padded_bytes, key, iv).decode('UTF-8')
    
    return text


def new_file_ext(file_path: str, new_ext: str):
    """Returns path for file with new extention"""

    root, ext = os.path.splitext(file_path)
    return root + new_ext

# SUB-FUNCTIONS
def _encrypt_bytes(_bytes: bytes, key: bytes):
    """Encrypt bytes using 256-bit AES."""

    cipher = AES.new(key, AES.MODE_CBC) 
    _padded_bytes = pad(_bytes, AES.block_size) # pad bytes
    encrypted_bytes = cipher.encrypt(_padded_bytes) # encrypt bytes
    return encrypted_bytes, cipher.iv

def _decrypt_bytes(_bytes: bytes, key: bytes, iv: bytes) -> bytes:
    """Decrypt 256-bit AES encrypted bytes."""

    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        _decrypted_bytes = cipher.decrypt(_bytes) # decrypt bytes
        original_bytes = unpad(_decrypted_bytes, AES.block_size) # unpad bytes
        return original_bytes
    except ValueError:
        raise DecryptionError
    

def _get_private_key(password: str, salt : bytes=None):
    """Generates 32-byte key from string."""

    if salt == None: salt = get_random_bytes(32)
    _bytes = password.encode('UTF-8') # encode into bytes. 
    key = KDF.scrypt(_bytes, salt, 32, N=2**14, r=8, p=1) 
    return key, salt

# EXCEPTIONS
class DecryptionError(Exception):
    def __str__(self):
        return "Failed Decryption: Incorrect Password"


if __name__ == '__main__':
    password = "something"
    tfile = "text.txt"
    efile = new_file_ext(tfile, ".enc")

    encrypt_file(tfile, efile, password)
    decrypt_file(efile, tfile, password)
