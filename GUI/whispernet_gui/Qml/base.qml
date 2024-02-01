import QtQuick
import QtQuick.Window
import QtQuick.Controls

//https://het.as.utexas.edu/HET/Software/html/qdeclarativeelements.html

//import ./Utils.qml
//import "../js/utils.js" as Utils
//import "./Utils.qml" as Utils


ApplicationWindow {
    width: 1366
    height: 768
    visible: true
    title: "WhispherNet ~ Gui"


    Rectangle {
        id: base_rectangle
        anchors.fill: parent


        //color: Style.primaryColor
        gradient: Gradient {
            GradientStop { position: 0.0; color: Style.gradientTop } //color: "#53A2E6" }
            GradientStop { position: 1.0; color: Style.gradientBottom } //color: "#133451" }
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
                onClicked: filePopup.open()
            }

            ToolButton {
                id: viewButton
                text: qsTr("View")
                onClicked: viewPopup.open()
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
                spacing: 5  // Add some spacing between the buttons

                ToolButton {
                    id: filePopupButton1
                    text: qsTr("item 1")
                    width: parent.width
                    onClicked: devPopup.open()

                    // Optional: Set a fixed height or let it size to content
                }
                ToolButton {
                    id: filePopupButton2
                    text: qsTr("Login To Server")
                    width: parent.width

                    onClicked: {
                        var component = Qt.createComponent("Login.qml");
                        if (component.status === Component.Ready) {
                            var loginWindow = component.createObject(parent);
                            loginWindow.show();
                        } else if (component.status === Component.Error) {
                            console.error("Error loading component:", component.errorString());
                        }
                    }
                }

                // The Text can either be part of the Column or outside it
                Text {
                    text: "File options"
                    anchors.horizontalCenter: parent.horizontalCenter
                    visible: false  // Set to true if you want it to be visible
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
                anchors.fill:parent

                ToolButton {
                    id: viewPopupButton1
                    text: qsTr("Item1")
                    width: parent.width
                    onClicked:devPopup.open()

                }
                ToolButton {
                    id: viewPopupButton2
                    text: qsTr("Item2")
                    width: parent.width
                    onClicked:devPopup.open()

                }

            }
        }
    }

    Popup {
        id: devPopup
        x:500
        y:500

        height: 30
        width: 160

        Text {
            color: "Black"

            anchors.fill: parent
            id: devPopupText
            text: qsTr("Congrats your popup works")
        }

    }


    // Loader to dynamically load the popup content
    Loader {
        id: popupLoader
        source: ""  // Initially empty
    }

    //basically a func to setup the popup
    Popup {
        id: myPopup
        width: 300
        height: 200
        contentItem: popupLoader.item  // Set the loaded item as the content

        // Positioning and other properties as needed
    }


    //can't get these to work in a utils file, so its here for now
    QtObject {
        id: utils
        function createWindow(qmlFilePath) {
            var component = Qt.createComponent(qmlFilePath);
            if (component.status === Component.Ready) {
                var window = component.createObject();
                if (window === null) {
                    console.error("Error creating window");
                } else {
                    window.visible = true;
                }
            } else if (component.status === Component.Error) {
                console.error("Error loading component:", component.errorString());
            }
        }
    }


    //cool little custom item in qml.
    Test {
        id: button
        x: 100; y: 100
        text: "Start"
        onClicked: {
            devPopup.open()
        }
    }

    /*
    DraggableItem{
        id: test
        x: 50
        y: 50
    }*/

}



