from tkinter import ttk
import tkinter as tk

class GraphicsNode:
    def __init__(self, parent, x, y, text="lolilol"):
        self.parent = parent
        self.x = x
        self.y = y
        self.text = text
        self.vc = self.parent.register(self.redraw)
        self.draw()

    def draw(self):
        self.entry = ttk.Entry(self.parent, textvariable=tk.StringVar(), validate='all', validatecommand=(self.vc,), width=len(self.text))
        self.window_id = self.parent.create_window(self.x, self.y, window=self.entry)
        (x,y) = self.entry.bbox()
        self.oval_id = self.parent.create_oval(self.x-x/2, self.y-y/2, self.x+x/2, self.y+y/2)
        self.entry.insert(0, self.text)
        self.redraw()

    def redraw(self):
        text = self.entry.get()
        # print(text)
        self.entry["width"] = len(text)
        return True
