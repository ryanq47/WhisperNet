from PySide6.QtWidgets import QDialog, QWidget, QMainWindow, QDockWidget
from PySide6.QtCore import Qt
from Utils.Logger import LoggingSingleton

#ahem... Totally not mostly chatGPT generated. :)

#logger = LoggingSingleton.get_logger()

class GuiUtils:
    @staticmethod
    def open_dialog(dialog_class: type[QDialog], parent=None):
        """
        Opens a dialog window based on the specified >>>QDialog<<< subclass.
        
        This function creates and shows a modal dialog instance from a given QDialog subclass. 
        It's designed to be a convenient way to display dialogs without needing to manage 
        their instantiation and execution repeatedly throughout your code.
        
        Parameters:
        - dialog_class: The QDialog subclass to instantiate and show.
        - parent: The parent widget of the dialog. Defaults to None.
        
        Usage Example:
        ```python
        class MyCustomDialog(QDialog):
            # Dialog implementation
        
        # To open the dialog:
        open_dialog(MyCustomDialog, self)
        ```
        
        :param dialog_class: The class (subclass of QDialog) that should be instantiated and displayed.
        :param parent: The parent widget of the dialog. Default is None.
        """
        dialog = dialog_class(parent)
        dialog.exec_()
    @staticmethod
    def open_popup_widget(widget_class: type[QWidget], parent=None):
        """
        Opens a pop-up (i.e. NEW WINDOW) widget based on the specified >>>QWidget<<< subclass.
        
        This function creates and shows a non-modal widget instance from a given QWidget subclass.
        It allows for the flexible display of widgets as standalone windows, which can be useful for
        various purposes such as showing additional information, settings, or auxiliary tools.
        
        Parameters:
        - widget_class: The QWidget subclass to instantiate and show.
        - parent: The parent widget of the pop-up widget. Defaults to None.
        
        Usage Example:
        ```python
        class MyPopUpWidget(QWidget):
            # Widget implementation
        
        # To show the widget as a pop-up:
        open_popup_widget(MyPopUpWidget, self)
        ```
        
        :param widget_class: The class (subclass of QWidget) that should be instantiated and displayed.
        :param parent: The parent widget of the pop-up widget. Default is None.
        """
        popup_widget = widget_class(parent)
        popup_widget.show()
    @staticmethod
    def open_dock_widget(widget_class, main_window: QMainWindow, widget_title: str):
        """
            Dynamically creates a dock widget and adds it to the specified QMainWindow.

            This utility function is designed to instantiate a widget from the given class, wrap it in a QDockWidget, and then dock it within the provided QMainWindow instance. It allows for dynamic addition of dock widgets to a main window, supporting modular application design.

            Parameters:
            - widget_class: The class of the widget to be instantiated and docked. This class must be a subclass of QWidget.
            - main_window: The QMainWindow instance to which the dock widget will be added.
            - widget_title: An optional title for the dock widget. If not provided, the function attempts to use the windowTitle of the instantiated widget, falling back to the class name if necessary.

            Usage:
                GUIUtils.open_dock_widget(MyCustomWidget, self, "My Custom Widget")

            Where 'MyCustomWidget' is a QWidget subclass, 'self' refers to the QMainWindow instance, and "My Custom Widget" is the optional title.
        """
        if not issubclass(widget_class, QWidget):
            raise ValueError("widget_class must be a subclass of QWidget")

        # Instantiate the widget from the provided class
        widget_instance = widget_class()

        # Use the provided title, the widget's window title, or the class name as fallback
        if not widget_title:
            widget_title = widget_instance.windowTitle() or widget_class.__name__

        # Create the QDockWidget with the determined title and add the widget instance to it
        dock_widget = QDockWidget(widget_title, main_window)
        dock_widget.setWidget(widget_instance)

        # Allow the dock widget to be moved and closed by the user
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
        dock_widget.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

        # Add the dock widget to the main window, docking it by default to the right side
        main_window.addDockWidget(Qt.RightDockWidgetArea, dock_widget)