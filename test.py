from urllib.request import *
from urllib.error import *

fout = open('output.txt', 'w')
fin = open('input.txt', 'r')

for name in fin:
    name = name.split()[0]
    try:
        a = urlopen(('https://instagram.com/' + name))
    except HTTPError:
        print(name, '- Wrong username or smth out of date')
        continue
    s = str(a.read())
    b = 0
    b = s.find('"counts"')
    l = s.find('{', b)
    r = s.find('}', b)
    s = s[l + 1:r]
    o = s.split(sep = ':')
    media = int(o[1].split(',')[0])
    followed_by = int(o[2].split(',')[0])
    follows = int(o[3])
    print(name, media, followed_by, follows, file = fout)
    print(name, media, followed_by, follows)


fout.close()
fin.close()
