from like_bot import spotify
import threading, os, time
from pystyle import Colors, Colorate
from colorama import *

lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0




def ui():
    print(Colorate.Horizontal(Colors.blue_to_purple, """ 
                                                (                    
                                                )\ )                 
                                                (()/(  (              
                                                /(_))))\ (  (    (   
                                                (_)) /((_))\ )\   )\  
                                                | _ (_)) ((_|(_) ((_) 
                                                |   / -_) _/ _ \/ _ \ 
                                                |_|_\___\__\___/\___/ 
                                                                    """, 1))
    



ui()

spotify_profile = str(input(Fore.LIGHTMAGENTA_EX+"Link: "))
threads = int(input(Fore.LIGHTMAGENTA_EX+"\nThreads: "))
os.system("cls")

def load_proxies():
    if not os.path.exists("proxy.txt"):
        print("\n'proxy.txt' Adinda Dosya Yok")
        time.sleep(10)
        os._exit(0)
    with open("proxy.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nProxy Yuklenemedi")
            time.sleep(10)
            os._exit(0)


load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    obj = spotify(spotify_profile, proxies[proxy_counter])
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print("{}".format(counter))
    else:
        safe_print(error)

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter:
            proxy_counter = 0