import unittest

from src.lab2.caesar import decrypt_caesar, encrypt_caesar


class CaesarTestCase(unittest.TestCase):

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")

    def test_encrypt_lowercase(self):
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")

    def test_encrypt_with_symbols(self):
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")

    def test_decrypt(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")

    def test_custom_shift(self):
        self.assertEqual(encrypt_caesar("ABC", 1), "BCD")

    def test_zero_shift(self):
        self.assertEqual(encrypt_caesar("Python", 0), "Python")

    def test_empty_string(self):
        self.assertEqual(encrypt_caesar(""), "")
        self.assertEqual(decrypt_caesar(""), "")


if __name__ == "__main__":
    unittest.main()