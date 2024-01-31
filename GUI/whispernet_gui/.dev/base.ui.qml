import QtQuick
import QtQuick.Window
import QtQuick.Controls 5.15

Item {
    width: 1366
    height: 768
    visible: true

    Rectangle {
        id: base_rectangle
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
        anchors.top: parent.top
        width: parent.width

        Row {
            anchors.fill: parent

            ToolButton {
                id: fileButton
                text: qsTr("File")
                //onClicked: filePopup.open()
            }

            ToolButton {
                id: viewButton
                text: qsTr("View")
                //onClicked: viewPopup.open()
            }
        }
    }

    Popup {
        id: filePopup
        x: fileButton.x // Align the popup with the file button
        y: toolBar.height
        width: 100
        height: 200

        Rectangle {
            width: parent.width
            height: parent.height
            color: "lightblue"

            Column {
                anchors.fill: parent
                spacing: 5 // Add some spacing between the buttons

                ToolButton {
                    id: filePopupButton1
                    text: qsTr("Item1")
                    width: parent.width
                    //onClicked: devPopup.open()

                    // Optional: Set a fixed height or let it size to content
                }
                ToolButton {
                    id: filePopupButton2
                    text: qsTr("Item2")
                    width: parent.width
                    //onClicked: devPopup.open()

                    // Optional: Set a fixed height or let it size to content
                }

                // The Text can either be part of the Column or outside it
                Text {
                    text: "File options"
                    anchors.horizontalCenter: parent.horizontalCenter
                    visible: false // Set to true if you want it to be visible
                }
            }
        }
    }

    Popup {
        id: viewPopup
        x: viewButton.x // Align the popup with the view button
        y: toolBar.height
        width: 100
        height: 200

        Rectangle {
            width: parent.width
            height: parent.height
            color: "lightgreen"

            Column {
                anchors.fill: parent

                ToolButton {
                    id: viewPopupButton1
                    text: qsTr("Item1")
                    width: parent.width
                    //onClicked:devPopup.open()
                }
                ToolButton {
                    id: viewPopupButton2
                    text: qsTr("Item2")
                    width: parent.width
                    //onClicked:devPopup.open()
                }
            }
        }
    }

    Popup {
        id: devPopup
        x: 500
        y: 500

        height: 30
        width: 160

        Text {
            color: "White"

            anchors.fill: parent
            id: devPopupText
            text: qsTr("Congrats your popup works")
        }
    }
}
