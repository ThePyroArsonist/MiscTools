#!/usr/bin/env python3
"""
tools/digital_signature.py - Sign & Verify
"""

import os
from typing import List
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def run(args: List[str]):
    if not args:
        print("Usage: python tools/digital_signature.py <action> -k <key_file>")
        print("Actions: sign, verify")
        return

    action = args[0].lower()
    key_hex = args[1] if len(args) > 1 else os.urandom(256).hex()
    key = RSA.import_key(bytes.fromhex(key_hex))
    message = bytes.fromhex(args[2])

    if action.lower() == 'sign':
        message_hash = SHA256.new(message)
        signature = pkcs1_15.new(key, message_hash)
        print(f"Signature: {signature.hex()}")
    elif action.lower() == 'verify':
        pub_key = key.publickey()
        if pkcs1_15.verify(pub_key, message, message_hash, signature):
            print("\n[Sign] Verified: True")
        else:
            print("\n[Sign] Verified: False")

    print("\n--- Tool Complete ---")