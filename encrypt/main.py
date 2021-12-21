# PROJECT: encrypt - encrypts text files
# AUTHOR: alexjaniak
# FILE: Main project file. Parses arguments from command line.

# IMPORTS
from encrypt.utils import *
import click 

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.password_option()
def encrypt(file_path, password):
    """Encrypt file with password protected AES-256"""
    write_path = new_file_ext(file_path, ".enc")
    encrypt_file(file_path, write_path, password)
    os.remove(file_path)

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.password_option()
def decrypt(file_path, password):
    """Decrypt password protected AES-256 encrypted file"""
    write_path = new_file_ext(file_path, ".txt")
    decrypt_file(file_path, write_path, password)
    os.remove(file_path)