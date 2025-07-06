import socket
import os
from colorama import Fore, Style, init
init(autoreset=True)

DEVICE_SIGNATURES = {
    "android": "Android Device 📱",
    "iphone": "Apple iPhone 🍎",
    "ipad": "Apple iPad 🍎",
    "raspberry": "Raspberry Pi 🍓",
    "macbook": "Apple MacBook 💻",
    "oneplus": "OnePlus Phone 🔴",
    "windows": "Windows Machine 💻",
    "desktop": "Windows Desktop 🖥️",
    "laptop": "Laptop 💻",
    "samsung": "Samsung Device 📱",
}

FALLBACK_PREFIXES = {
    "192.168.43": "Likely Mobile Hotspot Device 📶",
    "192.168.0": "Typical Home Router or PC 🖥️",
    "192.168.1": "Common LAN Device 🌐",
    "10.0.0": "Enterprise or Custom Subnet 💼",
    "100.": "Carrier Grade NAT / ISP Device 🌐",
    "172.16": "Corporate Network Device 🏢"
}

def banner():
    os.system("clear")
    print(Fore.RED + "╔" + "═" * 60 + "╗")
    print(Fore.RED + "║" + Fore.LIGHTRED_EX + "   ☠️ Device Profiler v2 by KK - with Fallback Detection ☠️".center(60) + Fore.RED + "║")
    print(Fore.RED + "╠" + "═" * 60 + "╣")
    print(Fore.YELLOW + "     Works even if hostname is not available (IP Guess)")
    print(Fore.RED + "╚" + "═" * 60 + "╝\n")

def classify_device(hostname):
    lower = hostname.lower()
    for keyword, device in DEVICE_SIGNATURES.items():
        if keyword in lower:
            return device
    return "Unknown Device 🕵️"

def fallback_from_ip(ip):
    for prefix, guess in FALLBACK_PREFIXES.items():
        if ip.startswith(prefix):
            return guess
    return "Unknown IP Range 🧩"

def profile_device(ip):
    print(Fore.CYAN + f"🎯 IP: {ip}")
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        device_type = classify_device(hostname)
        print(Fore.GREEN + f"🔗 Hostname: {hostname}")
        print(Fore.MAGENTA + f"🧠 Detected: {device_type}\n")
    except socket.herror:
        fallback = fallback_from_ip(ip)
        print(Fore.YELLOW + "⚠️ Hostname not found. Using IP prefix for guessing.")
        print(Fore.MAGENTA + f"🧠 Guessed Device Type: {fallback}\n")

def main():
    banner()
    ip = input(Fore.LIGHTCYAN_EX + "Enter IP address (e.g. 192.168.1.5): " + Style.RESET_ALL).strip()
    profile_device(ip)

if __name__ == "__main__":
    main()
