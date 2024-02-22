import requests
import random
import webbrowser
import os
import time
import requests
import webbrowser
import sys as n
import random
import webbrowser
import threading
aa = 0
zz = 0
Z = '\033[1;31m' 
X = '\033[1;33m'
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m'
R = "\033[1;91m"
J = '\033[1;94m'
B1 = '\033[2;36m'
ID = Mody.IDe
tokEn = Mody.ELHYBA

print(f""" {B1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
start_msg = requests.post(f"https://api.telegram.org/bot{tokEn}/sendMessage?chat_id={ID}&text=STARTED.").json()
id_msg = start_msg['result']['message_id']

while True:
    username = 'QWERTYUIOPASDFGHJKLZXCVBNM0987654321'
    user = 'bot'
    us = '1234567890QPOIUYTREWA4567SDFGHJKZXCVBN123ML'
    ab = str("".join(random.choice(username)for i in range(1)))
    jj9mj = str("".join(random.choice(user)for i in range(1)))
    s = str("".join(random.choice(us)for i in range(1)))        
    username = ab+s+jj9mj+user
    url = f"https://t.me/{username}"
    req = requests.get(url)
    if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:     
        os.system('cls' if os.name == 'nt' else 'clear')          
      
        print(f" {X}Username {R}({F}@{username}{R}) ")
        print(R+"------------------------------")
        print(f" ({F}-{R}) {F}Hit  {R}  : {F}{zz} \n {R}({J}-{R}) {J}Bad  {R}  : {J}{aa}  \n {R}({X}-{R}) {X}")
        print(R+"------------------------------")       
        tlg = f"https://api.telegram.org/bot{tokEn}/sendMessage?chat_id={ID}&text={username}"
        i = requests.post(tlg)         
        zz += 1
        open ("BOT TELE USER.txt",'a').write(username)              
    else:                   
        requests.post(f"https://api.telegram.org/bot{tokEn}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=جاري صيد يوزرات \n━━━━━━━━━━\nHIT ⌯ {zz}\nBAD ⌯ {aa}\nUSERs ⌯ @{username}\n━━━━━━━━━━\n ")
        os.system('cls' if os.name == 'nt' else 'clear')        
               
        print(f" {X}Username {R}({F}@{username}{R}) ")
        print(R+"━━━━━━━━━━━━━━")
        print(f" ({F}-{R}) {F}Hit  {R}  : {F}{zz} \n {R}({J}-{R}) {J}Bad  {R}  : {J}{aa}  \n {R}({X}-{R}) {X}")
        print(R+"━━━━━━━━━━━━━━")
        aa += 1
    
 #تم تغيير الحقوق وسلبها 😂
 #بلعافيه قلبيي ✨