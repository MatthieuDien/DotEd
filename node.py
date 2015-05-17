from PyQt5.QtCore import Qt, QMimeData, QMarginsF
from PyQt5.QtGui import QDrag, QTransform
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem, QApplication, QGraphicsItem
from edge import GraphicsSemiEdge, GraphicsEdge

class GraphicsTextItem(QGraphicsTextItem):

    def __init__(self, *args, **kwargs):
        QGraphicsTextItem.__init__(self, *args, **kwargs)

    def keyPressEvent(self, e):
        QGraphicsTextItem.keyPressEvent(self, e)
        self.parentItem().update()

    def mousePressEvent(self, e):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            e.ignore()
        else:
            for item in self.scene().selectedItems():
                item.setSelected(False)
            QGraphicsTextItem.mousePressEvent(self, e)

    def mouseMoveEvent(self, e):
        parent = self.parentItem()
        if parent.edgeInConstruction == None:
            parent.buildEdge(parent.scenePos())
        parent.mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        self.parentItem().mouseReleaseEvent(e)
        
class GraphicsNode(QGraphicsEllipseItem):

    def __init__(self, label = ""):
        QGraphicsEllipseItem.__init__(self)
        self.text = label
            
        self.textItem = GraphicsTextItem(self.text, parent = self)
        self.textItem.setTextInteractionFlags(Qt.TextEditorInteraction)
        
        self.setRect(self.textItem.boundingRect().marginsAdded(QMarginsF(10,10,10,10)))
        self.setFlags(QGraphicsItem.ItemIsSelectable)
        
        self.observers = set()
        self.edgeInConstruction = None
        
    def mouseMoveEvent(self, e):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            mimeData = QMimeData()
            drag = QDrag(e.widget())
            mimeData.setText("node")
            drag.setMimeData(mimeData)
            drag.exec_(Qt.MoveAction)
            self.ungrabMouse()
        if self.edgeInConstruction != None:
            self.edgeInConstruction.obsUpdate(e.scenePos())

    def buildEdge(self, pos):
        self.edgeInConstruction = GraphicsSemiEdge(self, pos)
        self.scene().addItem(self.edgeInConstruction)
            
    def mousePressEvent(self, e):
        modifiers = QApplication.keyboardModifiers()        
        if modifiers == Qt.NoModifier:
            for item in self.scene().selectedItems():
                item.setSelected(False)
            self.setSelected(True)
            self.buildEdge(e.scenePos())

    def mouseReleaseEvent(self, e):
        if self.edgeInConstruction != None:
            self.scene().removeItem(self.edgeInConstruction)
            self.observers.remove(self.edgeInConstruction)
            self.edgeInConstruction = None
            items = [it for it in self.scene().items(e.scenePos()) if isinstance(it, GraphicsNode)]
            if len(items) != 0:
                self.scene().addItem(GraphicsEdge(self, items[0]))
            
    def mouseDoubleClickEvent(self, e):
        self.scene().removeItem(self.edgeInConstruction)
        self.edgeInConstruction = None

    def update(self, *args, **kwargs):
        self.setRect(self.textItem.boundingRect().marginsAdded(QMarginsF(10,10,10,10)))
        QGraphicsEllipseItem.update(self, *args, **kwargs)
        
    def paint(self, *args, **kwargs):
        QGraphicsEllipseItem.paint(self, *args, **kwargs)
        for obs in self.observers:
            obs.obsUpdate()

    def addObserver(self, obs):
        if obs not in self.observers:
            self.observers.add(obs)

    def delObserver(self, obs):
        if obs in self.observers:
            self.obervers.remove(obs)

    def removeEdges(self):
        for obs in self.observers:
            self.scene().removeItem(obs)
        self.observers = set()
