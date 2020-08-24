from random import randint
import matplotlib.pyplot as plt

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, key):
    plain_text = plain_text.upper()
    cipher_text = ''
    for index, char in enumerate(plain_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
    
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ''
    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain_text += ALPHABET[(char_index - key_index) % len(ALPHABET)]
    
    return plain_text

def random_sequence(plain_text):
    random_sequence = []
    for rand in range(len(plain_text)):
        random_sequence.append(randint(0, len(ALPHABET)))
    
    return random_sequence

def frequency_analysis (plain_text):
    plain_text = plain_text.upper()
    letter_frequency = {}
    for letter in ALPHABET:
        letter_frequency[letter] = 0
    
    for letter in plain_text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1
    
    return letter_frequency
    
def plot_distribution(letter_frequency):
    centers = range(len(ALPHABET))
    plt.bar(centers, letter_frequency.values(), align = 'center', tick_label = list(letter_frequency.keys()))
    plt.xlim([0, len(ALPHABET) - 1])
    plt.show()

if __name__ == "__main__":
    plain_text = "My name is Shubhang Gupta"
    
    print("Original message: %s" % plain_text)
    key = random_sequence(plain_text)
    cipher_text = encrypt(plain_text, key)
    print("Encrypted message: %s" % cipher_text)
    decrypted_text = decrypt(cipher_text, key)
    print("Decrypted message: %s" % decrypted_text)
    
    plot_distribution(frequency_analysis(cipher_text))