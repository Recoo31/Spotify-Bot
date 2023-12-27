import requests, random, string
from keyauth import api
import os
import sys
import os.path
import hashlib
import time
import base64


# os.system("cls")
# os.system("title Lisans")
# print("Wait...")
# def getchecksum():
#         path = os.path.basename(__file__)
#         if not os.path.exists(path):
#             path = path[:-2] + "exe"
#         md5_hash = hashlib.md5()
#         a_file = open(path,"rb")
#         content = a_file.read()
#         md5_hash.update(content)
#         digest = md5_hash.hexdigest()
#         return digest

# keyauthapp = api(
#         name = "Spotify",
#         ownerid = "RZCK6vSDM8",
#         secret = "4044bfdd9f1a1993f6ee5eb0cea2406c921e48afa2e01dc1a0f4fed9f522134b",
#         version = "1.0",
#         hash_to_check = getchecksum()
#     )

# if os.path.exists("login.txt"):
#     os.system("cls")
#     with open("login.txt", "r") as f:
#         for line in f.read().splitlines():
#             if ":" in line:
#                 user = line.split(":")[0]
#                 password = line.split(":")[-1]
# else:

#     user = input('Username: ')
#     password = input('Password: ')
#     os.system("cls")
#     os.system("title Spotify Bot")


# keyauthapp.login(user,password)
# dosya = open("login.txt","w")
# dosya.write(user+':'+password)
# dosya.close()
# os.system("cls")
# os.system("title Spotify Bot")

# def parse(a, re, re2):
#     try:
#         start = a.index(re) + len(re)
#         end = a.index(re2, start)
#         return a[start:end]
#     except ValueError:
#         return ""

# if os.path.isdir("C:\Windows\Temp") == True: # Temp kontrol
#     if os.path.isfile("C:\Windows\Temp\guncel-kontrol") == False: # Dosya yoksa
#         getreco = requests.get("https://gist.github.com/Recoo31/b3c9b39598d738385e3ddf32a25e6f53") #get link
#         getreco2 = parse(getreco.text, '<td id="file-guncelleme-LC1" class="blob-code blob-code-inner js-file-line">','</td>')#parse link
#         r = requests.get(url=getreco2)
#         yaz = open('reco.py', 'wb').write(r.content) # donwload and write new reco.py
#         w = open("C:/Windows/Temp/guncel-kontrol", "w")
#         w.close()
#     else:
#         pass
# else:
#     if os.path.isfile("guncel-kontrol") == False:
#         getreco = requests.get("https://gist.github.com/Recoo31/b3c9b39598d738385e3ddf32a25e6f53") #get link
#         getreco2 = parse(getreco.text, '<td id="file-guncelleme-LC1" class="blob-code blob-code-inner js-file-line">','</td>')#parse link
#         r = requests.get(url=getreco2)
#         yaz = open('reco.py', 'wb').write(r.content) # donwload and write new reco.py
#         w = open("guncel-kontrol", "w")
#         w.close()
#     else:
#         pass



# if os.path.isfile("C:/Windows/Temp/guncelleme-not.txt") == True:
#     pass
# elif os.path.isfile("guncelleme-not.txt") == True:
#     pass
# else:
#     print("\n\n\n\n\n")
#     getannounce = requests.get("https://gist.github.com/Recoo31/049d3725d4816f81255422fef583d6c7")
#     getannounce2 = parse(getannounce.text, '<td id="file-duyuru-LC1" class="blob-code blob-code-inner js-file-line">', '</td>')
#     for reco in getannounce2.replace(r'\n', '\n'):
#         sys.stdout.write(str(reco))
#         sys.stdout.flush()
#         time.sleep(0.090)

#     time.sleep(1.5)
#     if os.path.isdir("C:/Windows/Temp") == True:
#         w = open("C:/Windows/Temp/guncelleme-not.txt", "w")
#         w.write(getannounce2)
#         w.close()
#     else:
#         w = open("guncelleme-not.txt", "w")
#         w.write(getannounce2)
#         w.close()

# os.system("cls")

global cevap
cevap = int(input("                        Normal Profil Icın:1                                Artist Icın:2 \n\n >"))



