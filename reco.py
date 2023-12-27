import os,time,sys

try:
    import requests
    from colorama import *
    from pystyle import Colors, Colorate
    from zipfile import ZipFile
except ModuleNotFoundError:
    print("Modul Eksik")
    print("Yukleniyor....")
    os.system("pip install requests_toolbelt")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install bs4")
    os.system("pip install psutil")
    os.system("pip install pycryptodome")
    os.system("pip install zipfile")
    print("Yuklendi!")
    print("Yuklendi!")
    print("Yuklendi!")
    print("Yuklendi!")
    print("Yuklendi!")
    print("Yuklendi!")
    time.sleep(1.5)
    os.system("python reco.py")
    exit(0)

super = requests.get("https://random-username-turkish.vercel.app/api")

if super.status_code == 200:
    print("Kontrol Başarılı")
else:
    print("Kontrol Başarısız | Api Kapalı")


if os.path.exists("temp.txt"):
    os.remove("temp.txt")
if os.path.exists("temp2.zip"):
    os.remove("temp2.zip")


def guncelleme():
    f = open("version.txt", "r")
    ver = f.readline()
    f.close()
##############################
    url2 = "https://raw.githubusercontent.com/Recoo31/auto/main/version.txt"
    res = requests.get(url=url2)
##############################
    a = open("temp.txt","w")
    a.write(res.text)
    a.close()
##############################
    b = open("temp.txt", "r")
    ver2 = b.read()
    b.close()
##############################
    if ver == ver2:
        print("Güncelleme yok")
        pass
    else:
        url = 'https://github.com/Recoo31/auto/raw/main/A.zip'
        r = requests.get(url)

        if os.path.exists("follow.py"):
            os.remove("follow.py")

        if os.path.exists("follow_bot.py"):
            os.remove("follow_bot.py")

        if os.path.exists("like_bot.py"):
            os.remove("like_bot.py")

        if os.path.exists("like.py"):
            os.remove("like.py")

        if os.path.exists("C:\Windows\Temp\guncel-kontrol"):
            os.remove("C:\Windows\Temp\guncel-kontrol")
        else:
            pass

        if os.path.exists("C:\Windows\Temp\guncelleme-not.txt"):
            os.remove("C:\Windows\Temp\guncelleme-not.txt")
        else:
            pass

        if os.path.exists("guncel-kontrol"):
            os.remove("guncel-kontrol")
        else:
            pass

        if os.path.exists("guncelleme-not.txt"):
            os.remove("guncelleme-not.txt")
        else:
            pass
            
        yaz = open('temp2.zip', 'wb').write(r.content)
        dosya = ZipFile('temp2.zip', 'r')
        dosya.extractall(path=None, members=None, pwd=None)
        dosya.close()
        w = open("version.txt", "w")
        w.write(ver2)
        w.close()

#guncelleme()

time.sleep(1.4)

if os.path.exists("temp.txt"):
    os.remove("temp.txt")

if os.path.exists("temp2.zip"):
    os.remove("temp2.zip")






os.system('cls')


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

print("")
print("")
print(Fore.MAGENTA+"                     Profile Follower:1                                  Playlist Like:2")



option = int(input("\n╰──> "))
os.system("cls")
if option == 1:
    os.system("python follow.py")
if option == 2:
    os.system("python like.py")
