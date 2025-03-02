from tkinter import *
from tkinter import messagebox

running = False
reps = 0
timer = None  # Stores the reference to the countdown timer
#------------------ABOUT -----------------------------#
def show_about():
    about_message = (
        "This is a Pomodoro Timer.\n"
        "Created for people needing reminders and guidance in their time management.\n"
        "Happy working! \U0001F600"
    )
    
    messagebox.showinfo("About the Pomodoro Timer", about_message)
def show_help():
    messagebox.showinfo("Help",
        "Whatever time you set for your work session will be counted down from, "
        "with each work session followed by a break duration set by you.\n"
        "Additionally, there is a long break period after 4 work sessions.\n")
    
#----------------TIMER RESET--------------------------#
def reset_timer():
    global running, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_label, text="00:00")
    title_label.config(text="Timer")
    tick.config(text="")
    start_btn.config(state=NORMAL)
    running = False
    reps= 0
##MAKE THE INPUT BOXES TAKE TEXT AS THE USER WANTS TO RESET
    work_entry.config(state= NORMAL)
    long_break_entry.config(state= NORMAL)
    short_break_entry.config(state= NORMAL)

#-------------------COUNTDOWN MECHANISM--------------#
def start_timer():
    global running, reps

    if running:  # Prevents multiple timers from starting
        return

    try:
        work_min = int(work_entry.get())  # Get user input for work time
        short_break_min = int(short_break_entry.get())  # Get user input for short break
        long_break_min = int(long_break_entry.get())  # Get user input for long break
    except ValueError:
        title_label.config(text="Enter valid numbers!", fg="white")
        return  # Stop execution if input is invalid
    
    ##MAKE THE INPUT BOXES NOT TAKE TEXT TILL THEY ARE DISABLED
    work_entry.config(state= DISABLED)
    long_break_entry.config(state=DISABLED)
    short_break_entry.config(state=DISABLED)
    
    running = True
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60
    reps += 1

    if reps % 8 == 0:
        messagebox.showinfo("Start Of Long Break", "Your long break period has started, ENJOY!!!")
        count_down(long_break_sec)
        start_btn.config(state=DISABLED)
        title_label.config(text="Long Break", bg="#e7305b", fg="white")
        
    elif reps % 2 == 0:
        messagebox.showinfo("Start Of Short Break", "Your short break period has started, RELAX!!!")
        count_down(short_break_sec)
        start_btn.config(state=DISABLED)
        title_label.config(text="Short Break", bg="#e7305b", fg="white")
    else:
        messagebox.showinfo("Start Of Work Session", "Your work session has started")
        count_down(work_sec)
        start_btn.config(state=DISABLED)
        title_label.config(text="Work", bg="#e7305b", fg="white")

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_label, text=f"{count_min:02d}:{count_sec:02d}")  

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Keep updating the countdown every one second
    else:
        global running
        running = False
        
        # Lift the window to the top
        window.lift()
        
        # Show a message box indicating the session has ended
        messagebox.showinfo("Time's Up!", "Your session has ended. Time to take a break!")
        
        # Start the next session after the message box is closed
        start_timer()  # Start next session

        # Update check marks after work sessions
        mark = "✔" * (reps // 2)
        tick.config(text=mark)

#----------------------UI SETUP-----------------------#
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="#e7305b")

# Canvas for Timer
img_width, img_height = 200, 200
canvas = Canvas(width=img_width, height=img_height, bg="#e7305b", highlightbackground="#e7305b")
try:
    # Load the image in Tkinter
    poro_img = PhotoImage(file=("toma.png"))
    #poro_img = PhotoImage(file="toma.png")
    canvas.create_image(img_width//2, img_height//2, image=poro_img)
except TclError:
     # If the image file is not found, draw a rectangle
    canvas.create_rectangle(10, 10, img_width - 10, img_height - 10, fill="red", outline="black")
    canvas.create_text(img_width // 2, img_height // 2)
    
##TEXT IN THE TOMATO
timer_label = canvas.create_text(img_width//2, img_height//2, text="00:00", font=("Courier", 27, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Create a menu bar
menubar = Menu(window)
window.config(menu=menubar)

# Create a "Help" menu
help_menu = Menu(menubar, tearoff=0)  # tearoff=0 prevents the menu from being torn off
help_menu.add_command(label="Help", command=show_help)

# Create an "About" menu
about_menu = Menu(menubar, tearoff=0)
about_menu.add_command(label="About", command=show_about)

# Add the "Help" and "About" menus to the menubar
menubar.add_cascade(label="Help", menu=help_menu)
menubar.add_cascade(label="About", menu=about_menu)

# Timer Label
title_label = Label(text="TIMER", fg="white", bg="#e7305b", font=("Arial", 30))
title_label.grid(column=1, row=0)

# User Input Fields
Label(text="Work Time (min):", bg="#e7305b", fg="white").grid(column=0, row=3)
work_entry = Entry(width=5)
work_entry.grid(column=1, row=3)
work_entry.insert(0, "25")  # Default value

Label(text="Short Break (min):", bg="#e7305b", fg="white").grid(column=0, row=4)
short_break_entry = Entry(width=5)
short_break_entry.grid(column=1, row=4)
short_break_entry.insert(0, "5")  # Default value

Label(text="Long Break (min):", bg="#e7305b", fg="white").grid(column=0, row=5)
long_break_entry = Entry(width=5)
long_break_entry.grid(column=1, row=5)
long_break_entry.insert(0, "20")  # Default value

# Buttons
start_btn = Button(text="Start", highlightbackground="#e7305b", font="arial", command=start_timer)
start_btn.grid(column=0, row=6)

reset_btn = Button(text="Reset", highlightbackground="#e7305b", font="Courier", command=reset_timer)
reset_btn.grid(column=2, row=6)

# Check Marks
tick = Label(fg="green", bg="#e7305b", font=("Arial", 14))
tick.grid(column=1, row=7)

window.mainloop()
