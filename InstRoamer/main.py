from InstUser import *

with open('usernames.txt', 'r') as fin:
    for name in fin:
        name = name.split()[0]
        user = InstagramUser(name)
        if user.username is None:
            print('Error', name)
            continue
        for i in user.getInfo():
            print(i, end = ' ')
        print()
