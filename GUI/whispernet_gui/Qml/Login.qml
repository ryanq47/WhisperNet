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
                id: serverField
                Layout.fillWidth: true
                placeholderText: qsTr("Server")
                height: 30
            }

            TextField {
                id: usernameField
                Layout.fillWidth: true
                placeholderText: qsTr("Username")
                height: 30
            }

            TextField {
                id: passwordField
                Layout.fillWidth: true
                placeholderText: qsTr("Password")
                height: 30
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Log In")
                height: 30
                onClicked: {
                    //console.log(authentication) // Should not be undefined
                    //console.log(authentication.login) // Should not be undefined

                    //console.log("Auth object:", auth)  // Direct access check
                    console.log("Data object:", global_data)
                    console.log("Nested Auth object:", global_data.auth)

                    authentication.login.to_server(usernameField.text,passwordField.text,passwordField.text)
                    // due to it being ASYNC... this doesnt happen right away. need to maybe do a signal update? i dunno, this print part is not necessary anyways
                    //passwordField.text = global_data.auth.get_jwt()
                    //not getting set right
                    //console.log("JWT: ", global_data.auth.jwt)
                }


            }
            Button {
                Layout.fillWidth: true
                text: qsTr("show JWT not async")
                height: 30
                onClicked: {
                    authentication.login.to_server(usernameField.text,passwordField.text,passwordField.text)
                    // due to it being ASYNC... this doesnt happen right away. need to maybe do a signal update? i dunno, this print part is not necessary anyways
                    passwordField.text = global_data.auth.get_jwt()
                    //not getting set right
                    //console.log("JWT: ", global_data.auth.jwt)



                }

            }
            Component.onCompleted: {
                global_data.auth.jwtChanged.connect(function(newJwt) {
                    // Update UI elements or perform actions with the new JWT
                    console.log("New JWT:", newJwt);
                    // For example, updating the password field (or other relevant field)
                    passwordField.text = newJwt;
                })
            }
        }
    }


}