os.system("cls")

# global cevap2
# cevap2 = int(input("                           Çoklu Bot:1                                 Tek Hesaba Bot:2 \n\n >"))
# os.system("cls")


maillist= ["@gmail.com","@hotmail.com","@outlook.com","@yahoo.com","@protonmail.com","@proton.me"]
class spotify:
    def __init__(self, profile, proxy = None):
        self.session = requests.Session()
        self.profile = profile
        self.proxy = proxy
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "Accept-encoding": "gzip, deflate, br",
            "Accept-language": "tr-TR,tr;q=0.9",
            "Content-type": "application/json",
            "Origin": "https://www.spotify.com",
            "Referer": "https://www.spotify.com/",
            "Sec-fetch-dest": "empty",
            "Sec-fetch-mode": "cors",
            "Sec-fetch-site": "same-site",
            "Sec-gpc": "1",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }

        

        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 17)) + maillist[random.randint(0,5)]
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 16))
        year = ("").join(random.choices(string.digits, k = 1))

        proxies = None
        if self.proxy != None:
            proxies = {
                        'http': f'http://{self.proxy}',
                        'https': f'http://{self.proxy}',
                    }
        try:
            us = self.session.get("https://random-username-turkish.vercel.app/api", timeout=4).text
            self.usi = us
            data = {
	"account_details":{
		"birthdate":"198"+year+"-06-2"+year,
		"consent_flags":{
			"eula_agreed":True,
			"send_email":False,
			"third_party_email":False
		},
		"display_name":self.usi,
		"email_and_password_identifier":{
			"email":email,
			"password":password
		},
		"gender":1
	},
	"callback_uri":"https://www.spotify.com/signup/challenge?locale=tr",
	"client_info":{
		"api_key":"4c7a36d5260abca4af282779720cf631",
		"app_version":"v2",
		"capabilities":[
			1
		],
		"installation_id":"f84c8a2a-9991-4dd2-a7b4-d74d092997e0",
		"platform":"www"
	},
	"tracking":{
		"creation_flow":"",
		"creation_point":"https://www.spotify.com/tr/",
		"referrer":""
	}
    
}
            create = self.session.post("https://spclient-ipv6.wg.spotify.com/signup/public/v2/account/create", headers = headers, json = data, proxies = proxies)
            if "login_token" in create.text:
                global username
                c = create.json()['success']
                login_token = c['login_token']
                username = c['username']
                self.username = username
                a = open("profile-list.txt","a")
                a.write(username+'\n')
                return login_token
            else:
                return False
        except:
            return False

    def get_csrf_token(self):
        proxies = {
                    'http': f'http://{self.proxy}',
                    'https': f'http://{self.proxy}',
                }
        try:
            r = self.session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1", proxies = proxies)
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return False
        
    def get_token(self, login_token):
        proxies = {
                    'http': f'http://{self.proxy}',
                    'https': f'http://{self.proxy}',
                }
        headers1 = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        cook = self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers1, data = "splot=" + login_token, proxies = proxies)
        spdc = cook.cookies.get('sp_dc')
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "WebPlayer",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/",
        }
        cookies = {'sp_dc': spdc}
        self.cookies=cookies
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers, cookies=self.cookies
            )
            return r.json()["accessToken"]
        except:
            return None
        

    def follow(self):
        login_token = self.register_account()
        if login_token == None:
            return None
        elif login_token == False:
            return None, f""
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "Token Alinamadi"
        headers = {
            "authorization": "Bearer {}".format(auth_token),
            "Host": "api.spotify.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Accept": "application/json",
            "Accept-Language": "en",
            "Accept-Encoding": "gzip, deflate, br",
            "app-platform": "WebPlayer",
            "spotify-app-version": "1.1.73.305.gbf92e68e",
            "Origin": "https://open.spotify.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Referer": "https://open.spotify.com/",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "TE": "trailers",
        }
        resimhead = {
            "Host": "image-upload.spotify.com",
            "Content-Length": "126757",
            "Accept-Language": "tr",
            "Authorization": "Bearer {}".format(auth_token),
            "Content-Type": "image/jpeg",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
            "Origin": "https://open.spotify.com",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://open.spotify.com/",
            "Accept-Encoding": "gzip, deflate"

        }
        resimhead1 = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "tr",
        "app-platform": "WebPlayer",
        "Authorization": "Bearer {}".format(auth_token),
        "content-length": "0",
        "origin": "https://open.spotify.com",
        "referer": "https://open.spotify.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "spotify-app-version": "1.1.88.399.g5e8f6880",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
        try:
            proxies = {
                    'http': f'http://{self.proxy}',
                    'https': f'http://{self.proxy}',
                    }
            if cevap == 1:
                ##############Profile Photo##############
                resim1 = self.session.get("https://picsum.photos/400")
                resim = resim1.content
                r = self.session.post("https://image-upload.spotify.com/v4/user-profile",data=resim, headers=resimhead)
                tokenimiz = r.json()['uploadToken']
                uri = f"https://spclient.wg.spotify.com/identity/v3/profile-image/{self.username}/{tokenimiz}"
                dat = ""
                c = self.session.post(url=uri, data=dat, headers=resimhead1, proxies = proxies)
