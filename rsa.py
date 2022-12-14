import random
from collections import namedtuple

import miller_rabin


def generate_key_pair(bit_len: int):
    e = 65537
    p, q = 0, 0
    while not miller_rabin.is_prime(p, 10):
        p = random.getrandbits(int(bit_len / 2))
    while not miller_rabin.is_prime(q, 10):
        q = random.getrandbits(int(bit_len / 2))

    n = p * q

    phi = (p - 1) * (q - 1)

    d = pow(e, -1, phi)
    return PublicKey(e, n), PrivateKey(d, n)


class PublicKey(namedtuple('PublicKey', 'e n')):
    __slots__ = ()

    def encrypt(self, x):
        return [pow(ord(char), self.e, self.n) for char in x]


class PrivateKey(namedtuple('PrivateKey', 'd n')):
    __slots__ = ()

    def decrypt(self, x):
        return ''.join([chr(pow(char, self.d, self.n)) for char in x])
