#!/usr/bin/env python3
"""
tools/aes.py - AES Modes: ECB, CBC, CTR, ...
"""

import os
from typing import List
from Crypto.Cipher import AES

def run(args: List[str]):
    if not args:
        print("Usage: python tools/aes.py <mode> -k <key> -p <plaintext>")
        print("Modes: ecb, cbc, ctr")
        return

    mode = args[0].lower()
    key_hex = args[1] if len(args) > 1 else os.urandom(16).hex()
    plaintext_hex = args[2] if len(args) > 2 else b"SecretMessage"

    key = bytes.fromhex(key_hex)
    plaintext = bytes.fromhex(plaintext_hex)

    iv_hex = args[3] if len(args) > 3 else os.urandom(16).hex()
    iv = bytes.fromhex(iv_hex)

    if mode == "ecb":
        cipher = AES.new(key, AES.MODE_ECB)
        print(f"[ECB]  Encrypted: {cipher.encrypt(plaintext).hex()}")
    elif mode == "cbc":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        print(f"[CBC]  Encrypted: {cipher.encrypt(plaintext).hex()}")
    elif mode == "ctr":
        cipher = AES.new(key, AES.MODE_CTR)
        print(f"[CTR]  Encrypted: {cipher.encrypt(plaintext).hex()}")

    print("\n--- Tool Complete ---")