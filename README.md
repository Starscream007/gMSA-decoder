# gMSA-decoder

A simple Python tool to decode a base64-encoded gMSA blob and extract the NTLM hash and AES keys for further attack steps.

## Requirements
- Python 3
- `impacket` (for AES key derivation)
- `hashlib` with MD4 support (OpenSSL legacy) for NTLM

## Usage
```bash
python3 gMSA_decoder.py
```

## Features
- Extracts NTLM hash from gMSA blob
- Derives AES256/AES128 Kerberos keys (useful when RC4 is disabled)

## Attack context
1. Retrieve the gMSA blob (bloodyAD, GoldenGMSA, DSInternals, etc.)
2. Run the script and paste the base64 blob
3. Use the NTLM hash or AES keys to request a TGT

## Kerberos salt format
`REALM.TLDhost<samaccountname_without_$_lowercase>.<dnshostname_lowercase>`
Example: `internal.localhostadm_gmsa.internal.local`

## Disclaimer
This tool is intended for authorized penetration testing and educational purposes only.
