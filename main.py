from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("./data/french_words.csv")
french_words = df.to_dict(orient='records')
random_word = None


def flip_card():
    canvas.itemconfig(lang_text, text="English")
    canvas.itemconfig(canvas_image, image=back_photo)
    global random_word
    canvas.itemconfig(word_text, text=random_word['English'])


def generate_word():
    canvas.itemconfig(lang_text, text="French")
    canvas.itemconfig(canvas_image, image=front_photo)
    global random_word
    random_word = random.choice(french_words)
    canvas.itemconfig(word_text, text=random_word['French'])
    window.after(3000, flip_card)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_photo)
lang_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, pady=50)

correct_button_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=generate_word)
correct_button.grid(column=0, row=2)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=1, row=2)

generate_word()

window.after(3000, flip_card)

window.mainloop()
