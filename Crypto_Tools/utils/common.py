#!/usr/bin/env python3
"""
tools/common.py - Shared Utilities for Crypto_Tools
"""

import os
from typing import List, Tuple

# AES Block Size
AES_BLOCK_SIZE = 16
# Key sizes for AES
AES_KEY_SIZES = [128, 192, 256]

def pad(data: bytes, block_size: int = AES_BLOCK_SIZE) -> bytes:
    """
    PKCS#7 Padding
    """
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len)
    return data + padding

def unpad(data: bytes, block_size: int = AES_BLOCK_SIZE) -> bytes:
    """
    Remove PKCS#7 padding
    """
    padding_len = data[-1]
    return data[:-padding_len]

def bytes_to_hex(data: bytes) -> str:
    """
    Convert bytes to hexadecimal string
    """
    return data.hex()

def hex_to_bytes(hex_str: str) -> bytes:
    """
    Convert hexadecimal string to bytes
    """
    return bytes.fromhex(hex_str)

def create_key(key_size: int) -> bytes:
    """
    Create a random key of specified size in bits
    """
    key_bytes = (key_size // 8)
    import secrets
    return secrets.token_bytes(key_bytes)

# Constants for algorithms
# Example: DES
from Crypto.Cipher import DES, TripleDES
# ... or import from tools if needed