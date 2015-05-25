from tkinter import *
from InstUser import *
#from datetime import *

root = Tk()

root.title('InstRoamer')
greeting = Label(root, text = 'Welcome to InstRoamer (prealpha)!')
greeting.pack(side = 'top')
checkbox_state = IntVar()
checkbox = Checkbutton(root, text = 'Print rating to the file', variable = checkbox_state)

def start():
    global is_rating_saved
    is_rating_saved = checkbox_state.get()
    root.destroy()
    global analyse_window
    global output
    analyse_window = Tk()
    analyse_window.title('InstRoamer')
    output = Text(analyse_window)
    output.pack()
    analyse_window.after(500, analyse)
    analyse_window.mainloop()

start_button = Button(root, text = 'Start!', command = start)
start_button.pack(side = 'bottom')
checkbox.pack(side = 'top')

def analyse():
    #d=datetime.today()
    #fout = open(d.strftime('%y_%m_%d')+'.txt', 'w')
    rated_users =[]
    with open('usernames.txt', 'r') as fin:
        for name in fin:
            name = name.split()[0].lower()
            user = InstagramUser(name)
            if user.username is None:
                output.insert('0.0', 'Error '+ name + '\n')
                continue
            output_str = ''
            for i in user.getOnlyRate():
                output_str += str(i) + (20-len(user.username))*' '
            output.insert('0.0', output_str + '\n')
                #print(i, end = ' ', file = fout)
            #print(file = fout)
            rated_users.append(user.getOnlyRate())
            analyse_window.update()
    if is_rating_saved:
        rated_users.sort(key = lambda userinfo: userinfo[1])
        with open('rating.txt','w') as frating:
            for sorted_user in rated_users:
                print(sorted_user[0], sorted_user[1], file = frating)
    #fout.close()
    output.insert('0.0', 'Analyse over\n')
root.mainloop()

