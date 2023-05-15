import random
from fast_pow import fast_pow
import math


# Returns the greatest common divisor of a and b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Returns a tuple (d, x, y) such that d = gcd(a, b) and ax + by = d
def extended_euclidean_algorithm(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_euclidean_algorithm(b, a % b)
        return (d, y, x - (a // b) * y)


# Returns a random prime number between min_value and max_value
def generate_prime(min_value, max_value):
    while True:
        p = random.randint(min_value, max_value)
        if is_prime(p):
            return p


# Checks if n is a prime number
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


# Generates public and private keys for RSA encryption
def generate_rsa_keys(min_value, max_value):
    p = generate_prime(min_value, max_value)
    q = generate_prime(min_value, max_value)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d, _, _ = extended_euclidean_algorithm(e, phi)
    d = d % phi
    if d < 0:
        d += phi
    return (e, n), (d, n)


# Encrypts a message using RSA encryption
def rsa_encrypt(message, public_key):
    m = message
    n, e = public_key
    if type(message) == int:
        m = str(m)
    encrypted_message = [fast_pow(ord(char), e, n) for char in m]
    return encrypted_message


# Decrypts a message using RSA encryption
def rsa_decrypt(encrypted_message, private_key):
    n, d = private_key
    em = encrypted_message
    if type(encrypted_message) == int:
        em = str(em)
    decrypted_message = ''.join([chr(fast_pow(char, d, n)) for char in em])
    return decrypted_message


def main():
    public_key = (27977, 13)
    private_key = (27977, 25477)
    encrypted_message = rsa_encrypt(150, public_key)
    decrypted_message = rsa_decrypt(encrypted_message, private_key)
    print(encrypted_message)
    print(decrypted_message)


if __name__ == '__main__':
    main()
