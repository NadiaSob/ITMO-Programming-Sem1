import typing as tp


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
        if s == 'X':
            ciphertext += 'A'
        elif s == 'x':
            ciphertext += 'a'
        elif s == 'Y':
            ciphertext += 'B'
        elif s == 'y':
            ciphertext += 'b'
        elif s == 'Z':
            ciphertext += 'C'
        elif s == 'z':
            ciphertext += 'c'
        elif not 'a' <= s <= 'z' and not 'A' <= s <= 'Z':
            ciphertext += s
        else:
            ciphertext += chr(ord(s) + shift)
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
        if s == 'A':
            plaintext += 'X'
        elif s == 'a':
            plaintext += 'x'
        elif s == 'B':
            plaintext += 'Y'
        elif s == 'b':
            plaintext += 'y'
        elif s == 'C':
            plaintext += 'Z'
        elif s == 'c':
            plaintext += 'z'
        elif not 'a' <= s <= 'z' and not 'A' <= s <= 'Z':
            plaintext += s
        else:
            plaintext += chr(ord(s) - shift)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
