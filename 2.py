from datetime import datetime

def caesar_cipher(text, shift=3):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

with open('input.txt', 'r', encoding='utf-8') as infile:
    text = infile.read()

encrypted_text = caesar_cipher(text)

with open('encrypted.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(encrypted_text)

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_entry = f'{timestamp} - "{text[:20]}" -> "{encrypted_text[:20]}"\n'

with open('history.txt', 'a', encoding='utf-8') as log:
    log.write(log_entry)
