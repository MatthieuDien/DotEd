import signal
import sys

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QApplication, QGraphicsView, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QCursor
from graph import GraphicsGraph
from node import GraphicsNode

signal.signal(signal.SIGINT, signal.SIG_DFL)
    
class View(QGraphicsView):

    def __init__(self, parent):
        super().__init__(parent)
        self.scene = GraphicsGraph(self)
        self.setScene(self.scene);
        self.setSceneRect(QRectF(self.viewport().rect()));
        
class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.view = View(self)
        self.view.setMouseTracking(True)
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
