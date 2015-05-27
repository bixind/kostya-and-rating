from InstUser import *
from datetime import *
d=datetime.today()

fout = open(d.strftime('%y_%m_%d')+'.txt', 'w')
rated_users =[]
with open('usernames.txt', 'r') as fin:
    for name in fin:
        name = name.split()[0].lower()
        user = InstagramUser(name)
        if user.username is None:
            print('Error', name)
            continue
        for i in user.getInfo():
            print(i, end = ' ')
            print(i, end = ' ', file = fout)
        print()
        print(file = fout)
        rated_users.append(user.getOnlyRate())
        
rated_users.sort(key = lambda userinfo: userinfo[1])
with open('rating.txt','w') as frating:
    for sorted_user in rated_users:
        print(sorted_user[0], sorted_user[1], file = frating)
fout.close()
