punct_ords = [(33, 48), (58, 65), (91, 97), (123, 127)]

punctuation = []
for tup in punct_ords:
    for i in range(tup[0], tup[1]):
        punctuation.append(chr(i))

def find_rotation(ciphertext, threat_list, nonthreat_list):
    for shift in range(26):
        decipher_text = decipher(ciphertext, shift)
        matched_words = 

def match_words(text, threat_list):
    for word in text.split(' '):
        if not word.isalpha():
            word = word[:-1] # get rid of punctuation, hopefully
        

def decipher(ciphertext, shift):
    deciphered_str = ''

    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            deciphered_str += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            deciphered_str += char

    return deciphered_str

def handle_testcase():
    nonthreat_amt = int(input())
    nonthreat_list = []
    for _ in range(nonthreat_amt):
        nonthreat_list.append(input())

    threat_amt = int(input())
    threat_list = []
    for _ in range(threat_amt):
        threat_list.append(input())

    ciphertext = input()
