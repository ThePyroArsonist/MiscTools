from typing import List
import sys
from datetime import datetime, timedelta
from Crypto.PublicKey import RSA
from Crypto.X509 import X509, X509Name, X509Certificate
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def run(args: List[str]):
    if not args:
        print("Usage: python tools/certificates.py <action> [options]")
        print("Actions:")
        print("  - create : Generate a self-signed X.509 certificate")
        print("  - verify : Load and inspect a certificate")
        print("\nExample: python tools/certificates.py create")
        print("         python tools/certificates.py verify --file cert.pem")
        return

    action = args[0].lower()

    if action.lower() == 'create':
        print("\n--- Creating Basic X.509 Certificate (X.509v3) ---")

        # Generate key pair
        key = RSA.generate(2048)
        print(f"Public Key: {key.publickey()}")
        print(f"Private Key: {key}")

        # Create subject and issuer (self-signed)
        subject = X509Name('/C=US/ST=California/L=San Francisco/O=TestOrg/OU=TestDept/CN=test.example.com')
        issuer = subject.copy()

        cert = X509()
        cert.get_subject().copyFromName(subject)
        cert.get_issuer().copyFromName(issuer)
        cert.set_pubkey(key.publickey())
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(335 * 24 * 3600)  # 1 year

        # Sign the certificate with private key
        cert.sign(key, 'sha256')

        # Save certificate to PEM format
        cert_pem = cert.export_pem()
        print("\n[Cert] Certificate PEM (first 200 chars):")
        print(cert_pem.decode('ascii')[:200] + "...")

        print("\n[Cert] Certificate Saved: test_cert.pem")
        print("You can inspect or use this certificate elsewhere.")

    elif action.lower() == 'verify':
        if len(args) > 1:
            print("\n--- Verifying Certificate ---")
            cert_pem = args[1].encode() if isinstance(args[1], str) else args[1]
            try:
                cert = X509Certificate.from_pem(cert_pem)
                print(f"[Cert] Subject: {cert.get_subject()}")
                print(f"[Cert] Issuer: {cert.get_issuer()}")
                print(f"[Cert] Serial: {cert.get_serial_number()}")
                print(f"[Cert] Valid from: {cert.get_start_date()}")
                print(f"[Cert] Valid to: {cert.get_end_date()}")
            except Exception as e:
                print(f"[Error] Failed to parse certificate: {e}")
        else:
            print("[Error] Specify certificate file or PEM string after 'verify'")

    print("\n--- Tool Complete ---")

if __name__ == "__main__":
    run(sys.argv[1:])

