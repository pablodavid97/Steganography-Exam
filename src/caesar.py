ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26

def decrypt(text, key):
    length = len(text)
    ciphered_val = 0
    original_char = ""
    original_text = ""

    for i in range(length):
        if(text[i].isalpha()):
            if (text[i].isupper()):
                index = ALPHABET_UPPER.find(text[i])

                if(index != -1):
                    ciphered_val = (index - key) % ALPHABET_LENGTH
                    original_char = ALPHABET_UPPER[ciphered_val]

            else:
                index = ALPHABET_LOWER.find(text[i])

                if(index != -1):
                    ciphered_val = (index - key) % ALPHABET_LENGTH
                    original_char = ALPHABET_LOWER[ciphered_val]
        else:
            original_char = text[i]

        original_text += original_char

    return original_text