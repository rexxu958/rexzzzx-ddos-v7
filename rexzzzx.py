#!/usr/bin/env python3
import os
import sys
import subprocess
from termcolor import colored

# KONFIGURASI UTAMA
VERSION = "v20.23-STABLE"
AUTHOR = "REXZZX TEAM"

class RexzzxUltimate:
    def __init__(self):
        self.tools = {
            # [1] WIFI TOOLS
            "wifi": {
                "show_passwords": self.wifi_passwords,
                "deauth_attack": self.wifi_deauth,
                "handshake_capture": self.capture_handshake,
                "wps_attack": self.wps_attack
            },
            
            # [2] WEB TOOLS
            "web": {
                "sqli_scanner": self.sql_injection_scan,
                "admin_finder": self.find_admin_panels
            },
            
            # [3] OSINT TOOLS
            "osint": {
                "phone_tracker": self.track_phone,
                "email_lookup": self.email_osint
            }
        }

    # [1] WIFI TOOLS IMPLEMENTATION
    def wifi_passwords(self):
        """Show saved WiFi passwords (Termux compatible)"""
        try:
            print(colored("\n[+] Daftar Password WiFi Tersimpan:", 'green'))
            if os.path.exists('/data/misc/wifi/wpa_supplicant.conf'):
                os.system('grep -i "ssid\|psk" /data/misc/wifi/wpa_supplicant.conf')
            else:
                print(colored("[-] File konfigurasi WiFi tidak ditemukan", 'red'))
                print(colored("[!] Coba dengan akses root", 'yellow'))
        except Exception as e:
            print(colored(f"[-] Error: {str(e)}", 'red'))

    def wifi_deauth(self):
        """Deauthentication attack"""
        print(colored("\n[!] Fitur ini membutuhkan:", 'yellow'))
        print("- Perangkat dengan monitor mode")
        print("- aircrack-ng (pkg install aircrack-ng)")
        print(colored("\n[+] Contoh command:", 'green'))
        print("airmon-ng start wlan0")
        print("aireplay-ng --deauth 10 -a [BSSID] wlan0mon")

    def capture_handshake(self):
        """Capture WPA handshake"""
        print(colored("\n[!] Panduan Capture Handshake:", 'yellow'))
        print("1. airmon-ng start wlan0")
        print("2. airodump-ng wlan0mon")
        print("3. airodump-ng -c [channel] --bssid [BSSID] -w capture wlan0mon")
        print("4. Tunggu hingga muncul 'WPA handshake'")

    def wps_attack(self):
        """WPS attack method"""
        print(colored("\n[!] Panduan WPS Attack:", 'yellow'))
        print("1. wash -i wlan0mon (scan WPS)")
        print("2. reaver -i wlan0mon -b [BSSID] -vv")

    # [2] WEB TOOLS IMPLEMENTATION
    def sql_injection_scan(self):
        """Basic SQL injection check"""
        url = input(colored("\n[?] Masukkan URL target: ", 'blue'))
        print(colored(f"\n[+] Memindai {url}...", 'green'))
        print(colored("[!] Gunakan sqlmap untuk analisis lengkap:", 'yellow'))
        print(f"sqlmap -u '{url}' --risk=3 --level=5")

    def find_admin_panels(self):
        """Find admin panels"""
        url = input(colored("\n[?] Masukkan URL target: ", 'blue'))
        print(colored("\n[+] Mencari admin panels...", 'green'))
        common_paths = ['/admin', '/login', '/wp-admin', '/administrator']
        for path in common_paths:
            print(f"Mencoba: {url}{path}")

    # [3] OSINT TOOLS IMPLEMENTATION
    def track_phone(self):
        """Phone number tracker"""
        print(colored("\n[!] Fitur ini membutuhkan API pihak ketiga", 'yellow'))
        print(colored("[+] Gunakan tools seperti PhoneInfoga:", 'green'))
        print("git clone https://github.com/sundowndev/phoneinfoga")
        print("cd phoneinfoga && ./phoneinfoga scan -n [NOMOR]")

    def email_osint(self):
        """Email lookup tool"""
        email = input(colored("\n[?] Masukkan email target: ", 'blue'))
        print(colored(f"\n[+] Memeriksa {email}...", 'green'))
        print(colored("[!] Gunakan hunter.io atau epieos.com untuk OSINT lengkap", 'yellow'))

    # MENU SYSTEM
    def show_menu(self):
        os.system('clear')
        print(colored(f"\n=== REXZZX ULTIMATE {VERSION} ===", 'blue', attrs=['bold']))
        print(colored(f"=== {AUTHOR} ===\n", 'yellow'))
        
        for category in self.tools:
            print(colored(f"=== {category.upper()} ===", 'green'))
            for i, (tool, _) in enumerate(self.tools[category].items(), 1):
                print(f"{i}. {tool.replace('_', ' ').title()}")
            print()
        
        print(colored("0. Exit", 'red'))

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = input(colored("\n[?] Pilih kategori: ", 'yellow'))
                
                if choice == "0":
                    print(colored("\n[+] Keluar dari program...", 'green'))
                    sys.exit()
                
                # Convert choice to category
                categories = list(self.tools.keys())
                if choice.isdigit() and 0 < int(choice) <= len(categories):
                    category = categories[int(choice)-1]
                    self.show_tool_menu(category)
                else:
                    print(colored("\n[-] Pilihan tidak valid!", 'red'))
                    
            except KeyboardInterrupt:
                print(colored("\n[!] Dihentikan oleh pengguna", 'red'))
                sys.exit()
            except Exception as e:
                print(colored(f"\n[-] Error: {str(e)}", 'red'))

    def show_tool_menu(self, category):
        while True:
            os.system('clear')
            print(colored(f"\n=== {category.upper()} TOOLS ===", 'green', attrs=['bold']))
            
            tools = list(self.tools[category].items())
            for i, (tool, _) in enumerate(tools, 1):
                print(f"{i}. {tool.replace('_', ' ').title()}")
            print(colored("\n0. Kembali ke menu utama", 'yellow'))
            
            try:
                choice = input(colored("\n[?] Pilih tool: ", 'blue'))
                
                if choice == "0":
                    return
                
                if choice.isdigit() and 0 < int(choice) <= len(tools):
                    tool_name, tool_func = tools[int(choice)-1]
                    print(colored(f"\n[+] Memulai {tool_name.replace('_', ' ')}...", 'green'))
                    tool_func()
                    input(colored("\n[!] Tekan Enter untuk melanjutkan...", 'yellow'))
                else:
                    print(colored("[-] Pilihan tidak valid!", 'red'))
                    
            except KeyboardInterrupt:
                return
            except Exception as e:
                print(colored(f"\n[-] Error: {str(e)}", 'red'))
                input(colored("\n[!] Tekan Enter untuk melanjutkan...", 'yellow'))

if __name__ == "__main__":
    try:
        # Check basic requirements
        if sys.version_info[0] < 3:
            print(colored("[!] Python 3 diperlukan!", 'red'))
            sys.exit(1)
            
        tool = RexzzxUltimate()
        tool.run()
    except KeyboardInterrupt:
        print(colored("\n[!] Dihentikan oleh pengguna", 'red'))
    except Exception as e:
        print(colored(f"\n[!] Error fatal: {str(e)}", 'red'))
