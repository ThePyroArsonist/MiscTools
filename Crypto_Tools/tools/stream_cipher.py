#!/usr/bin/env python3
"""
tools/stream_cipher.py - DES, 3DES, RC4 Tools
"""

from typing import List
import os
from Crypto.Cipher import DES, TripleDES, ARC4

def run(args: List[str]):
    if not args:
        print("Usage: python tools/stream_cipher.py <method> <key> <plaintext>")
        print("Methods: des, 3des, rc4")
        return

    method = args[0].lower()
    key = bytes.fromhex(args[1]) if len(args) > 1 else os.urandom(8).hex()
    plaintext = bytes.fromhex(args[2]) if len(args) > 2 else b"HelloWorld"

    if method == "des":
        cipher = DES.new(key[:8])
        print(f"[DES] Encrypted: {cipher.encrypt(plaintext).hex()}")
    elif method == "3des":
        cipher = TripleDES.new(key[:24])
        print(f"[3DES] Encrypted: {cipher.encrypt(plaintext).hex()}")
    elif method == "rc4":
        cipher = ARC4.new(key)
        print(f"[RC4]  Encrypted: {cipher.encrypt(plaintext).hex()}")

    print("\n--- Tool Complete ---")