from PySide6.QtCore import QObject, Property
## Styles

class Style(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._primaryColor = "#4285F4"
        self._accentColor = "#DB4437"
        self._defaultFontSize = 14

        self._gradientTop = "#53A2E6"
        self._gradientBottom = "#133451"


    @Property(str)
    def primaryColor(self):
        return self._primaryColor

    @Property(str)
    def accentColor(self):
        return self._accentColor

    @Property(int)
    def defaultFontSize(self):
        return self._defaultFontSize

    @Property(str)
    def gradientTop(self):
        return self._gradientTop

    @Property(str)
    def gradientBottom(self):
        return self._gradientBottom
