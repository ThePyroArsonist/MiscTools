#!/usr/bin/env python3
"""
tools/rsa.py - RSA Tools: KeyGen, Encrypt, Decrypt
"""

import os
from typing import List
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256

def run(args: List[str]):
    print("RSA Tool - Usage: python tools/rsa.py <action> -k <key_file>")
    print("Actions: encrypt, decrypt, keygen, sign, verify")

    action = args[0] if args else 'keygen'

    if action.lower() == 'keygen':
        print("\n--- Generating RSA Key Pair ---")
        key = RSA.generate(2048)
        print(f"Public Key: {key.publickey()}")
        print(f"Private Key: {key}")

    elif action.lower() == 'encrypt':
        key_hex = args[1] if len(args) > 1 else os.urandom(256).hex()
        plaintext = bytes.fromhex(args[2])
        key = RSA.import_key(bytes.fromhex(key_hex))
        cipher = PKCS1_OAEP.new(key.publickey())
        ciphertext = cipher.encrypt(plaintext)
        print(f"Encrypted: {ciphertext.hex()}")

    print("\n--- Tool Complete ---")