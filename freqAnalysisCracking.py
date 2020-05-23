import matplotlib.pyplot as plt
LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def frequency_analysis(plain_text):
    plain_text = plain_text.upper()
    letter_frequency = {}
    for letter in LETTERS:
        letter_frequency[letter] = 0
    for letter in plain_text:
        if letter in LETTERS:
            letter_frequency[letter] += 1
    return letter_frequency
    
def plot_distribution(letter_frequency):
    centers = range(len(LETTERS))
    plt.bar(centers,  letter_frequency.values(), align="center", tick_label=list(letter_frequency.keys()))
    plt.xlim([0,len(LETTERS)-1])
    plt.show()
if __name__ == "__main__":
    plain_text = "My name is shubhang gupta studying in delhi university"
    frequencies = frequency_analysis(plain_text)
    plot_distribution(frequencies)