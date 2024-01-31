import QtQuick
import QtQuick.Window
import QtQuick.Controls 5.15

Item {
    width: 1366
    height: 768
    visible: true

    Rectangle {
        id: base_rectangle
        //color: "#ffffff"
        anchors.fill: parent

        gradient: Gradient {
            GradientStop {
                position: 0.0
                color: "#53A2E6"
            }
            GradientStop {
                position: 1.0
                color: "#133451"
            }
        }
    }

    ToolBar {
        id: toolBar
        x: 0
        y: 0
        width: 1366
        height: 30

        Row {
            id: row
            anchors.fill: parent

            ToolButton {
                id: toolButton
                text: qsTr("File")
                height: 30
            }

            ToolButton {
                id: toolButton1
                text: qsTr("View")
                height: 30
            }
        }
    }
}
