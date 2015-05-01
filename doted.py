import signal
import sys
import pickle

from PyQt5.QtCore import Qt, QRectF, QMarginsF
from PyQt5.QtWidgets import *

from node import GraphicsNode

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Scene(QGraphicsScene):
    def __init__(self, *args, **kwargs):
        QGraphicsScene.__init__(self, *args, **kwargs)

    def mouseDoubleClickEvent(self, e):
        print("click")
        print(e.scenePos().x())

        if e.button() == Qt.LeftButton :
            pos = e.scenePos()
            ellipse = GraphicsNode(self, label="lolilol")
            ellipse.setPos(pos)
            self.addItem(ellipse)

    def dragEnterEvent(self, e):
        print("drag enter")
        print(e.mimeData().formats())
        e.acceptProposedAction()
        
    def dragMoveEvent(self, e):
        self.mouseGrabberItem().setPos(e.scenePos())
        self.update()        
    
    def dropEvent(self,e):
        self.mouseGrabberItem().setPos(e.scenePos())
        self.update()
    
class View(QGraphicsView):

    def __init__(self, parent):
        super().__init__(parent)
        self.scene = Scene(self)
        self.setScene(self.scene);
        self.setSceneRect(QRectF(self.viewport().rect()));
        
class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.view = View(self)
        self.button = QPushButton('Clear View', self)
        self.button.clicked.connect(self.handleClearView)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.button)
        self.setGeometry(800, 800, 800, 800)
        self.show()

    def handleClearView(self):
        self.view.scene.clear()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
