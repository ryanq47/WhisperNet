import QtQuick.Window

import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true

    Rectangle {
        id: rectangle
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
}
