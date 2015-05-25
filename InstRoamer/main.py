from InstUser import *
from datetime import *
d=datetime.today()

fout = open(d.strftime('%y_%m_%d')+'.txt', 'w')
frating = open('rating.txt','w')
with open('usernames.txt', 'r') as fin:
    for name in fin:
        name = name.split()[0]
        user = InstagramUser(name)
        if user.username is None:
            print('Error', name)
            continue
        for i in user.getInfo():
            print(i, end = ' ')
            print(i, end = ' ', file = fout)
            print()
            print(file = fout)

        for i in user.getOnlyRate():
             print(i, end = ' ', file = frating)

        print()
