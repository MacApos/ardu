import random
from tkinter import *
from tkinter import filedialog

root = Tk()
root.minsize(310, 245)

def callback0(*args):
    slide = slider0_var.get()
    if slide:
        slider0.set(int(slide))


def slide0(*args):
    pos0.delete(0, END)
    pos0.insert(0, str(slider0.get()))


def callback1(*args):
    slide = slider1_var.get()
    if slide:
        slider1.set(int(slide))


def slide1(*args):
    pos1.delete(0, END)
    pos1.insert(0, str(slider1.get()))


def callback2(*args):
    slide = slider2_var.get()
    if slide:
        slider2.set(int(slide))


def slide2(*args):
    pos2.delete(0, END)
    pos2.insert(0, str(slider2.get()))


def run():
    global saved_pos
    saved_pos = [int(pos.get()) for pos in [pos0, pos1, pos2]]
    print(saved_pos)


def record():
    global saved_pos
    setup = []
    for pos in positions:
        setup.append(int(pos.get()))
    saved_pos.append(setup)
    print(saved_pos)


def play():
    global saved_pos
    print(f'List of saved position = {saved_pos}')


def restart():
    for pos in positions:
        pos.delete(0, END)
        pos.insert(0, '0')


def clear():
    saved_pos = []
    print(saved_pos)


def random_setup():
    saved_pos = []
    for pos in positions:
        random_setup = random.randint(0, 180)
        pos.delete(0, END)
        pos.insert(0, str(random_setup))
        saved_pos.append(pos.get())
    print(saved_pos)


def open_file():
    global saved_pos
    filepath = filedialog.askopenfilename()
    file = open(filepath, "r")
    data = file.read()
    saved_pos = eval(data)
    file.close()
    print(saved_pos)


def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    file.write(str(saved_pos))
    file.close()


saved_pos = []

button_wide = 13
entry_width = 15
label_width = 100
slider_width = 100

slider0_var = StringVar(value='0')
slider1_var = StringVar(value='0')
slider2_var = StringVar(value='0')

sliders_var = [slider0_var, slider1_var, slider2_var]
callback = [callback0, callback1, callback2]

for idx, slider_var in enumerate(sliders_var):
    slider_var.trace_add('write', callback[idx])

servo0 = Label(root, text='Servo1')
servo0.grid(row=0, column=0, sticky='ew')

servo1 = Label(root, text='Servo2')
servo1.grid(row=2, column=0, sticky='ew')

servo2 = Label(root, text='Servo3')
servo2.grid(row=4, column=0, sticky='ew')

pos0 = Entry(root, textvariable=slider0_var, width=entry_width)
pos0.grid(row=1, column=1, sticky='s')

pos1 = Entry(root, textvariable=slider1_var, width=entry_width)
pos1.grid(row=3, column=1, sticky='s', pady=3)

pos2 = Entry(root, textvariable=slider2_var, width=entry_width)
pos2.grid(row=5, column=1, sticky='s', pady=3)

slider0 = Scale(root, from_=0, to=360, orient=HORIZONTAL, length=slider_width, command=slide0)
slider0.grid(row=1, column=0)

slider1 = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=slider_width, command=slide1)
slider1.grid(row=3, column=0)

slider2 = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=slider_width, command=slide2)
slider2.grid(row=5, column=0)

run = Button(root, text='RUN', command=run, width=button_wide)
run.grid(row=6, column=0)

save = Button(root, text='RECORD', command=record, width=button_wide)
save.grid(row=6, column=1)

play = Button(root, text='PLAY', command=play, width=button_wide)
play.grid(row=6, column=2)

restart = Button(root, text='RESTART', command=restart, width=button_wide)
restart.grid(row=7, column=0, sticky='s')

clear = Button(root, text='CLEAR', command=clear, width=button_wide)
clear.grid(row=7, column=1)

random_setup = Button(root, text='RANDOM', command=random_setup, width=button_wide)
random_setup.grid(row=7, column=2, sticky='ew')

sliders = [slider0, slider1, slider2]
positions = [pos0, pos1, pos2]

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open File", command=open_file)
filemenu.add_command(label="Save File", command=save_file)


root.config(menu=menubar)

root.mainloop()

print(saved_pos)