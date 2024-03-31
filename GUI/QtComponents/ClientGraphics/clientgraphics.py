from PySide6.QtWidgets import QWidget, QGraphicsItemGroup, QMessageBox, QGraphicsPixmapItem, QGraphicsItem, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt

class LabeledDraggablePixmapItem(QGraphicsItemGroup):
    def __init__(self, pixmap, label_text):
        super().__init__()

        # Create the pixmap item
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.addToGroup(self.pixmap_item)  # Add pixmap item to the group

        # Create the label item
        self.label_item = QGraphicsTextItem(label_text)
        self.addToGroup(self.label_item)  # Add text label to the group

        # Position the label below the pixmap
        label_x = self.pixmap_item.boundingRect().width() / 2 - self.label_item.boundingRect().width() / 2
        label_y = self.pixmap_item.boundingRect().height()
        self.label_item.setPos(label_x, label_y)

        # Enable item interaction
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def mousePressEvent(self, event):
        # Implement the right click action or any other interaction here
        super().mousePressEvent(event)

class ClientGraphics(QWidget):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui_file = loader.load('QtComponents/ClientGraphics/clientgraphics.ui', self)
        self.__ui_load()
        self.name = "ClientGraphics"

    def __ui_load(self):
        '''
        Load UI elements
        '''
        if self.ui_file is None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", errmsg)
            print(errmsg)
            return

        try:
            self.graphics_view = self.ui_file.findChild(QGraphicsView, "client_graphicsView")
            if not self.graphics_view:
                raise ValueError("GraphicsView not found in the UI file")

            self.scene = QGraphicsScene(self)
            self.graphics_view.setScene(self.scene)

            # Add interactive items to the scene
            self.add_draggable_item("Assets/root.png", 0, 0)
            self.add_draggable_item("Assets/client.png", 100, 100)

            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def add_draggable_item(self, icon_path, x, y, label="DefaultClientLabel"):
        pixmap = QPixmap(icon_path)
        item = LabeledDraggablePixmapItem(pixmap, label)
        item.setPos(x, y)
        self.scene.addItem(item)

