// DraggableItem.qml
import QtQuick
import QtQuick.Controls

//A playaround draggable item. Maybe use this as a plugin template
Item {
    id: draggableItem
    width: 500
    height: 500
    visible: true

    // You can add other properties and visual elements here
    Rectangle {
        width: parent.width
        height: parent.height

        Column {
            id: column
            anchors.fill: parent
            spacing: 5
            TextField {
                id: usernameField
                width: 200
                color: "black"
                height: 30
                placeholderText: qsTr("Username")
            }
            TextField {
                id: passwordField
                width: 200
                height: 30
                placeholderText: qsTr("Password")
            }

            Button {
                id: loginButton

                width: 200
                height: 30
                text: qsTr("Log In")
            }
        }
    }

    Button {
        id: closePopupButton
        //what to anchor //where to anchor to/in ref from
        anchors.top: draggableItem.top
        anchors.right: draggableItem.right
        text: "Close"
    }
}
