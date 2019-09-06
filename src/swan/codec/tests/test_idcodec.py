import unittest
import string
from speck import SpeckCipher
from swan.codec.codec import BaseCodec, IDCodec


class TestIDCodec(unittest.TestCase):
	def setUp(self):
		key = 0x123456789ABCDEF00FEDCBA987654321
		alphabet = string.ascii_letters + string.digits
		keysize = 64
		idsize = 32

		self.codec = IDCodec(key,
			alphabet,
			keysize,
			idsize)

		self.cipher = SpeckCipher(key, key_size=keysize, block_size=idsize)
		self.base_codec = BaseCodec(alphabet, bits=idsize)

	def test_exception(self):
		with self.assertRaises(Exception) as e:
			self.codec.encode(0)

		with self.assertRaises(Exception) as e:
			self.codec.encode(-1)

		with self.assertRaises(Exception) as e:
			self.codec.encode(2**32 + 2)

		with self.assertRaises(Exception) as e:
			self.codec.encode(2**64)
	
	def test_codec(self):
		vals = [0, 2**32-1]
		for val in vals:
			encoded_1 = self.codec.encode(val + 1)
			encoded_2 = self.base_codec.encode(self.cipher.encrypt(val))
			self.assertEqual(encoded_1, encoded_2)

			decoded_1 = self.codec.decode(encoded_1)
			decoded_2 = self.cipher.decrypt(self.base_codec.decode(encoded_2)) + 1
			self.assertEqual(decoded_1, decoded_2)
