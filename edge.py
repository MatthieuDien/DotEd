from PyQt5.QtCore import QLineF, QPointF
from PyQt5.QtWidgets import QGraphicsLineItem
from PyQt5.QtGui import QPen

def closestPointTo(point, path):
    target = path.boundingRect().center()
    mid = (point + target) / 2.
    
    if path.contains(mid):
        while path.contains(mid) :
            target = mid
            mid = (point + target) / 2.
            
    else:
        while (mid-point).manhattanLength() > 1:
            while not path.contains(mid) :
                point = mid
                mid = (point + target) / 2.

            while path.contains(mid) :
                mid = (point + mid) /2.
    return mid

class GraphicsEdge(QGraphicsLineItem):

    def __init__(self, startNode, endNode):
        QGraphicsLineItem.__init__(self)
        self.setPen(QPen())
                
        self.startNode = startNode
        self.endNode = endNode

        self.startNode.addObserver(self)
        self.endNode.addObserver(self)

        startShape = self.startNode.mapToScene(self.startNode.shape())
        endShape = self.endNode.mapToScene(self.endNode.shape())

        p1 = closestPointTo(startShape.boundingRect().center(), endShape)
        p2 = closestPointTo(endShape.boundingRect().center(), startShape)
                
        self.setLine(QLineF(p1, p2))
        
    def obsUpdate(self):
        startShape = self.startNode.mapToScene(self.startNode.shape())
        endShape = self.endNode.mapToScene(self.endNode.shape())
        
        p1 = closestPointTo(startShape.boundingRect().center(), endShape)
        p2 = closestPointTo(endShape.boundingRect().center(), startShape)

        self.setLine(QLineF(p1, p2))
