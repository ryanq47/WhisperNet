import QtQuick
import QtQuick.Controls 5.15

Item {
    id: item1

    Rectangle {
        id: rectangle
        color: "#ffffff"
        anchors.fill: parent

        Button {
            id: button
            x: 565
            y: 440
            width: 67
            height: 32
            text: qsTr("Button")
            anchors.right: parent.right
            anchors.bottom: parent.bottom
        }

        TextArea {
            id: textArea
            x: 8
            y: 8
            width: 624
            height: 426
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            placeholderText: qsTr("Text Area")
        }
    }

    TextField {
        id: textField
        x: 8
        y: 440
        width: 555
        height: 32
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        placeholderText: qsTr("Text Field")
    }
}
