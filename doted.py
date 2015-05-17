import signal
import sys

import tkinter as tk

from node import GraphicsNode

signal.signal(signal.SIGINT, signal.SIG_DFL)
    
class MyCanvas(tk.Canvas):

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.bind("<Double-Button-1>", self.doubleClickHandler)
        self.nodes = dict()

    def doubleClickHandler(self, event):
        # closest_items = self.find_closest(event.x, event.y, halo=10)
        closest_items = self.find_overlapping(event.x-5, event.y-5, event.x+5, event.y+5)
        if closest_items == ():
            node = GraphicsNode(self, event.x, event.y)
            for i in node.getIds():
                self.nodes[i] = node
        else:
            node = self.nodes[closest_items[0]]
            print(closest_items)
            node.editLabel()
            

        # else:
        #     #TODO : Dispatch
        #     self
        
        
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
