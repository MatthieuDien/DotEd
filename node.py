import pydot_ng as pydot
from PyQt5.QtCore import Qt, QMimeData, QMarginsF
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsSimpleTextItem, QApplication, QGraphicsItem
import pickle

class GraphicsNode(QGraphicsEllipseItem):

    def __init__(self, parent, label=None, *args, **kwargs):
        QGraphicsEllipseItem.__init__(self, *args, **kwargs)
        self.text = "" if label == None else label
        self.gr_item = QGraphicsSimpleTextItem(self.text, self)
        self.setRect(self.gr_item.boundingRect().marginsAdded(QMarginsF(10,10,10,10)))
        self.parent = parent
        self.setFlags(QGraphicsItem.ItemIsMovable)

    def mouseMoveEvent(self, e):
        print("mov")
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            mimeData = QMimeData()
            drag = QDrag(e.widget())
            mimeData.setText("lol")
            drag.setMimeData(mimeData)
            drag.exec(Qt.MoveAction)
            self.ungrabMouse()

