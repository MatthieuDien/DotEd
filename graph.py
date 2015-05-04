from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QTransform
from node import GraphicsNode
from edge import GraphicsEdge

class GraphicsGraph(QGraphicsScene):
    def __init__(self, *args, **kwargs):
        QGraphicsScene.__init__(self, *args, **kwargs)

        ellipse1 = GraphicsNode(label="lolilol")
        ellipse1.setPos(QPointF(-200,100))
        self.addItem(ellipse1)

        ellipse2 = GraphicsNode(label="lolilol")
        ellipse2.setPos(QPointF(200,100))
        self.addItem(ellipse2)

        edge = GraphicsEdge(ellipse1, ellipse2)
        self.addItem(edge)
        


    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton and self.itemAt(e.scenePos(), QTransform()) == None:
            pos = e.scenePos()
            ellipse = GraphicsNode(label="lolilol")
            ellipse.setPos(pos)
            self.addItem(ellipse)

    def dragEnterEvent(self, e):
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
