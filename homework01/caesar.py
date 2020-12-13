import typing as tp

upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for s in plaintext:
        if s in upperCase:
            i = upperCase.index(s)
            ciphertext += upperCase[(i + shift) % len(upperCase)]
        elif s in lowerCase:
            i = lowerCase.index(s)
            ciphertext += lowerCase[(i + shift) % len(lowerCase)]
        else:
            ciphertext += s
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for s in ciphertext:
        if s in upperCase:
            i = upperCase.index(s)
            plaintext += upperCase[(i - shift) % len(upperCase)]
        elif s in lowerCase:
            i = lowerCase.index(s)
            plaintext += lowerCase[(i - shift) % len(lowerCase)]
        else:
            plaintext += s
    return plaintext


print(encrypt_caesar('PYTHON'))
print(decrypt_caesar('SBWKRQ'))
