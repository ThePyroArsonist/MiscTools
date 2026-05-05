#!/usr/bin/env python3
"""
tools/hash.py - Hash Functions (SHA-1, SHA-256, etc.)
"""

from typing import List
from Crypto.Hash import SHA1, SHA256, SHA384, SHA512

def run(args: List[str]):
    if not args:
        print("Usage: python tools/hash.py <algorithm> <data>")
        print("Algorithms: sha1, sha256, sha384, sha512")
        return

    algo = args[0].lower()
    data = bytes.fromhex(args[1])

    hashers = {
        'sha1': SHA1,
        'sha256': SHA256,
        'sha384': SHA384,
        'sha512': SHA512,
    }

    hasher = hashers.get(algo)
    if hasher:
        result = hasher.new(data).hexdigest()
        print(f"[Hash] {algo.upper()}: {result}")
    else:
        print(f"Unknown hash algorithm: {algo}")

    print("\n--- Tool Complete ---")