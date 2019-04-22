# Lab 16 URLs and HTML
# Adam Houser, Colin Reed, Sergio Quiroz
#-------------------------------------

import urllib
import sys
import os

def lab16(site):
    os.getcwd()
    file=open("lab16output.html","w")
    data=urllib.urlopen(site)
    data = data.readlines()
    for line in data:
        if "<path" in line:
            file.write(line)
    file.close()

lab16("https://www.bbc.com/news")
