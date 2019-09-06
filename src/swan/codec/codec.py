import math
from speck import SpeckCipher


def hash_length(num:int, base:int) -> int:
    return (math.floor(math.log(num) / math.log(base)) + 1)


class BaseCodec(object):
    def __init__(self, alphabet, bits=32):
        self.bits = bits
        self.encoder = alphabet
        self.decoder = {k: v for v, k in enumerate(alphabet)}
        self.base = len(alphabet)
        self.length = hash_length(2**self.bits-1, self.base)

    def decode(self, hash: str) -> int:
        result = 0
        for i, c in enumerate(reversed(hash)):
            result += (self.base ** i) * self.decoder[c]
        return result

    def encode(self, id: int) -> str:
        val = id
        result = ''
        while val != 0:
            q, r = divmod(val, self.base)
            result = self.encoder[r] + result
            val = q
        return result.rjust(self.length, self.encoder[0])


class IDCodec(object):
    def __init__(self, key, alphabet, key_size, block_size):
        self.cipher = SpeckCipher(key, key_size=key_size, block_size=block_size)
        self.codec = BaseCodec(alphabet, bits=block_size)
        self.max_id = 2 ** block_size

    def decode(self, hash: str) -> int:
        return self.cipher.decrypt(self.codec.decode(hash)) + 1

    def encode(self, id: int) -> str:
        if id < 1 or id > self.max_id:
            raise Exception('id must be between 1 and %d' % (self.max_id))

        return self.codec.encode(self.cipher.encrypt(id - 1))
