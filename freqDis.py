import matplotlib.pyplot as pl
LETTERS = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def freq_analysis(plain_text):
    plain_text = plain_text.upper()
    letter_freq = {}
    for letter in LETTERS:
        letter_freq[letter] = 0
    for letter in plain_text:
        if letter in LETTERS:
            letter_freq[letter] += 1
    return letter_freq
def plot_dist(letter_freq):
    centers = range(len(LETTERS))
    pl.bar(
        centers,
        letter_freq.values(),
        align="center",
        tick_label=list(letter_freq.keys())
    )
    pl.xlim([0, len(LETTERS) - 1])
    pl.show()
plain_text = "Shubhang is a Nerd"
frequency = freq_analysis(plain_text)
plot_dist(frequency)