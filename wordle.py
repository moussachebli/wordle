import tkinter as tk
from tkinter import *
import string
import random
import time

class Wordle(object):
    def __init__(self):
        self.blocks_placed = 0
        self.answer = self.create_answer()
    def create_answer(self):
        file_path = "wordle_answers.txt"
        with open(file_path, 'r') as file:
            word_list = file.read().splitlines()
        answer = random.choice(word_list)
        return answer
    
    def process_guess(self, entry, entry_text, label):
        guess = entry.get()
        if len(guess) == 5:
            print("Guess:", guess.upper())
            entry_text.set(guess.upper())
            self.create_block(label, guess.upper())
            return False  #return false to clear textbox after input
        else:
            print("Please enter a word with 5 letters.")
            return False  
        
    def create_block(self, label, guess):
        answer = self.answer.upper()
        #uncomment answer and choose 5 letter word as the answer to test game
        #answer = 
        check = set()
        for x in guess:
            check.add(x)
        for index, char in enumerate(guess.upper()):
            if char in answer:
                if char == answer[index]:
                    bg = "green"
                else:
                    if index < answer.index(char) or index > answer.index(char):
                        bg = "gray"
                        if guess.count(char) == 1:
                            bg = "yellow"
                    else:
                        bg = "yellow"
            else:
                bg = "gray"
            if self.blocks_placed < 40:
                block = tk.Label(
                label,
                text=char,
                bg=bg,
                width=2,
                height=1,
                relief=tk.RAISED,
                fg = "black"
                )
                block.config(font = ('Helvetica', 14))
                block.pack(side = tk.LEFT, padx = (1, 0))
                x_coord = 170 + (self.blocks_placed % 5) * 22
                y_coord = 30 + (self.blocks_placed // 5) * 32
                block.place(x=x_coord, y=y_coord)
                self.blocks_placed+=1   
            else:
                block = tk.Label(
                label,
                text = "YOU LOSE! ",
                bg = 'white',
                width = 35,
                height = 6,
                relief = tk.RAISED,
                fg = 'black'
                )
                block.config(font = ('Helvetica', 14))
                block.pack(side = tk.LEFT, padx = (1, 0))
                x_coord = 120
                y_coord = 250
                block.place(x=x_coord, y=y_coord)
                self.blocks_placed+=1
            if self.blocks_placed % 5 == 0 and answer == guess:
                block = tk.Label(
                label,
                text = "YOU WIN!!!",
                bg = "yellow",
                width = 40,
                height = 10,
                relief = tk.RAISED,
                fg = "black"
                )
                block.config(font = ('Helvetica', 14))
                block.pack(side = tk.LEFT, padx = (1, 0))
                x_coord = x_coord-180
                y_coord += 30
                block.place(x=x_coord, y=y_coord)
                self.blocks_placed+=1
                time.sleep(3)
                Button(label, text="Quitx", command=mainloop.destroy).pack()
            
    def mainloop(self):
        window = tk.Tk()
        height = 600
        width = 500
        background_color = '#aace9c'

        # Entry widget for user input
        entry_text = tk.StringVar()
        entry = tk.Entry(window, textvariable=entry_text)
        entry.pack()

        label = tk.Frame(
            window,
            height=height, 
            width=width, 
            background=background_color
        )
        label.pack(pady=10)
        label.pack_propagate(False)

        # Button to process the guess
        def submit_guess():
            guess = entry.get()
            if not self.process_guess(entry, entry_text, label):
                entry.delete(0, tk.END)  # Clear entry after user enters
                entry.focus_set()  # Keep focus on entry for the next guess
        
        # Function to handle keyboard button clicks
        '''def key_click(char):
            entry.insert(tk.END, char)
        
        # Create keyboard buttons
        keyboard_frame = tk.Frame(window)
        keyboard_frame.pack()

        for char in string.ascii_uppercase:
            button = tk.Button(
                keyboard_frame,
                text=char,
                command=lambda c=char: key_click(c)
            )
            button.grid(row=0, column=ord(char) - ord('A'))'''

        # Submit button
        submit_button = tk.Button(
            window,
            text='Submit',
            command=submit_guess
        )
        submit_button.pack()
        
        window.mainloop()

instance = Wordle()
instance.mainloop()            
