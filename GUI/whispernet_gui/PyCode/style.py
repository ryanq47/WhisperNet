from PySide6.QtCore import QObject, Property
import random
## Styles

class Style(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main colors stuff
        self._gradientBottom = "#000000"
        self._gradientGunMetalGrey = "#595857"
        self._primaryColor = "#4285F4"
        self._accentColor = "#DB4437"

        ## Font stuff
        self._defaultFontSize = 14
        self._defaultFontFamily = "monospace"

        ## Rando Colors
        self._gradientTopBlue = "#6A8CAF"
        self._gradientTopGreen = "#8CA96A"
        self._gradientTopRed = "#A9686A"
        self._gradientTopGreySilver = "#A0A0A0"  # Muted Silver-Grey

        ## Toolbar
        self._toolbarColor = "#444"

        ## Widget Stuff
        self._closeButtonColor = "#CB4C4E"

    @Property(str)
    def primaryColor(self):
        #return self._primaryColor
        return self._gradientGunMetalGrey

    @Property(str)
    def accentColor(self):
        return self._accentColor

    @Property(int)
    def defaultFontSize(self):
        return self._defaultFontSize

    @Property(str)
    def gradientTop(self):
        return self._gradientGunMetalGrey # Non Random
        #return random.choice([self._gradientTopBlue, self._gradientTopGreen, self._gradientTopRed, self._gradientTopGreySilver])

    @Property(str)
    def gradientBottom(self):
        #return self._gradientGunMetalGrey
        return self._gradientBottom


    @Property(str)
    def closeButton(self):
        return self._closeButtonColor


    @Property(str)
    def buttonColor(self):
        #return self._gradientGunMetalGrey
        return self._gradientGunMetalGrey

    @Property(str)
    def buttonColor(self):
        #return self._gradientGunMetalGrey
        return self._toolbarColor

    @Property(str)
    def fontFamily(self):
        #return self._gradientGunMetalGrey
        return self._defaultFontFamily
