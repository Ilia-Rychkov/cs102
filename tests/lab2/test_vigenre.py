import unittest

from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere


class VigenereTestCase(unittest.TestCase):

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_decrypt_uppercase(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_key_a_uppercase(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")

    def test_key_a_lowercase(self):
        self.assertEqual(encrypt_vigenere("python", "a"), "python")

    def test_encrypt_and_decrypt(self):
        encrypted = encrypt_vigenere("PYTHON", "KEY")
        self.assertEqual(decrypt_vigenere(encrypted, "KEY"), "PYTHON")

    def test_repeating_keyword(self):
        self.assertEqual(encrypt_vigenere("AAAAAA", "ABC"), "ABCABC")


if __name__ == "__main__":
    unittest.main()