def encrypt_vigenere(text: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    result = ""
    for i, letter in enumerate(text):
        key_letter = keyword[i % len(keyword)]

        if "A" <= letter <= "Z":
            shift = ord(key_letter.upper()) - ord("A")
            result += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            shift = ord(key_letter.lower()) - ord("a")
            result += chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += letter
    return result


def decrypt_vigenere(text: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    result = ""
    for i, letter in enumerate(text):
        key_letter = keyword[i % len(keyword)]

        if "A" <= letter <= "Z":
            shift = ord(key_letter.upper()) - ord("A")
            result += chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            shift = ord(key_letter.lower()) - ord("a")
            result += chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
        else:
            result += letter
    return result