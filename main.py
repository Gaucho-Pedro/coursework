import logging

import dixon
import rsa

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
    public, private = rsa.generate_key_pair(32)

    e = public.e
    n = private.n
    print(n)

    encrypted_msg = public.encrypt("Привет")
    print(private.decrypt(encrypted_msg))
    numbers = dixon.factor(n)
    print(numbers)
    n = int(numbers[0]) * int(numbers[1])
    phi = (int(numbers[0]) - 1) * (int(numbers[1]) - 1)

    d = pow(e, -1, phi)

    assert d == private.d
