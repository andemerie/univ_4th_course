import re
from math import gcd, floor, ceil
from task1 import get_shift

alphabet = []
for i in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(i))


def is_letter(char):
    return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z')


def get_encrypted_letter(char, pos_in_text, keyword):
    if not is_letter(char):
        return char

    encrypted_char = char.lower()
    pos_in_keyword = pos_in_text % len(keyword)
    pos_in_alphabet = ord(encrypted_char) - ord('a')
    encrypted_char = alphabet[(ord(keyword[pos_in_keyword]) - ord('a') + pos_in_alphabet) % len(alphabet)]

    if char.isupper():
        encrypted_char = encrypted_char.upper()
    return encrypted_char


def encrypt(source, keyword):
    encrypted = ''
    pos_in_text = 0
    for char in source:
        encrypted += get_encrypted_letter(char, pos_in_text, keyword)
        pos_in_text += 1
    return encrypted


def are_all_letters(string):
    for char in string:
        if not is_letter(char):
            return False
    return True


def find_gcd_for_list(list):
    previous_value = list[0]
    for i in range(1, len(list)):
        previous_value = gcd(previous_value, list[i])
    return previous_value


def get_keyword_len(encrypted):
    distances = {}
    for i in range(0, len(encrypted) - 3):
        trigram = encrypted[i: i + 3]
        if not are_all_letters(trigram) or distances.get(trigram):
            continue

        pattern = re.compile(trigram)
        for match in pattern.finditer(encrypted, i + 1):
            if not trigram in distances:
                distances[trigram] = [match.start() - i]
            else:
                distance_list = distances[trigram]
                distances[trigram].append(match.start() - i - sum(distance_list))
    frequent_trigram = max(distances, key=lambda trigram: len(distances[trigram]))
    limitation1 = floor(len(distances[frequent_trigram]) * 0.1)

    filtered_distances = {trigram: distance for trigram, distance in distances.items() if len(distance) > 1}

    distance_list = []
    for distance in filtered_distances:
        distance_list.extend(filtered_distances[distance])
    distance_count = {}
    for d in distance_list:
        if not d in distance_count:
            distance_count[d] = 1
        else:
            distance_count[d] += 1
    limitation2 = floor(len(distances[frequent_trigram]) * 0.3)
    f = [key for key in distance_count if distance_count[key] > 2]

    return find_gcd_for_list(f)


def decrypt(encrypted):
    keyword_len = get_keyword_len(encrypted)
    print(keyword_len)

    string_list = []
    for i in range(0, keyword_len):
        string_list.append('')
    for i in range(0, len(encrypted)):
        string_list_index = i % keyword_len
        string_list[string_list_index] += encrypted[i]

    for string in string_list:
        shift = get_shift(string)
        decrypted_char = alphabet[shift % len(alphabet)]
        print(decrypted_char)

    return encrypted

source_file = open('source/source5.txt')
source = source_file.read()
source_file.close()

encrypted = encrypt(source, 'willpower')

encrypted_file = open('encrypted/task2_encrypted.txt', 'w')
encrypted_file.write(encrypted)
encrypted_file.close()

decrypted = decrypt(encrypted)

decrypted_file = open('decrypted/task2_decrypted.txt', 'w')
decrypted_file.write(decrypted)
decrypted_file.close()
