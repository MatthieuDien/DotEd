from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import Qt
from node import GraphicsNode

class GraphicsGraph(QGraphicsScene):
    def __init__(self, *args, **kwargs):
        QGraphicsScene.__init__(self, *args, **kwargs)

    def mouseDoubleClickEvent(self, e):
        print("click")
        print(e.scenePos().x())

        if e.button() == Qt.LeftButton :
            pos = e.scenePos()
            ellipse = GraphicsNode(label="lolilol")
            ellipse.setPos(pos)
            self.addItem(ellipse)

    def dragEnterEvent(self, e):
        print(e.mimeData().formats())
        if e.mimeData().hasText() :
            if e.mimeData().text() == "node":
                e.acceptProposedAction()
            else :
                e.ignore()
        else:
            e.ignore()        
                
    def dragMoveEvent(self, e):
        if e.mimeData().hasText() :
            if e.mimeData().text() == "node":
                self.mouseGrabberItem().setPos(e.scenePos())
                self.update()
            else :
                e.ignore()
        else :
            e.ignore()
    
    def dropEvent(self,e):
        if e.mimeData().hasText() :
            if e.mimeData().text() == "node":
                self.mouseGrabberItem().setPos(e.scenePos())
                self.update()
            else :
                e.ignore()
        else :
            e.ignore()
