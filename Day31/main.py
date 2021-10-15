from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")


def generate_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    french_word = current_card["French"]
    main_canvas.itemconfig(canvas_title, text=f"French", fill="black")
    main_canvas.itemconfig(canvas_word, text=f"{french_word}", fill="black")
    main_canvas.itemconfig(canvas_image, image=card_front)
    timer = window.after(3000, func=flip_card)


def flip_card():
    english_word = current_card["English"]
    main_canvas.itemconfig(canvas_image, image=card_back)
    main_canvas.itemconfig(canvas_title, text=f"English", fill="white")
    main_canvas.itemconfig(canvas_word, text=f"{english_word}", fill="white")


def remove_word():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

main_canvas = Canvas(width=820, height=540, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_image = main_canvas.create_image(410, 275, image=card_front)
canvas_title = main_canvas.create_text(400, 170, font=("Ariel", 40, "italic"), text="")
canvas_word = main_canvas.create_text(400, 270, font=("Ariel", 60, "bold"), text="")
main_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1, padx=50)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1, padx=50)

generate_word()

mainloop()
