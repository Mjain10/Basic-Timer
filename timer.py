from tkinter import *
import time

window = Tk()
window.title('Timer')
window.configure(background = "pale turquoise")

def countdown(): 
    timer = int(entry.get())
    time_up = "Time's up!"
    while timer >= 0:
        label_for_time['text'] = timer
        timer -= 1
        time.sleep(1)
        window.update()
    label_for_time['text'] = time_up

entry = Entry(window, width = 5)
entry.pack(side = TOP, expand=YES)

total_seconds = Label(window, fg = 'black', bg = 'pale turquoise', font = ("Comic Sans MS", 10), text = 'Total Seconds')
total_seconds.pack(fill=BOTH, expand=YES)

label_for_time = Label(window, fg = 'blue', bg = 'pale turquoise', font = ("Comic Sans MS", 30))
label_for_time.pack(fill=BOTH, expand=YES)

seconds_left = Label(window, fg = 'black', bg = 'pale turquoise', font = ("Comic Sans MS", 30), text = 'Seconds Left')
seconds_left.pack(fill=BOTH, expand=YES)

b = Button(window, fg = 'black', text = 'Start', font = ("Comic Sans MS", 20), command = countdown)
b.pack(side = BOTTOM, expand=YES)

window.mainloop()

