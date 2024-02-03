import QtQuick
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: draggableItem
    visible: true
    title: "Log into Server"

    //REctangle purely for gradient/styles
    Rectangle {
        anchors.fill: parent

        gradient: Gradient {
            GradientStop { position: 0.0; color: Style.gradientTop } //color: "#53A2E6" }
            GradientStop { position: 1.0; color: Style.gradientBottom } //color: "#133451" }
        }

        // Use a Layout to allow dynamic resizing
        ColumnLayout {
            anchors {
                fill: parent
                margins: 5
            }
            spacing: 5

            Text {
                Layout.fillWidth: true
                text: "<b>Login Form</b>"
                height: 30
            }

            TextField {
                Layout.fillWidth: true
                placeholderText: qsTr("Server")
                height: 30
            }

            TextField {
                Layout.fillWidth: true
                placeholderText: qsTr("Username")
                height: 30
            }

            TextField {
                Layout.fillWidth: true
                placeholderText: qsTr("Password")
                height: 30
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Log In")
                height: 30
                onClicked: {
                    console.log(authentication) // Should not be undefined
                    console.log(authentication.login) // Should not be undefined

                    authentication.login.to_server("test","test","test")
                }
            }
        }
    }


}
