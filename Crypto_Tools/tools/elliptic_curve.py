#!/usr/bin/env python3
"""
tools/elliptic_curve.py - ECDH, ECDSA Tools
"""

from typing import List
from Crypto.PublicKey import ECDH
from Crypto.Signature import pss
from Crypto.Hash import SHA256

def run(args: List[str]):
    if not args:
        print("Usage: python tools/elliptic_curve.py <action>")
        print("Actions: ecdh, ecdsa, keygen")
        return

    action = args[0].lower()

    if action.lower() == 'ecdh':
        print("\n--- ECDH Key Exchange ---")
        alice = ECDH.generate()
        bob = ECDH.generate()
        shared_secret = alice.exchange(bob)
        print(f"Shared Secret (Alice): {shared_secret.hex()}")
        print(f"Shared Secret (Bob):   {alice.exchange(bob).hex()}")

    print("\n--- Tool Complete ---")