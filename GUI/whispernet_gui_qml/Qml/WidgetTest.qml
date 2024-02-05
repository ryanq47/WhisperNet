// CustomDevWidget.qml
import QtQuick 2.0
import QtQuick.Controls
//DO NOT call Item. has to be DevWidget
DevWidget {
    widgetName: "CustomDevWidget"

    // Override properties or add new functionality
    Component.onCompleted: {
        console.log(widgetName + " is ready.");
    }

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


//kinda fucked buty keep playign wtih ti