##########################################Post Follow########################################################
                if "," in self.profile and not "!" in self.profile:
                    self.profile = self.profile.split(",")
                    for i in range(len(self.profile)):
                        reco = f"https://api.spotify.com/v1/me/following?type=user&ids={self.profile[i]}"
                        putt = self.session.put(
                            reco,
                            headers = headers,
                            proxies=proxies,
                            cookies=self.cookies
                        )
                elif "!" in self.profile and not "," in self.profile:
                    self.profile = self.profile.replace("!","")
                    try:
                        reco = "https://api.spotify.com/v1/me/following?type=user&ids="
                        putt = self.session.put(
                            reco + self.profile,
                            headers = headers,
                            proxies=proxies,
                            cookies=self.cookies
                        )
                        try:
                            random_profile = open("profile-list.txt").readlines()
                            for yeteramk in range(0,2):
                                random_user = random.choice(random_profile)
                                reco = f"https://api.spotify.com/v1/me/following?type=user&ids={random_user.strip()}"
                                putt = self.session.put(
                                        url=reco,
                                        headers = headers,
                                        proxies=proxies,
                                        cookies=self.cookies
                                    )
                                time.sleep(0.8)
                        except:
                            print("Hata Kod:2")
                    except:
                        print("Hata Kod:3, discorddan ulaş")
                        pass

                elif "!!" in self.profile:
                    try:
                        self.profile = self.profile.replace("!!","")
                        self.profile = self.profile.split(",")
                        for i in range(len(self.profile)):
                            reco = f"https://api.spotify.com/v1/me/following?type=user&ids={self.profile[i]}"
                            putt = self.session.put(
                                reco,
                                headers = headers,
                                proxies=proxies,
                                cookies=self.cookies
                            )
                            for yeteramk in range(0,3):
                                random_profile = open("profile-list.txt").readlines()
                                random_user = random.choice(random_profile)
                                reco = f"https://api.spotify.com/v1/me/following?type=user&ids={random_user.strip()}"
                                putt = self.session.put(
                                        url=reco,
                                        headers = headers,
                                        proxies=proxies,
                                        cookies=self.cookies
                                    )
                                time.sleep(0.8)
                    except:
                        print("Hata var, discorddan ulaş")
                        pass

                else:
                    reco = "https://api.spotify.com/v1/me/following?type=user&ids="
                    putt = self.session.put(
                        reco + self.profile,
                        headers = headers,
                        proxies=proxies,
                        cookies=self.cookies
                    )

                ##############Response##############
                if putt.status_code == 204:
                    return True,""
                else:
                    return False, "Retry"


            if cevap == 2:
                reco = "https://api.spotify.com/v1/me/following?type=artist&ids="
                putt = self.session.put(
                    reco + self.profile,
                    headers = headers,
                    proxies=proxies,
                    cookies=self.cookies
                )

                #Response#
                if putt.status_code == 204:
                    return True, ""
                else:
                    return False, "Retry"
        except:
            return False, "Hata Kod:4"

