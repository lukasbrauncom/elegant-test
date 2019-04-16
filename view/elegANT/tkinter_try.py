import tkinter as tk
from tkinter import Tk
import tkinter.colorchooser as color_chooser

class _start_view_:
    def __init__(self, master):
        self.master = master
        master.title("elegAnt")

        self.label = tk.Label(master, text="elegANT, the Game!")
        self.label.grid(row=0,column=0, padx=5, pady=5)
        self.str_username = tk.StringVar()
        self.str_username.set("please enter your name")
        self.username = tk.Entry(master, textvariable=self.str_username)
        self.username.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.color_button = tk.Button(master, text='Color?', command=self.get_color)
        self.color_button.grid(row=1, column=3, padx=5, pady=5, sticky='W')

        self.start_button = tk.Button(master, text="Start", command=self.start, highlightcolor="green")
        self.start_button.grid(row=2, column=0, padx=5, pady=5, sticky='W')

        self.close_button = tk.Button(master, text="Close", command=master.quit, highlightcolor="red")
        self.close_button.grid(row=2, column=1, padx=5, pady=5, sticky='E')

    def start(self):
        if self.str_username.get() == "please enter your name":
            print('That is not your name!')
        else:
            print('is your name really', self.str_username.get(), '?')

    def get_color(self):
        color = color_chooser.askcolor()
        print(color)


if __name__ == "__main__":
    root = Tk()
    my_gui = _start_view_(root)
    root.mainloop()