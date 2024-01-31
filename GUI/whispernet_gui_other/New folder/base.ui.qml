

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import UntitledProject

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    border.color: "#000000"
    gradient: Gradient {
        GradientStop {
            position: 0
            color: "#3a3a3a"
        }

        GradientStop {
            position: 1
            color: "#5364a5"
        }
        orientation: Gradient.Vertical
    }

    TabBar {
        id: tabBar
        x: 8
        y: 36
        width: 240
    }

    ToolBar {
        id: toolBar
        x: 0
        y: 0
        width: 1920
        height: 36
        opacity: 1
        visible: true
        position: ToolBar.Header
        clip: false

        Button {
            id: button1
            x: 0
            width: 81
            height: 36
            text: qsTr("File")
            anchors.top: parent.top
            anchors.topMargin: 0
        }

        Button {
            id: button2
            x: 87
            width: 81
            height: 36
            text: qsTr("View")
            anchors.top: parent.top
            anchors.topMargin: 0
        }

        Button {
            id: button3
            x: 174
            width: 81
            height: 36
            text: qsTr("Menu")
            anchors.top: parent.top
            anchors.topMargin: 0
        }
    }

    Button {
        id: button
        x: 1885
        width: 35
        height: 35
        text: qsTr("Exit")
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 0
        anchors.topMargin: 1
        icon.cache: true
        icon.color: "#ff0404"
        autoExclusive: false
        checkable: false
        flat: false
    }
}
