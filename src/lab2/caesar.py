def encrypt_caesar(text: str, shift: int = 3) -> str:
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
    result = ""
    for letter in text:
        if "A" <= letter <= "Z":
            result += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            result += chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += letter
    return result


def decrypt_caesar(text: str, shift: int = 3) -> str:
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
    result = ""
    for letter in text:
        if "A" <= letter <= "Z":
            result += chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            result+= chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
        else:
            result += letter
    return result