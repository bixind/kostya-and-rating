from InstUserLabel import *
from tkinter import *

class UserTable:
    def add_user(self, instUser):
        self.users.append(UserLabel(instUser, parent= self.mainframe))

    def __init__(self, *users, height = 400, parent = None):
        if (parent):
            self.mainframe = Frame(parent, height = height, width = 440, bg = 'light blue')
        else:
            self.mainframe = Frame(height = height, width = 440, bg = 'light blue')
        self.mainframe.focus()
        self.users = []
        self.dy = 0
        self.height = height
        for user in users:
            self.add_user(user)

        def scroll(event):
            self.dy = self.dy -event.delta/120*20
            print(self.dy)
            self.show_slaves()

        def move(e):
            if e.keysym == 'Up':
                self.dy = self.dy + 20
            else:
                self.dy = self.dy - 20
            print(self.dy)
            self.show_slaves()

        self.mainframe.bind('<MouseWheel>', scroll)
        self.mainframe.bind('<Up>', move)
        self.mainframe.bind('<Down>', move)

    def show_slaves(self):
        num = 0
        for ulabel in self.users:
            num += 1
            ulabel.place(x = 20, y = (num - 1) * 60 + 10 + self.dy)

    def place(self, **kw):
        self.mainframe.place(kw)
        self.show_slaves()

    def pack(self, **kw):
        self.mainframe.pack(kw)
        self.show_slaves()

    def sort_by_rating(self):
        self.users.sort(key = lambda user: -user.instUser.rating())
        self.show_slaves()
