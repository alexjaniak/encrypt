# PROJECT: encrypt - encrypts text files
# AUTHOR: alexjaniak
# FILE: Main project file. Parses arguments from command line.

# IMPORTS
from os import write
from click.core import V
from encrypt.utils import *
import click 

@click.command()
@click.password_option()
@click.option('--w','write_path',type=click.Path(exists=True), help="path to encrypted file")
@click.option('-l','mode', flag_value="leave", help="leave original file")
@click.argument('file_path', type=click.Path(exists=True))
def encrypt(file_path, password, write_path, mode=None):
    """Encrypts file with password protected AES-256."""
    if(not write_path):
        write_path = new_file_ext(file_path, ".enc")
        
    encrypted_bytes = encrypt_file(file_path, password)

    # write encrypted bytes to write file
    with open(write_path, 'wb') as wfile:
        wfile.write(encrypted_bytes)

    if(not mode == "leave"): # removes original file if not in 'leave' mode
        os.remove(file_path)

@click.command()
@click.password_option()
@click.option('--w','write_path',type=click.Path(exists=True), help="path to decrypted file")
@click.option('-l','mode', flag_value='leave', help="leave encrypted file")
@click.option('-v','mode', flag_value='view', help="output decrypted content - doesn't write to file")
@click.argument('file_path', type=click.Path(exists=True))
def decrypt(file_path, password, write_path, mode=None):
    """Decrypt password protected AES-256 encrypted file"""
    # create write_path if not given
    if(not write_path):
        write_path = new_file_ext(file_path, ".txt")

    decrypted_text = decrypt_file(file_path, password)

    if(mode == "view"): # checked for 'view' mode
        print(decrypted_text)
    else:
        # write text to write file
        with open(write_path, 'w') as wfile:
            wfile.write(decrypted_text)

        if(not mode == "leave"): # removes encrypted file if not in 'leave' mode
            os.remove(file_path)