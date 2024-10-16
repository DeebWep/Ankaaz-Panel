#!/usr/bin/python
# -------------------------------------------------
INSTAGRAM= 'khuliyef.exe'

# -------------------------------------------------
# import mudules                                  |
# -------------------------------------------------
import os
import time
import sys
import concurrent.futures

import requests
ADMIN_PANEL_PATHS_FILE = "wordlists/admin-panel-directorylist.txt"
REVERSE_SHELL_TEMPLATE_FILE = "wordlists/reverse_shell_template.txt"
# ------------------------------------------------
try:
    import requests as req
except:
    os.system('pip install requests')
#--------------------------------------------
try:
    from colorama import Fore, init
except:
    os.system('pip install colorama')
#--------------------------------------------
try:
    from colored import fg, bg, attr
except:
    os.system('pip install colored')
#--------------------------------------------
try:
    import pyuseragents as agent
except:
    os.system('pip install pyuseragents')
#--------------------------------------------
os.system('clear')
class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orang = '\033[34m'
    white = '\033[00m'
    reset = '\033[0m'
def banner():
    print(f'''

{color.blue} .S_SSSs     .S_sSSs     .S    S.    .S_SSSs     .S_SSSs     sdSSSSSSSbs    {color.blue}
{color.blue}.SS~SSSSS   .SS~YS%%b   .SS    SS.  .SS~SSSSS   .SS~SSSSS    YSSSSSSSS%S    {color.blue}
{color.blue}S%S   SSSS  S%S   `S%b  S%S    S&S  S%S   SSSS  S%S   SSSS          S%S     {color.blue}
{color.blue}S%S    S%S  S%S    S%S  S%S    d*S  S%S    S%S  S%S    S%S         S&S      {color.red}
{color.red}S%S SSSS%S  S%S    S&S  S&S   .S*S  S%S SSSS%S  S%S SSSS%S        S&S       {color.red}
{color.red}S&S  SSS%S  S&S    S&S  S&S_sdSSS   S&S  SSS%S  S&S  SSS%S        S&S       {color.red}
{color.red}S&S    S&S  S&S    S&S  S&S~YSSY%b  S&S    S&S  S&S    S&S       S&S        {color.red}
{color.red}S&S    S&S  S&S    S&S  S&S    `S%  S&S    S&S  S&S    S&S      S*S         {color.red}
{color.red}S*S    S&S  S*S    S*S  S*S     S%  S*S    S&S  S*S    S&S     S*S          {color.green}
{color.green}S*S    S*S  S*S    S*S  S*S     S&  S*S    S*S  S*S    S*S   .s*S           {color.green}
{color.green}S*S    S*S  S*S    S*S  S*S     S&  S*S    S*S  S*S    S*S   sY*SSSSSSSP    {color.green}
{color.green}SSS    S*S  S*S    SSS  S*S     SS  SSS    S*S  SSS    S*S  sY*SSSSSSSSP    {color.green}
{color.green}       SP   SP          SP                 SP          SP                   {color.green}
{color.green}       Y    Y           Y                  Y           Y                    {color.green}

''')


# Admin panel tapmaq funksiyasi
def admin_panel_finder():
    os.system('clear')
    banner()
    print("\n[+] Admin Panel Finder Seçildi")
    print(f"{color.white}[+] Hədəf URL'yi daxil edin (Nümunə: http://example.com or https://example.com): {color.reset}", end="")
    target_url = input().strip()

    # Faylı oxu və bütün yolları yoxla
    try:
        with open(ADMIN_PANEL_PATHS_FILE, "r") as file:
            paths = file.readlines()
            
        index = 0  # Taramanın başladığı yer

        while index < len(paths):
            path = paths[index].strip()
            url = f"{target_url}/{path}"
            print(f"{color.white}                                                                                     {color.reset}")  # URL'yi yoxlayarken qirmizi rəngdə yaz
            try:
                response = requests.get(url, timeout=10)  # 10 saniyə zaman aşımı
                if response.status_code == 200:
                    print(f"{color.green}[+] Admin panel tapıldı: {url}{color.reset}")
                else:
                    print(f"{color.red}[-] {url} Tapılmadı ( Vəziyyət kodu: {response.status_code}){color.reset}")
            except requests.RequestException as e:
                print(f"{color.red}[-] {url} Ünvana daxil olma xətası: {str(e)}{color.reset}")

            except KeyboardInterrupt:
                print(f"\n{color.red}[!] Proses Dayandırıldı!{color.reset}")
                choice = handle_interrupt(target_url, paths, index)  # İndeksi gönderiyoruz
                if choice == "1":
                    return  # Ana menüye dön
                elif choice == "2":
                    exit()  # Programı sonlandır
                elif choice == "3":
                    # Kaldığı yerden devam et
                    print(f"{color.green}[+] Kaldığınız yerden davam edilir...{color.reset}")
                    continue  # Döngü devam etsin

            index += 1

    except FileNotFoundError:
        print(f"{color.red}Xəta: {ADMIN_PANEL_PATHS_FILE} Faylı tapılmadı. Xahiş edirik, düzgün yerdə olduğunuzdan əmin olun.{color.reset}")
    except Exception as e:
        print(f"{color.red}Xəta: {str(e)}{color.reset}")



