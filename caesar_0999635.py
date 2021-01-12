import re
import string
import english_quadgrams

alphabet = string.ascii_letters + string.punctuation


# Display the group information
def group_info():
    return [("0999635", "Daan Kraaijeveld", "INF1I")]


# Encrypt string using the given shift
def encrypt_caesar(plaintext, shift):
    res = ''
    for char in plaintext:
        if re.match(r'[A-Za-z]', char):
            if char.isupper():
                res += alphabet[(alphabet.index(char) + shift) % 26].upper()
            else:
                res += alphabet[(alphabet.index(char) + shift) % 26]
        else:
            res += char
    return res
        

# Decrypt caesar using the given shift
def decrypt_caesar(ciphertext, shift):
    res = ''
    for char in ciphertext:
        if re.match(r'[A-Za-z]', char):
            if char.isupper():
                res += alphabet[(alphabet.index(char) - shift) % 26].upper()
            else:
                res += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            res += char
    return res
        

# Get the quadgram fitness of a given string, lower is better
def quadgram_fitness(text):
    res = 0
    text = re.sub(r'[^A-Za-z]', '', text.lower().replace(' ', ''))

    for index, char in enumerate(text):
        quadgram = text[index:index+4]

        if quadgram in english_quadgrams.quadgram_score:
            res += english_quadgrams.quadgram_score[quadgram]
        else:
            if len(quadgram) > 3:
                res += 23

    return round(res, 7)


# Get the plaintext for an encrypted ciphertext. Only output the plaintext, not the shift.
def solve_caesar(ciphertext):
    res = []
    for i in range(26):
        res.append(quadgram_fitness(decrypt_caesar(ciphertext, i)))
    return decrypt_caesar(ciphertext, res.index(min(res)))

print(solve_caesar(encrypt_caesar("Good Luck!", 7)))