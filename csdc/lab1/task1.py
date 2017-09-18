alphabet_len = ord('z') - ord('a') + 1


def get_encrypted_letter(char, shift):
    encrypted_char = char.lower()
    char_value = ord(encrypted_char)
    shift %= alphabet_len

    if shift > 0:
        if char_value > ord('z') - shift and char_value <= ord('z'):
            encrypted_char = chr(char_value + shift - alphabet_len)
        elif char_value >= ord('a') and char_value <= ord('z') - shift:
            encrypted_char = chr(char_value + shift)
    elif shift < 0:
        if char_value >= ord('a') and char_value < ord('a') - shift:
            encrypted_char = chr(char_value + shift + alphabet_len)
        elif char_value >= ord('a') - shift and char_value <= ord('z'):
            encrypted_char = chr(char_value + shift)

    if char.isupper():
        encrypted_char = encrypted_char.upper()
    return encrypted_char


def encrypt(source):
    encrypted = ''
    shift = 3
    for char in source:
        encrypted += get_encrypted_letter(char, shift)
    return encrypted


def is_letter(char):
    return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z')


def get_shift(encrypted):
    letter_frequencies_file = open('letter_frequencies.txt')
    letter_frequencies = []
    for line in letter_frequencies_file:
        split_line = line.split()
        letter_frequencies.append([split_line[0], float(split_line[1])])
    letter_frequencies_file.close()

    letter_frequencies.sort(key=lambda frequency_info: -frequency_info[1])

    current_frequencies = []
    for i in range(ord('a'), ord('z') + 1):
        current_frequencies.append([chr(i), 0])
    letter_num = 0
    for char in encrypted:
        if not is_letter(char):
            continue
        letter_num += 1
        char = char.lower()
        current_frequencies[ord(char) - ord('a')][1] += 1
    for i in range(0, alphabet_len):
        current_frequencies[i][1] /= letter_num

    current_frequencies.sort(key=lambda frequency_info: -frequency_info[1])

    shifts = {}
    for i in range(0, alphabet_len):
        shift = ord(current_frequencies[i][0]) - ord(letter_frequencies[i][0])
        if not shift in shifts:
            shifts[shift] = 1
        else:
            shifts[shift] += 1
    shift = max(shifts, key=lambda shift: shifts[shift])
    return shift


def get_decrypted_letter(char, shift):
    decrypted_char = char.lower()
    char_value = ord(decrypted_char)
    shift %= alphabet_len

    if shift > 0:
        if char_value >= ord('a') and char_value < ord('a') + shift:
            decrypted_char = chr(char_value - shift + alphabet_len)
        elif char_value >= ord('a') + shift and char_value <= ord('z'):
            decrypted_char = chr(char_value - shift)
    elif shift < 0:
        if char_value > ord('z') + shift and char_value <= ord('z'):
            decrypted_char = chr(char_value - shift - alphabet_len)
        elif char_value >= ord('a') and char_value <= ord('z') + shift:
            decrypted_char = chr(char_value - shift)

    if char.isupper():
        decrypted_char = decrypted_char.upper()
    return decrypted_char


def decrypt(encrypted):
    shift = get_shift(encrypted)
    decrypted = ''
    for char in encrypted:
        decrypted += get_decrypted_letter(char, shift)
    return decrypted


source_file = open('source/source5.txt')
source = source_file.read()
source_file.close()

encrypted = encrypt(source)

encrypted_file = open('encrypted/task1_encrypted.txt', 'w')
encrypted_file.write(encrypted)
encrypted_file.close()

decrypted = decrypt(encrypted)

decrypted_file = open('decrypted/task1_decrypted.txt', 'w')
decrypted_file.write(decrypted)
decrypted_file.close()
