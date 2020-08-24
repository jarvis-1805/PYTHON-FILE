ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caeser_decrypt(cipher_text):
    plain_text = ''
    
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index-KEY)%len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
        
    return plain_text

ct = "WKLVCLVCDQCH DPSOH"
pt = caeser_decrypt(ct)
print(pt)