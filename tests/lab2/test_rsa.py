import unittest

from src.lab2.rsa import (
    decrypt,
    encrypt,
    gcd,
    generate_keypair,
    is_prime,
    multiplicative_inverse,
)


class RSATestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(1))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_generate_keypair(self):
        public, private = generate_keypair(17, 19)

        self.assertEqual(public[1], 17 * 19)
        self.assertEqual(private[1], 17 * 19)

    def test_equal_primes(self):
        with self.assertRaises(ValueError):
            generate_keypair(17, 17)

    def test_not_prime(self):
        with self.assertRaises(ValueError):
            generate_keypair(8, 19)

    def test_encrypt_decrypt(self):
        public, private = generate_keypair(17, 19)

        message = "Hello"
        encrypted = encrypt(private, message)
        decrypted = decrypt(public, encrypted)

        self.assertEqual(decrypted, message)


if __name__ == "__main__":
    unittest.main()