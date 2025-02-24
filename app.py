from tkinter import Tk, Frame, Label, Button, StringVar, CENTER
import json
import os
import random
from flashcard import Flashcard  # Import Flashcard class

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard Quiz App")
        self.master.configure(bg="#FFFAF0")  # Light cream background
        self.master.geometry("600x400")  # Set fixed window size
        self.master.resizable(False, False)  # Disable resizing

        self.flashcards = self.load_flashcards()
        self.current_index = 0

        self.card_frame = Frame(self.master, bg="#FFFAF0")
        self.card_frame.pack(pady=20, padx=20, expand=True)

        self.question_var = StringVar()
        self.answer_var = StringVar()
        self.is_flipped = False

        self.question_label = Label(self.card_frame, textvariable=self.question_var, font=("Helvetica", 24), wraplength=400, bg="#FFFAF0", fg="#FF69B4", justify=CENTER)
        self.question_label.pack(pady=10)
        self.question_label.bind("<Button-1>", self.flip_card)

        button_style = {"bg": "#FFB6C1", "fg": "white", "font": ("Helvetica", 12, "bold"), "highlightbackground": "#FF69B4", "highlightthickness": 2}

        self.nav_frame = Frame(self.master, bg="#FFFAF0")
        self.nav_frame.pack(pady=10)

        self.prev_button = Button(self.nav_frame, text="Previous", command=self.prev_card, **button_style)
        self.prev_button.pack(side="left", padx=20)

        self.next_button = Button(self.nav_frame, text="Next", command=self.next_card, **button_style)
        self.next_button.pack(side="left", padx=20)

        self.shuffle_button = Button(self.master, text="Shuffle", command=self.shuffle_flashcards, **button_style)
        self.shuffle_button.pack(pady=10)

        self.show_question()

    def load_flashcards(self):
        with open(os.path.join(os.path.dirname(__file__), 'data', 'flashcards.json'), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Flashcard(item['question'], item['answer']) for item in data]

    def show_question(self):
        self.is_flipped = False
        self.question_var.set(self.flashcards[self.current_index].get_question())
        self.answer_var.set(self.flashcards[self.current_index].get_answer())

    def flip_card(self, event=None):
        if self.is_flipped:
            self.question_var.set(self.flashcards[self.current_index].get_question())
        else:
            self.question_var.set(self.flashcards[self.current_index].get_answer())
        self.is_flipped = not self.is_flipped

    def next_card(self):
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            self.show_question()

    def prev_card(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_question()

    def shuffle_flashcards(self):
        random.shuffle(self.flashcards)
        self.current_index = 0
        self.show_question()

if __name__ == "__main__":
    root = Tk()
    app = FlashcardApp(root)
    root.mainloop()