from tkinter import *
import math

running = False
reps = 0
"""#-----------------------CONSTANTS=------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd#"
FONT_NAME = "Courier"
"""
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None 


#----------------TIMER RESET--------------------------#


#--------------TIMER MECHANISM-----------------------#
def reset_timer():
    global running 
    window.after_cancel(timer)
    canvas.itemconfig(timer_label, text="00:00")
    title_label.config(text="Timer")
    tick.config(text="")
    running = False


#-------------------COUNTDOWN MECHANISM--------------#
#function for start timer    
def start_timer():
    global running, reps
    
    if running is True:  # Prevents multiple timers from starting
        return
    else:
        running = True
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        reps += 1
        if reps % 8 == 0:
            count_down(long_break_sec) 
            title_label.config(text="Break", bg="#e2979c", background="#e7305b")
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Break", bg="#e2979c", background="#e7305b" )
        else:
            count_down(work_sec)
            title_label.config(text="Work", bg="#9bdeac",background="#e7305b")
def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_label, text=f"{count_min:02d}:{count_sec:02d}")  
    if count > 0:
        global timer
        timer= window.after(1000, count_down, count-1)  #  Keep updating the countdown
    else:
        global running
        running = False
        start_timer()  # Start next session
        mark = ""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick.config(text=mark)  
            
#----------------------UI SETUP-----------------------#
window = Tk()
window.title("Pomodororo")
window.config(padx= 100, pady=50, bg="#e7305b")

img_width = 200
img_height = 200

canvas = Canvas(width=img_width, height=img_height,bg="#e7305b", highlightbackground="#e7305b")
# canvas.pack(expand=True)
poro_img = PhotoImage(file="toma.png")
# Center the image properly
canvas.create_image(img_width//2, img_height//2, image=poro_img)

#Create the text and align it 
timer_label = canvas.create_text(img_width//2, img_height//2, text="00:00", font= ("Courier",27, "bold"), fill= "white")
canvas.grid(column=1, row=1)

#CREATE TIMER NAME 
title_label  = Label(text="TIMER", fg="green",bg= "#e7305b", font=("Arial", 30))
title_label.grid(column=1, row=0)
            
 
#CREATE THE START TICK
strt_btn = Button(text="Start",highlightbackground="#e7305b", font="arial", command=start_timer)
strt_btn.grid(column=0, row= 2)
 

#CREATE THE RESET BUTTON
res_btn = Button(text="Reset",highlightbackground="#e7305b", font= "Courier", command=reset_timer)
res_btn.grid(column=2, row= 2)


#CREATE THE TICKS
tick = Label(fg="green", bg="#e7305b")
tick.grid(column=1, row=3)





window.mainloop()