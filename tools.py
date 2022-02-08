import  os,colorama,socket,time,sys,random
from colorama import Fore,Style,Back
from datetime import *
from time import sleep
colorama.init(autoreset=True)
os.system("clear")

cl = [Fore.BLUE , Fore.LIGHTMAGENTA_EX, Fore.CYAN ,Fore.GREEN, Fore.LIGHTCYAN_EX, Fore.RED]
r = random.choice(cl)


banner2 = """
       +=======================================+
       |.......... Phishing tools .............|
       +---------------------------------------+
       |#Author: unknown-kel                   |
       |#I take no responsibilities for the    |
       |  use of this program !                |
       +=======================================+
       |..........Phishing tools ..............|
       +---------------------------------------+

"""


banner1 = """

███████████████████████████████████    ./unknown-kel
█▄─▄▄─█─▄▄▄▄█▄─█▀▀▀█─▄█▄─▄▄▀█▄─▄▄▀█
██─▄▄▄█▄▄▄▄─██─█─█─█─███─▄─▄██─██─█
▀▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀

"""

for i in banner1:
    sys.stdout.write(r +i)
    sys.stdout.flush()
    sleep(0.02)

passwrds = "sgsvdjsvs"


while True:
	print("Open this url to get password »» " + r + "https://controlc.com/2704441f")
	pass_ent = input("\033[1;91m["+"\033[1;92m»»"+"\033[1;91m]"+"\033[1;92m Enter Password »»\033[1;93m ")
	if pass_ent !=passwrds:
		print(Fore.RED + "[x]Access Denied!")
		sleep(1)
		os.system("https://controlc.com/2704441f")
	elif pass_ent == passwrds:
			print("[✓]Access Granted!")
			sleep(2)
			break
		

os.system("clear")
sleep(2)
banner= """

 ██▓███   ██░ ██ ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██░  ██▒▓██░ ██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░░        ░  ░░ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
          ░  ░  ░             ░ ░      ░ ░      ░  ░      ░  
     https://github.com/unknown-kel                                                        
"""

for i in banner:
    sys.stdout.write(r + i)
    sys.stdout.flush()
    sleep(0.001)

for i in banner2:
    sys.stdout.write(r +i)
    sys.stdout.flush()
    sleep(0.001)

print("\n")
print(r + "Your Ip address :" ,socket.gethostbyname(socket.gethostname()))
sleep(1)
today = date.today()
print(r + "Date :" ,today)
sleep(1)
now = datetime.now()
current_time = time(now.hour, now.minute, now.second)
print(r + "Time :" ,current_time)
sleep(2)

print(r + "."*60)
sleep(2)
print("\n")
print("\033[1;91m["+"\033[1;92m1"+"\033[1;91m]"+"\033[1;93m  Pubg phishing tool")
print("\033[1;91m["+"\033[1;92m2"+"\033[1;91m]"+"\033[1;93m  Zphisher")
print("\033[1;91m["+"\033[1;92m3"+"\033[1;91m]"+"\033[1;93m  BlackEye")
print("\033[1;91m["+"\033[1;92m4"+"\033[1;91m]"+"\033[1;93m  weeman")
print("\033[1;91m["+"\033[1;92m5"+"\033[1;91m]"+"\033[1;93m  Seeker")
print("\033[1;91m["+"\033[1;92m6"+"\033[1;91m]"+"\033[1;93m  Hacklock")
print("\033[1;91m["+"\033[1;92m7"+"\033[1;91m]"+"\033[1;93m  T-phish")
print("\033[1;91m["+"\033[1;92m8"+"\033[1;91m]"+"\033[1;93m  YouTube Channel")
print("\033[1;91m["+"\033[1;92m9"+"\033[1;91m]"+"\033[1;93m  WhatsApp Me")
print("\033[1;91m["+"\033[1;92m0"+"\033[1;91m]"+"\033[1;99m  Exit Tool")


print("\n")
print(r + "."*60)
sleep(1)


while True:
	op = input("\033[1;91m["+"\033[1;92m»»"+"\033[1;91m]"+" \033[1;93mEnter Option To Install »»\033[1;92m ")
	if op == "1":
		os.system("clear")
		print(banner)
		os.system("cd ; git clone https://github.com/lovehacker404/Phishing ; cd Phishing ;bash BlackMafia.sh")
		break
	elif op == "2":
		os.system("clear")
		print(r+banner)
		os.system("cd ; apt update && apt upgrade -y ; apt install git curl wget php -y ; git clone git://github.com/htr-tech/zphisher.git ; cd zphisher ; bash zphisher.sh")
		break
	elif op == "3":
		os.system("clear")
		print(r+banner)
		os.system("cd ;git clone https://github.com/thelinuxchoice/blackeye ; cd blackeye ; bash blackeye.sh")
	elif op == "4":
		os.system("clear")
		print(r+banner)
		os.system("cd ;git clone https://github.com/samyoyo/weeman.git ;cd weeman ;chmod +x weeman.py ;python2 weeman.py")
		break
	elif op == "5":
		os.system("clear")
		print(r+banner)
		os.system("cd; git clone https://github.com/thewhiteh4t/seeker.git; bash termux_install.sh; python seeker.py -t manual")
	elif op == "6":
		os.system("clear")
		print(r+banner)
		os.system("cd; git clone https://github.com/noob-hackers/hacklock; cd $HOME; cd hacklock; bash setup; bash hacklock.sh")
		break
	elif op == "7":
		os.system("clear")
		print(r+banner)
		os.system("cd; git clone https://github.com/0xarman/T-Phish.git; unzip T-Phish; cd T-Phish; bash phish.sh")
		break
	elif op == "8":
		os.system("xdg-open https://youtube.com/channel/UCyQ39v3Vw3Tk2Hj2cDBZucQ")
	elif op == "9":
		os.system("xdg-open http://wa.me//+233550983471")
	elif op == "0":
		print("\033[95m\nThanks For Using Our Script")
		exit()
	else:
		print("\033[1;91m["+"\033[1;92mx"+"\033[1;91m]"+"\033[1;93m Invalid Option")
		sleep(1)
