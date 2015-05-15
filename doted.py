import signal
import sys

import tkinter as tk

from graph import GraphicsGraph
from node import GraphicsNode

signal.signal(signal.SIGINT, signal.SIG_DFL)
    
class MyCanvas(tk.Canvas):

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.bind("<Double-Button-1>", self.createNode)

    def createNode(self, event):
        # self.create_oval(event.x, event.y, event.x+50, event.y+50)
        GraphicsNode(self, event.x, event.y)
        
        
class MyWindow(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def handleClear(self):
        for obj in self.canvas.find_all():
            self.canvas.delete(obj)

    def createWidgets(self):
        self.clearButton = tk.Button(self)
        self.clearButton["text"] = "Clear"
        self.clearButton["command"] = self.handleClear
        self.clearButton.pack(side="bottom")

        self.canvas = MyCanvas(self)
        self.canvas.pack(side="top")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MyWindow(master=root)
    app.mainloop()
