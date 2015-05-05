from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QTransform, QCursor
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
        item = self.focusItem()
        if item != None:
            item.mouseDoubleClickEvent(e)
        elif e.button() == Qt.LeftButton and self.itemAt(e.scenePos(), QTransform()) == None:
            pos = e.scenePos()
            ellipse = GraphicsNode(label="lolilol")
            ellipse.setPos(pos)
            self.addItem(ellipse)
        else:
            e.ignore()

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

    def keyPressEvent(self, e):
        items = self.selectedItems()
        if len(items) != 0:
            for item in items:
                if e.key() == Qt.Key_Delete :
                    if isinstance(item, GraphicsNode):
                        item.removeEdges()
                    self.removeItem(item)
        else:
            if self.focusItem() != None:
                self.focusItem().keyPressEvent(e)
