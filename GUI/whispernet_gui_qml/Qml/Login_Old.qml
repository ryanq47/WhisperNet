import QtQuick
import QtQuick.Controls

Window {
    visible: false  // Initially hidden, shown programmatically
    width: 300
    height: 200
    title: "Floating Window"

    Rectangle {
        id: rectangle
        color: "#ffffff"
        anchors.fill: parent

        Column {
            id: column
            anchors.fill: parent
            spacing: 5
            TextField {
                id: usernameField
                width: 200
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
}
