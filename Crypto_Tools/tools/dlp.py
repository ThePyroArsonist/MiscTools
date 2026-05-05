#!/usr/bin/env python3
"""
tools/dlp.py - Discrete Log Problem
"""

from typing import List
import random

def run(args: List[str]):
    if not args:
        print("Usage: python tools/dlp.py <p> <g> <h> (find x: g^x = h (mod p))")
        return

    p = int(args[0])
    g = int(args[1])
    h = int(args[2])

    x = dlp_solver(p, g, h)

    if x is not None:
        print(f"\n[DL]  Found x = {x}")
    else:
        print(f"\n[DL]  No discrete log solution found for given values.")

    print("\n--- Tool Complete ---")

def dlp_solver(p: int, g: int, h: int) -> int:
    # Baby-step Giant-step algorithm
    m = int(p**0.5) + 1
    baby_steps = {pow(g, i, p): i for i in range(m)}
    factor = pow(g, -m, p)
    for i in range(m):
        if (h * pow(factor, i, p)) in baby_steps:
            return i + m * baby_steps[h * pow(factor, i, p)]
    return None