#!/usr/bin/env python3
from math import gcd

# -----------------------------
# Modular Arithmetic
# -----------------------------

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a, n):
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError("No modular inverse exists")
    return x % n


# -----------------------------
# Euler Totient (simple)
# -----------------------------

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


# -----------------------------
# Chinese Remainder Theorem
# -----------------------------

def crt(congruences):
    # congruences = [(a1, n1), (a2, n2), ...]
    x = 0
    N = 1
    for _, n in congruences:
        N *= n

    for a, n in congruences:
        Ni = N // n
        inv = mod_inverse(Ni, n)
        x += a * Ni * inv

    return x % N


# -----------------------------
# RSA
# -----------------------------

def rsa_keygen(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)


def rsa_encrypt(m, pub):
    e, n = pub
    return mod_exp(m, e, n)


def rsa_decrypt(c, priv):
    d, n = priv
    return mod_exp(c, d, n)


# -----------------------------
# Diffie-Hellman
# -----------------------------

def diffie_hellman(p, g, a, b):
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    s1 = mod_exp(B, a, p)
    s2 = mod_exp(A, b, p)
    return {
        "A": A,
        "B": B,
        "shared_secret": s1,
        "check": s1 == s2
    }


# -----------------------------
# Discrete Log (Brute Force)
# -----------------------------

def discrete_log(g, y, p):
    for x in range(p):
        if mod_exp(g, x, p) == y:
            return x
    return None


# -----------------------------
# Simple CLI
# -----------------------------

def menu():
    print("""
Crypto Toolkit
==============
1. Modular Inverse
2. Modular Exponentiation
3. RSA Demo
4. Diffie-Hellman
5. Discrete Log
6. CRT Solver
0. Exit
""")


def main():
    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            a = int(input("a: "))
            n = int(input("mod n: "))
            print("Inverse:", mod_inverse(a, n))

        elif choice == "2":
            b = int(input("base: "))
            e = int(input("exp: "))
            m = int(input("mod: "))
            print("Result:", mod_exp(b, e, m))

        elif choice == "3":
            p = int(input("p: "))
            q = int(input("q: "))
            e = int(input("e: "))
            pub, priv = rsa_keygen(p, q, e)
            print("Public:", pub)
            print("Private:", priv)
            msg = int(input("Message: "))
            c = rsa_encrypt(msg, pub)
            print("Encrypted:", c)
            print("Decrypted:", rsa_decrypt(c, priv))

        elif choice == "4":
            p = int(input("p: "))
            g = int(input("g: "))
            a = int(input("a: "))
            b = int(input("b: "))
            print(diffie_hellman(p, g, a, b))

        elif choice == "5":
            g = int(input("g: "))
            y = int(input("y: "))
            p = int(input("p: "))
            print("x:", discrete_log(g, y, p))

        elif choice == "6":
            k = int(input("Number of equations: "))
            cong = []
            for _ in range(k):
                a = int(input("a: "))
                n = int(input("mod: "))
                cong.append((a, n))
            print("Solution:", crt(cong))

        elif choice == "0":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
