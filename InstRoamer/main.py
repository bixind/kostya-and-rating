from InstUserTable import *
import threading
#from datetime import *

root = Tk()
root['width'] = 400
root.title('InstRoamer')
root.resizable(False, False)
greetingLabel = Label(root, text = 'Welcome to Instagram Roamer!', font = '30')

def analyse():
    waitLabel.pack(side = 'top')
    startButton.pack_forget()
    namesList = []
    with open('usernames.txt', 'r') as fin:
        for name in fin:
            namesList.append(name.split()[0].lower())
    namesLock = threading.Lock()
    tableLock = threading.Lock()

    def connect():
        while True:
            namesLock.acquire()
            if (namesList.__len__() < 1):
                namesLock.release()
                return
            name = namesList.pop()
            namesLock.release()
            userLabel = UserLabel(name = name, master=table)
            tableLock.acquire()
            table.add_label(userLabel)
            tableLock.release()

    thrCount = 30
    for i in range(thrCount):
        thread = threading.Thread(target=connect)
        thread.start()

    while threading.active_count() > 1:
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
