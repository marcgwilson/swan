import unittest
import string
from swan.codec.codec import BaseCodec


class TestBaseCodec(unittest.TestCase):
	def setUp(self):
		alphabet = string.ascii_letters + string.digits
		self.base62 = BaseCodec(alphabet)
	
	def test_codec(self):
		vals = [0, 2**32-1]
		for val in vals:
			encoded = self.base62.encode(val)
			decoded = self.base62.decode(encoded)
			self.assertEqual(val, decoded)

		self.assertEqual(self.base62.encode(vals[0]), 'aaaaaa')
		self.assertEqual(self.base62.encode(vals[1]), 'eQPpmd')
