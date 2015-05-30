from urllib.request import urlopen
from urllib.error import *

class InstagramUser:
    """A class for Instagram User"""

    def __init__(self, username = ''):
        if type(username) is not str:
            raise TypeError('String type expected')
        if username:
            try:
                a = urlopen('https://instagram.com/' + username)
                self.username = username
                s = str(a.read())
                del a;
                b = s.find('UserProfile')
                l = s.find('[',b)
                bal = 1
                i = l + 1
                while bal > 0:
                    if s[i] == ']':
                        bal -= 1
                    if s[i] == '[':
                        bal += 1
                    i += 1
                r = i
                self.info = s[l + 1:r - 1]
                b = s.find('counts')
                l = s.find('{', b)
                r = s.find('}', b)
                s = s[l + 1: r]
                p = []
                for st in s.split(','):
                    p.append(int(st.split(':')[1]))
                self.media = p[0]
                self.followed_by = p[1]
                self.follows = p[2]
                b = self.info.find('"is_private"') + '"is_private"'.__len__() + 1
                if self.info[b] == 't':
                    self.is_private = True
                else:
                    self.is_private = False
            except HTTPError as e:
                self.username = None
        else:
            self.username = None

    def rating(self):
        if self.followed_by == 0 or self.follows == 0 or self.media == 0:
            return 0
        else:
            return self.followed_by**2/(self.media*self.follows)

    def relatedUsers(self):
        users = set()
        b = self.info.find('"username"')
        while b >= 0:
            b = b + '"username"'.__len__() + 1
            l = self.info.find('"', b)
            r = self.info.find('"', l + 1)
            users.add(self.info[l + 1:r])
            b = self.info.find('"username"', b)
        return users

    def getInfo(self):
        return (self.username, self.media, self.followed_by, self.follows, self.rating())

    def getOnlyRate(self):
        return (self.username, "%.4g"%(self.rating()))
