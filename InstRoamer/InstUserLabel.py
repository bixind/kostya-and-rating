from tkinter import *
from InstUser import *

class UserLabel:
    def __init__(self, instUser, parent = None):
        if (parent):
            self.mainframe = Frame(parent, width = 400, height = 50, bg = 'dark grey')
        else:
            self.mainframe = Frame(width = 400, height = 50, bg = 'dark grey')
        self.instUser = instUser
        self.nameLabel = Label(self.mainframe, text = self.instUser.username, bg = 'dark grey', fg = 'cyan')
        self.mediaLabel = Label(self.mainframe, text = 'Publications:\n' + str(self.instUser.media), bg = 'dark grey')
        self.followed_byLabel = Label(self.mainframe, text = 'Followers:\n' + str(self.instUser.followed_by), bg = 'dark grey')
        self.followsLabel = Label(self.mainframe, text = 'Subscribers:\n' + str(self.instUser.follows), bg = 'dark grey')
        self.ratingLabel = Label(self.mainframe, text = 'Rating:\n' + "%.3g"%self.instUser.rating(), bg = 'dark grey')

    def show_slaves(self):
        self.nameLabel.place(x = 10, y = 14)
        self.mediaLabel.place(relx = 0.3, x = -10, y = 7)
        self.followed_byLabel.place(relx = 0.5, x = -10, y = 7)
        self.followsLabel.place(relx = 0.7, x = -18, y = 7)
        self.ratingLabel.place(relx = 1, x = -60, y = 7)

    def place(self, **kw):
        self.mainframe.place(kw)
        self.show_slaves()

    def pack(self, **kw):
        self.mainframe.pack(kw)
        self.show_slaves()

    def place_forget(self):
        self.mainframe.place_forget()

    def info(self):
        return self.username.configure()
