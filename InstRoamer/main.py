from tkinter import *
from InstUser import *
from InstUserTable import *
#from datetime import *

root = Tk()
root['width'] = 400
root.title('InstRoamer')
root.resizable(False, False)
greetingLabel = Label(root, text = 'Welcome to Instagram Roamer!', font = '30')

def analyse():
    waitLabel.pack(side = 'top')
    startButton.pack_forget()
    rated_users =[]
    with open('usernames.txt', 'r') as fin:
        for name in fin:
            name = name.split()[0].lower()
            root.update()
            user = InstagramUser(name)
            root.update()
            if user.username is None:
                print('Error', name)
                continue
            for i in user.getInfo():
                print(i, end = ' ')
            print()
            rated_users.append(user.getOnlyRate())
            table.add_user(user)
            table.show_slaves()

    rated_users.sort(key = lambda userinfo: userinfo[1])
    with open('rating.txt','w') as frating:
        for sorted_user in rated_users:
            print(sorted_user[0], sorted_user[1], file = frating)

    waitLabel.pack_forget()
    sortButton.pack(side = 'top')


startButton = Button(root, text = 'Start!', command = analyse)
waitLabel = Label(root, text = 'Wait')
greetingLabel.pack(side = 'top')
startButton.pack(side = 'top')
table = UserTable()
sortButton = Button(root, command = table.sort_by_rating, text = 'Sort by rating')
table.pack(side = 'bottom')

root.mainloop()
