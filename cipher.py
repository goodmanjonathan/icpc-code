#!/usr/bin/env python3

# ICPC South Central USA 2014 #6793

punct_ords = [(33, 48), (58, 65), (91, 97), (123, 127)]

punctuation = ''
for tup in punct_ords:
    for i in range(tup[0], tup[1]):
        punctuation += chr(i)

def find_rotation(ciphertext, threat_list, nonthreat_list):
    max_score = {'rot': 0,
                 'score': 0,
                 'info': None}
    for shift in range(26):
        decipher_text = decipher(ciphertext, shift)
        results = match_words(decipher_text, threat_list, nonthreat_list)
        score = results['threats'] + results['nonthreats']
        if score > max_score['score']:
            max_score['rot'] = shift
            max_score['score'] = score
            max_score['info'] = results

    return max_score

def match_words(text, threat_list, nonthreat_list):
    threats = 0
    nonthreats = 0
    words = 0
    for word in text.split(' '):
        word = word.strip(punctuation).lower()
        words += 1
        if word in threat_list:
            threats += 1
        if word in nonthreat_list:
            nonthreats += 1

    return {'threats': threats,
            'nonthreats': nonthreats,
            'words': words}

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

    result = find_rotation(ciphertext, threat_list, nonthreat_list)

    match_percent = int(result['score'] / result['info']['words'] * 100)
    threat_percent = int(result['info']['threats'] / result['info']['words'] * 100)
    print(decipher(ciphertext, result['rot']))
    print('Shift: {}, Match: {}%, Threat: {}%'.format(result['rot'],
                                                       match_percent,
                                                       threat_percent))

test_cases = int(input())
for _ in range(test_cases):
    handle_testcase()
