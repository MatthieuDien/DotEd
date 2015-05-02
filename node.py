import pydot_ng as pydot
from PyQt5.QtCore import Qt, QMimeData, QMarginsF
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsSimpleTextItem, QApplication, QGraphicsItem

class GraphicsNode(QGraphicsEllipseItem):

    def __init__(self, label = ""):
        QGraphicsEllipseItem.__init__(self)
        self.text = label
            
        self.gr_item = QGraphicsSimpleTextItem(self.text, self)
        self.setRect(self.gr_item.boundingRect().marginsAdded(QMarginsF(10,10,10,10)))
        self.setFlags(QGraphicsItem.ItemIsMovable)

    def mouseMoveEvent(self, e):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            mimeData = QMimeData()
            drag = QDrag(e.widget())
            mimeData.setText("node")
            drag.setMimeData(mimeData)
            drag.exec(Qt.MoveAction)
            self.ungrabMouse()

