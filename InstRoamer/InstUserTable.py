from InstUserLabel import *
from tkinter import *

class UserTable(Frame):
    def add_user(self, name):
        try:
            userLabel = UserLabel(name = name, master = self)
            self.users.append(userLabel)
            self.show_slaves()
        except UsernameError:
            self.errorCount += 1
            print('Error')

    def __init__(self, *users, height = 400, master = None):
        self.errorCount = 0
        Frame.__init__(self, master = master, height = height, width = 440, bg = 'light blue')
        self.focus()
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
            self.dy = min(self.dy, 0)
            self.dy = max(self.dy, -self.users.__len__()*60 + self.height - 10)
            if (self.users.__len__()*60 < self.height):
                self.dy = 0
            print(self.dy)
            self.show_slaves()

        self.bind('<MouseWheel>', scroll)
        self.bind('<Up>', move)
        self.bind('<Down>', move)

    def show_slaves(self):
        num = 0
        for ulabel in self.users:
            num += 1
            ulabel.place(x = 20, y = (num - 1) * 60 + 10 + self.dy)

    def place(self, **kw):
        Frame.place(self, kw)
        self.show_slaves()

    def pack(self, **kw):
        Frame.pack(self, kw)
        self.show_slaves()

    def sort_by_rating(self):
        self.users.sort(key = lambda user: -user.rating())
        self.show_slaves()
