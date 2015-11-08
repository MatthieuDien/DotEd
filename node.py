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
        self.text_id = self.parent.create_text(self.x, self.y, text=self.text)

#ttk.Entry(self.parent, textvariable=tk.StringVar(), validate='all', validatecommand=(self.vc,), width=len(self.text))
        # self.window_id = self.parent.create_window(self.x, self.y, window=self.entry)
        (x1, y1, x2, y2) = self.parent.bbox(self.text_id)
        self.oval_id = self.parent.create_oval(x1-10, y1-10, x2+10, y2+10)
        # self.entry.insert(0, self.text)
        # self.redraw()

    def redraw(self, code, reason):
        print("code : ", code, " reason : ", reason, " typcode : ", type(code), " typreason : ", type(reason))
        if code == "-1" and reason == "focusout":
            print("coucou")
            self.text = self.entry.get()
            print(self.text)
            # self.entry["width"] = len(text)
            self.parent.delete(self.oval_id)
            self.parent.delete(self.window_id)
            self.entry.destroy()
            self.text_id = self.parent.create_text(self.x, self.y, text=self.text)
            (x1, y1, x2, y2) = self.parent.bbox(self.text_id)
            self.oval_id = self.parent.create_oval(x1-10, y1-10, x2+10, y2+10)
        elif code == 0 or code == 1:
            self.entry["width"] = len(self.entry.get())

        return True

    def editLabel(self):
        self.entry = ttk.Entry(self.parent, textvariable=tk.StringVar(), validate='all', validatecommand=(self.vc,"%d","%V"), width=len(self.text))
        self.entry.bind("<Return>", lambda e : self.redraw("-1", "focusout"))
        self.window_id = self.parent.create_window(self.x, self.y, window=self.entry)
        self.entry.insert(0, self.text)
        self.entry["width"] = len(self.text)
        self.redraw(-1,"focusout")
        self.parent.delete(self.oval_id)
        self.parent.delete(self.text_id)
        (x1, y1, x2, y2) = self.parent.bbox(self.window_id)
        self.oval_id = self.parent.create_oval(x1-10, y1-10, x2+10, y2+10)
        # print("coucou")

    def getIds(self):
        return [self.oval_id, self.text_id]
