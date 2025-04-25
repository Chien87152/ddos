import os
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

proxy_sources = list(set([
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "http://worm.rip/http.txt",
    "https://api.openproxylist.xyz/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt",
    "https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/http.txt",
    "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
    "https://raw.githubusercontent.com/rx443/proxy-list/main/online/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt",
    "https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/file/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/miyukii-chan/proxy-list/master/proxies/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/j0rd1s3rr4n0/api/main/proxy/http.txt",
    "https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/http.txt",
    "https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/enseitankado/proxine/main/proxy/http.txt",
    "https://raw.githubusercontent.com/dunno10-a/proxy/main/proxies/http.txt",
    "https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/caliphdev/Proxy-List/main/http.txt",
    "https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
    "https://proxyspace.pro/http.txt",
    "https://openproxylist.xyz/http.txt"
]))

all_proxies = set()
live_count = 0
lock = threading.Lock()

def set_title(live, total):
    os.system(f"title [Scanner Proxy By Henry] | Success proxy: {live} | Total proxy: {total}")

def fetch_proxies(url):
    try:
        response = requests.get(url, timeout=10)
        proxies = response.text.strip().splitlines()
        with lock:
            all_proxies.update(proxy.strip() for proxy in proxies if proxy.strip())
    except:
        pass

def check_proxy(proxy, country_filter):
    global live_count
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        start_time = time.time()
        response = requests.get("http://ip-api.com/json", proxies=proxies, timeout=15)
        latency = int((time.time() - start_time) * 1000)
        if response.status_code == 200:
            data = response.json()
            country = data.get("country", "")
            if (country_filter == "all" or country == country_filter) and latency < 15000:
                with lock:
                    live_count += 1
                    print(f"[Success] {proxy} | Country: {country} | Isp: {data.get('isp')} | Timeout: {latency}ms")
                    with open("http.txt", "a") as f:
                        f.write(proxy + "\n")
                    set_title(live_count, len(all_proxies))
    except:
        pass

def main_scan(country_filter):
    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(fetch_proxies, proxy_sources)

    print(f"Successfully get '{len(all_proxies)}' proxy")
    set_title(0, len(all_proxies))

    with ThreadPoolExecutor(max_workers=500) as executor:
        for proxy in all_proxies:
            executor.submit(check_proxy, proxy, country_filter)

def show_menu():
    print("""
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
Scanner Proxy Henry | Scan Ssl Proxy United States
Owner: (@TcpLegit)
""")
    print("[1] Scan Type Country")
    print("[2] Scan United States")
    print("[3] Exit")

    choice = input(">>> ")

    if choice == "1":
        print("\n[a] Vietnam")
        print("[b] Japan")
        print("[c] Germany")
        print("[d] France")
        print("[e] Russia")
        print("[f] Indonesia")
        print("[all] Globals")
        sub = input(">>> ").lower()
        mapping = {
            "a": "Vietnam",
            "b": "Japan",
            "c": "Germany",
            "d": "France",
            "e": "Russia",
            "f": "Indonesia",
            "all": "all"
        }
        selected_country = mapping.get(sub)
        if selected_country:
            main_scan(selected_country)
    elif choice == "2":
        main_scan("United States")
    elif choice == "3":
        exit()
    else:
        show_menu()

if __name__ == "__main__":
    show_menu()