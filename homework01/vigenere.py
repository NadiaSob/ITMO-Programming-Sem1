upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        keysymbol = keyword[i % len(keyword)]
        if keysymbol.isupper():
            shift = ord(keysymbol) - ord('A')
        else:
            shift = ord(keysymbol) - ord('a')

        s = plaintext[i]
        if s in upperCase:
            j = upperCase.index(s)
            ciphertext += upperCase[(j + shift) % len(upperCase)]
        elif s in lowerCase:
            j = lowerCase.index(s)
            ciphertext += lowerCase[(j + shift) % len(lowerCase)]
        else:
            ciphertext += s
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        keysymbol = keyword[i % len(keyword)]
        if keysymbol.isupper():
            shift = ord(keysymbol) - ord('A')
        else:
            shift = ord(keysymbol) - ord('a')

        s = ciphertext[i]
        if s in upperCase:
            j = upperCase.index(s)
            plaintext += upperCase[(j - shift) % len(upperCase)]
        elif s in lowerCase:
            j = lowerCase.index(s)
            plaintext += lowerCase[(j - shift) % len(lowerCase)]
        else:
            plaintext += s
    return plaintext
