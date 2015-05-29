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
            table.add_user(name)
            root.update()
            for i in table.users[table.users.__len__() - 1].getInfo():
                print(i, end = ' ')
            print()
            table.show_slaves()
    waitLabel.pack_forget()
    errorCountLabel['text'] = 'Errors: ' + str(table.errorCount)
    errorCountLabel.pack(side = 'top')
    sortButton.pack(side = 'top')

startButton = Button(root, text = 'Start!', command = analyse)
errorCountLabel = Label(root)
waitLabel = Label(root, text = 'Wait')
greetingLabel.pack(side = 'top')
startButton.pack(side = 'top')
table = UserTable()
sortButton = Button(root, command = table.sort_by_rating, text = 'Sort by rating')
table.pack(side = 'bottom')

root.mainloop()
