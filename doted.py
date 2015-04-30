import sys
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import *



class View(QGraphicsView):

    def __init__(self, parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene);
        self.setSceneRect(QRectF(self.viewport().rect()));
        
    def initUI(self):
        # self.setGeometry(300, 300, 280, 170)
        # # self.setWindowTitle('Points')
        # self.show()
        pass
    
    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton :
            pos = self.mapToScene(e.pos())
            self.scene.addEllipse(pos.x(), pos.y(), 20,10)

class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.view = View(self)
        self.button = QPushButton('Clear View', self)
        self.button.clicked.connect(self.handleClearView)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.button)
        self.show()

    def handleClearView(self):
        self.view.scene.clear()

    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
