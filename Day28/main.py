from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


def count_time(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_time, count - 1)
    else:
        start_button_clicked()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for i in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


def start_button_clicked():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS < 9:
        if REPS % 8 == 0:
            count_time(long_break_sec)
            timer_label.config(text="Break", fg=RED)
        elif REPS % 2 == 0:
            count_time(short_break_sec)
            timer_label.config(text="Break", fg=PINK)
        else:
            count_time(work_sec)
            timer_label.config(text="Work", fg=GREEN)


def reset_button_clicked():
    canvas.after_cancel(timer)
    check_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 122, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 60, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_button_clicked, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_button_clicked, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
