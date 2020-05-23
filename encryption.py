ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()
    
    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index+KEY)%len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
        
    return cipher_text
    
pt = "this is a message"
ct = caesar_encrypt(pt)
print(ct)