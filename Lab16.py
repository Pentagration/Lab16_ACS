# Lab 16 URLs and HTML
# Adam, Colin, Sergio
#-------------------------------------

from urllib import request
import sys
import os


import urllib.request
with urllib.request.urlopen("http://www.python.org") as url:
    s = url.read()


writeString = ''
with urllib.request.urlopen('https://www.bbc.com/news/world-us-canada-48001382') as url:
    data = url.read()
data = data.readlines()
for line in data:
    if '<p>' in line:
        while not '</p>' in line:
            writeString = writeString + line






#file = open("/home/colin/Documents/School/PentagrationGithub/Lab16_ACS/index.html", "wt")

#ile.write(writeString)

#file.close()
print(writeString)
