# gMSA-decoder

A simple Python tool to decode a base64-encoded gMSA blob and extract the NTLM hash for further attack steps.

## Requirements
- Python 3
- `pycryptodome` or native `hashlib` with MD4 support (OpenSSL legacy)

## Usage
```bash
python3 gMSA_decoder.py
```

## Attack context
1. Retrieve the gMSA blob (GoldenGMSA, DSInternals, etc.)
2. Run the script and paste the base64 blob
3. Use the output NTLM hash with Rubeus or mimikatz

## Disclaimer
This tool is intended for authorized penetration testing and educational purposes only.
