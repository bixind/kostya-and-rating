from tkinter import *
from InstUser import *

class UserLabel(Frame, InstagramUser):
    def __init__(self, name, master = None):
        InstagramUser.__init__(self, name)
        Frame.__init__(self, master = master, width = 400, height = 50, bg = 'dark grey')
        self.nameLabel = Label(self, text = self.username, bg = 'dark grey', fg = 'cyan')
        self.mediaLabel = Label(self, text = 'Publications:\n' + str(self.media), bg = 'dark grey')
        self.followed_byLabel = Label(self, text = 'Followers:\n' + str(self.followed_by), bg = 'dark grey')
        self.followsLabel = Label(self, text = 'Follows:\n' + str(self.follows), bg = 'dark grey')
        self.ratingLabel = Label(self, text = 'Rating:\n' + "%.3g"%self.rating(), bg = 'dark grey')

    def show_slaves(self):
        self.nameLabel.place(x = 10, y = 14)
        self.mediaLabel.place(relx = 0.3, x = -10, y = 7)
        self.followed_byLabel.place(relx = 0.5, x = -10, y = 7)
        self.followsLabel.place(relx = 0.7, x = -18, y = 7)
        self.ratingLabel.place(relx = 1, x = -60, y = 7)

    def place(self, **kw):
        Frame.place(self, kw)
        self.show_slaves()

    def pack(self, **kw):
        Frame.pack(self, kw)
        self.show_slaves()

    def info(self):
        return self.username.configure()
