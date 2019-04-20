# Lab 16 URLs and HTML
# Adam, Colin, Sergio
#-------------------------------------

from urllib import request
import sys
import re

req = request.Request('https://github.com/facebook/react-native/issues/10471')

resp = request.urlopen(req)

# Error handling. If request fails, try again with user agent. If it fails again system exit.
if resp.code != 200:

    req = request.Request('https://github.com/facebook/react-native/issues/10471', headers={'User-Agent': 'Mozilla/5.0'})

    resp = request.urlopen(req)

    if resp.code != 200:
        sys.exit("Request failed.")


writeString = ''

data = resp.read()
data.split('<p>')
for str in data:
    if str ==





file = open("/home/colin/Documents/School/PentagrationGithub/Lab16_ACS/index.html", "wt")

file.write(
 """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01
 Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">

 <html>
 <head><title>I made this page with Python!</title>
 </head>
 <body>
 <h1>MY PYTHON PAGE!!!</h1>
 </body>
 </html>""")

file.close()
