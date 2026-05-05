#!/usr/bin/env python3
"""
Crypto_Tools - Main Script (Light-Weight Dispatcher)
Launches specific cryptography tools based on user input.
"""

import sys
import os
from typing import List, Optional

# Add the tools directory to the path
TOOLS_DIR = os.path.join(os.path.dirname(__file__), 'tools')
if not sys.path[0] or TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

# Import available tools dynamically
try:
    from tools import stream_cipher
    from tools.aes import aes_tools
    from tools.rsa import rsa_tools
    from tools.dlp import dlp_tools
    from tools.elliptic_curve import ec_tools
    from tools.digital_signature import sig_tools
    from tools.hash import hash_tools
    from tools.certificates import cert_tools
except ImportError as e:
    print(f"Import error: {e}")
    print("Ensure all modules in tools/ are properly installed.")
    sys.exit(1)

AVAILABLE_TOOLS = {
    'stream_cipher': stream_cipher,
    'aes': aes_tools,
    'rsa': rsa_tools,
    'dlp': dlp_tools,
    'ec': ec_tools,
    'sig': sig_tools,
    'hash': hash_tools,
    'cert': cert_tools,
}

def print_menu():
    print("\n" + "=" * 50)
    print("      CRYPTO TOOLS SUITE - MAIN MENU")
    print("=" * 50)
    print("\n1. Stream Cipher Tools (DES, 3DES)")
    print("2. AES Tools (ECB, CBC, CTR, ... )")
    print("3. RSA Tools (Encrypt, Decrypt, KeyGen)")
    print("4. Discrete Log Problem (DLP)")
    print("5. Elliptic Curve Tools (ECDH, ECDSA)")
    print("6. Digital Signatures")
    print("7. Hash Functions")
    print("8. Digital Certificates (Basic)")
    print("0. Exit")
    print("=" * 50 + "\n")

def get_input() -> Optional[str]:
    while True:
        user_input = input("Select a tool (or 0 to exit): ").strip()
        if user_input in AVAILABLE_TOOLS:
            return user_input
        elif user_input.lower() == '0':
            return 'exit'
        else:
            print(f"Unknown option: {user_input}. Please try again.")

def run_tool(tool_name: str, user_input: List[str]):
    if tool_name in ['exit', '0']:
        print("\nExiting program...")
        sys.exit(0)

    tool_module = AVAILABLE_TOOLS[tool_name]
    print(f"\n--- Loading {tool_name.upper()} Tools ---\n")
    tool_module.run(user_input)

def main():
    print("\nWelcome to Crypto_Tools!\n")
    print("Option A: Interactive Menu")
    print("Option B: Command Line Script")
    
    mode = input("Select mode (A or B): ").strip()

    if mode.upper() == 'B':
        # Command-line interface
        print("\n--- Command Line Mode ---\n")
        print("Usage: python main.py <tool_name> <args...>")
        print("Example: python main.py aes -m cbc -k '12345' -p '67890'")
        print("\nType 'menu' for interactive menu.")

        if len(sys.argv) > 1:
            tool_name = sys.argv[1].lower()
            if tool_name in AVAILABLE_TOOLS:
                args = sys.argv[2:]
                run_tool(tool_name, args)
            elif tool_name.lower() == 'menu':
                while True:
                    print_menu()
                    choice = input("Enter tool or 0 to exit: ").strip().lower()
                    if choice == '0' or choice in AVAILABLE_TOOLS:
                        run_tool(choice, [])
                    elif choice.lower() == 'q':
                        print("\nQuitting...")
                        sys.exit(0)
                    else:
                        print("Invalid option. Try again.")
        else:
            print("\nNo tool specified. Run: python main.py <tool_name>")
            print("Type 'menu' for interactive mode, or press Ctrl+C to exit.")
    else:
        # Interactive menu
        while True:
            print_menu()
            choice = input("Enter tool or 0 to exit: ").strip().lower()
            if choice == '0' or choice in AVAILABLE_TOOLS:
                run_tool(choice, [])
            elif choice.lower() == 'q':
                print("\nQuitting...")
                sys.exit(0)
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()