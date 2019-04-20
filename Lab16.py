# Lab 16 URLs and HTML
# Adam, Colin, Sergio
#-------------------------------------

from urllib import request
import sys

req = request.Request('https://www.bbc.com/news/world-asia-47997727')

resp = request.urlopen(req)

# Error handling. If request fails, try again with user agent. If it fails again system exit.
if resp.code != 200:

    req = request.Request('https://github.com/facebook/react-native/issues/10471', headers={'User-Agent': 'Mozilla/5.0'})

    resp = request.urlopen(req)

    if resp.code != 200:
        sys.exit("Request failed.")


writeString = ''

data = resp.read().decode('utf-8')
data = data.split('<p>') # Delim is paragraph tag
data.pop(0) # Removing whatever comes before the first paragraph
for str in data:
    str = '!' + str # Adding a exclamation point to the beginning of every new string.
    str = str.split('</p>') # running delim as ending paragraph tag.

#data.remove(-1) # Removing whatever comes after the last paragraph tag

for str in data:
    if str[0] == '!':
        writeString = writeString + str + '\n'





file = open("/home/colin/Documents/School/PentagrationGithub/Lab16_ACS/index.html", "wt")

file.write(writeString)

file.close()
print(writeString)