def directory_bruteforce():
    print("\n[+] Directory Bruteforce Seçildi")
    print(f"{color.white}[+] Hədəf URL'yi daxil edin (Nümunə: http://example.com və ya https://example.com): {color.reset}", end="")
    target_url = input().strip()

    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        print(f"{color.red}[-] Səhv URL formatı. URL-ni http:// və ya https:// ilə başlayıb daxil edin.{color.reset}")
        return

    # Wordlist qovluğunun yolu
    wordlist = "wordlists/directory-list-2.3-medium.txt"

    # Wordlist faylını aç və hər sətirdə yolu oxu
    if os.path.exists(wordlist):
        with open(wordlist, "r") as file:
            directories = file.read().splitlines()
    else:
        print(f"{color.red}[-] Wordlist faylı tapıla bilmədi! Xahiş edirik faylın yolunu yoxlayın.{color.reset}")
        return

    print(f"{color.green}[+] Skan başlanır... {color.reset} (Dayandırmaq üçün Ctrl+C)")

    # Wordlist'də hər cərgə üçün bir istək göndər
    index = 0
    while index < len(directories):
        dir = directories[index]
        url = f"{target_url}/{dir}"
        print(f"{color.white}                                                                                     {color.reset}")
        try:
            response = requests.get(url)

            if response.status_code == 200:  # Əgər status kod 200 isə (tapıldısa)
                print(f"{color.green}[+] Tapıldı: {url} - Status: {response.status_code}{color.reset}")
            else:
                print(f"{color.red}[-] Yoxlanılır: {url} - Status: {response.status_code}{color.reset}")

        except requests.exceptions.RequestException as e:
            print(f"{color.red}Xəta: {str(e)}{color.reset}")

        except KeyboardInterrupt:
            print(f"\n{color.red}[!] Proses Dayandırıldı!{color.reset}")
            choice = handle_interrupt(target_url, directories, index)
            if choice == "1":
                return  # Ana menuya qayıt
            elif choice == "2":
                exit()  # Programı dayandır
            elif choice == "3":
                pass  # Qaldığı yerdən davam et
        index += 1

# Ctrl+C istifadəçidən proses dayandıqda nə etmək istədiklərini soruşmaq üçün
def handle_interrupt(target_url, directories, current_index):
    while True:
        print(f"\n{color.white}[?] Nə etmək istəyirsən?{color.reset}")
        print("1. Ana menuya qayıt")
        print("2. Prosesi sonlandır")
        print("3. Qaldığınız yerdən davam edin")

        choice = input(f"{color.white}\n\nSeçiminiz: {color.reset}").strip()

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print(f"{color.red}Səhv seçim, zəhmət olmasa 1, 2 və ya 3 daxil edin.{color.reset}")

# Fasilə edildikdən sonra prosesi bərpa etmək üçün
def directory_bruteforce_continue(target_url, directories, start_index):
    print(f"{color.green}[+] Qaldığınız yerdən davam edilir...{color.reset}")
    for dir in directories[start_index:]:
        url = f"{target_url}/{dir}"
        try:
            response = requests.get(url)

            if response.status_code == 200:  # Eğer status kod 200 ise (bulunduysa)
                print(f"{color.green}[+] Tapıldı: {url} - Status: {response.status_code}{color.reset}")
            else:
                print(f"{color.red}[-] Yoxlanılır: {url} - Status: {response.status_code}{color.reset}")

        except requests.exceptions.RequestException as e:
            print(f"{color.red}Xəta: {str(e)}{color.reset}")


# Əsas menyuda FFUF alətini əlavə etmək üçün
def ffuf_tool():
    os.system('clear')
    banner()
    print(f"{color.green}[+] Simple Directory Brute Force Tool-u işə salınır...{color.reset}")
    directory_bruteforce()


# Üçüncü vasitə: Reverse PHP Shell
def create_reverse_shell():
    os.system('clear')
    banner()
    print("\n[+] Reverse PHP Shell Generator Seçildi")
    
    # İstifadəçidən IP adresi və port istəyin
    ip_address = input(f"{color.white}[+] İP adresinizi daxil edin: {color.reset}")
    port = input(f"{color.white}[+] Port nömrəsini daxil edin: {color.reset}")
    output_file = input(f"{color.white}[+] Yaradılan faylın adını daxil edin (nümunə: my_reverse_shell): {color.reset}").strip()
    # Reverse shell şablonunu oxu
    try:
        with open(REVERSE_SHELL_TEMPLATE_FILE, "r") as file:
            php_shell_template = file.read()
        
        # Şablonda IP və portu dəyişdir
        php_shell = php_shell_template.replace("{IP_ADDRESS}", ip_address).replace("{PORT}", port)

        # Faylı yaradın
        shell_file_name = output_file+".php"
        with open(shell_file_name, "w") as shell_file:
            shell_file.write(php_shell)

        print(f"{color.green}[+] Reverse PHP shell yaradıldı: {shell_file_name}{color.reset}")
    except FileNotFoundError:
        print(f"{color.red}Xəta: {REVERSE_SHELL_TEMPLATE_FILE} Faylı tapılmadı.{color.reset}")
    except Exception as e:
        print(f"{color.red}Xəta: {str(e)}{color.reset}")


# Ana menu göstərən funksiya
def main_menu():
    while True:
        os.system('clear')
        banner()
        print("[1]  Admin Panel Finder")
        print("[2]  Directory Bruteforce")
        print("[3]  Reverse PHP Shell Generator")
        print("[4]  Çıxış")
        choice = input("\nBir seçim edin (1/2/3/4): ").strip()

        if choice == '1':
            admin_panel_finder()
        elif choice == '2':
            ffuf_tool()
        elif choice == '3':
            create_reverse_shell()
        elif choice == '4':
            print("Çıxılır...")
            break
        else:
            os.system('clear')
            print("\nSəhv seçim, xahiş edirik yenidən cəhd edin.")

if __name__ == "__main__":
    main_menu()
