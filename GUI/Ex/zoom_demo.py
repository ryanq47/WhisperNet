from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter  # Import QPainter
import sys

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.scaleFactor = 1.15  # Define the zoom factor

    def wheelEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            # Check the direction of the scroll wheel
            if event.angleDelta().y() > 0:
                # Zoom in
                self.scale(self.scaleFactor, self.scaleFactor)
            else:
                # Zoom out
                self.scale(1 / self.scaleFactor, 1 / self.scaleFactor)
            event.accept()
        else:
            super().wheelEvent(event)

app = QApplication(sys.argv)

# Create a scene and add some items
scene = QGraphicsScene()
scene.addItem(QGraphicsRectItem(0, 0, 100, 100))

# Create a zoomable view
view = ZoomableGraphicsView(scene)
view.show()

sys.exit(app.exec())
