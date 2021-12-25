# encrypt: CLI for encrypting files. 
### About 
encrypt is a simple command-line-interface for password protected 256-bit file encryption.
Alternative to jodding down passwords or private information in a standard notes app! Encrypt allows encryption
of plain text with a plain & easy interface. 

## Installation
Just install through `pip >= 21.2.4` with `python >= 3.9`.
```
pip install encrypt
```

## Usage
encrypt offers 2 commands `encrypt` & `decrypt`. 

### encrypt
Given a file - text.txt, for example - it can be encrypted using the following command: 
```
encrypt path/to/file/text.txt
```
The user will be prompted for a password, which will later be used to decrypt the file!
The original - text.txt - will be replaced by a file with encrypted content named text.enc.
To specify a custom output file use the `--w` tag:
```
encrypt path/to/file/text.txt --w path/to/encrypted_file/encrypted_text.enc
```
To keep the original file, append the `-l` tag.

### decrypt
To decrypt an encrypted file use the following command:
```
decrypt path/to/file/text.enc
```
The user will be prompted for the password used to encrypt the file. 
The encrypted file is then replaced by a file with encrypted content named text.txt.
To print the decrypted content of the file without creating a new file/replacing the encrypted file,
append the `-v` tag. This tag is incompatible with unix piping unless the password is specified in the command:
```
decrypt path/to/file/text.enc -v --password=... | less
```
Similar to the `encrypt` command, the `-l` & `--w` tags have the same function. 


## TODO
* Test on images and other file formats