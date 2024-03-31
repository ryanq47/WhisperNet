from PySide6.QtWidgets import QDialog, QWidget

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

def open_popup_widget(widget_class: type[QWidget], parent=None):
    """
    Opens a pop-up widget based on the specified >>>QWidget<<< subclass.
    
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
