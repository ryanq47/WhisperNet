import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts 1.0

//https://het.as.utexas.edu/HET/Software/html/qdeclarativeelements.html

//import ./Utils.qml
//import "../js/utils.js" as Utils
//import "./Utils.qml" as Utils


ApplicationWindow {
    width: 1366
    height: 768
    visible: true
    title: "WhispherNet ~ Gui"


    ColumnLayout {
        id: columnLayout
        anchors.fill: parent

        Rectangle {
            id: base_rectangle
            anchors.fill: parent

            Text {
                anchors.centerIn: parent
                text: "Hi, open something!"
                color: "white"
            }

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
            //makes it fill width of column, due to column layout not having explicit width/height, whcih width was trying to pull from
            Layout.fillWidth: true
            background: Rectangle {
                color: "#444"//Style.primaryColor // Replace "desiredColor" with your preferred color
            }

            font.family: Style.fontFamily

            Row {
                anchors.fill: parent
                //fix em up
                ToolButton {
                    id: fileButton
                    text: qsTr("File")
                    onClicked: filePopup.open()
                    font.family: Style.fontFamily

                    background: Rectangle {
                        id: fileBackground
                        color: fileButton.hovered ? "#555" : "#444" // Change color on hover
                        radius: 2 // Optional: rounded corners

                        // Respond to button press
                        MouseArea {
                            id: fileMouseArea
                            anchors.fill: parent
                            onPressed: background.color = "#666"
                            onReleased: background.color = fileButton.hovered ? "#555" : "#444"
                        }
                    }

                    contentItem: Text {
                        text: fileButton.text
                        color: fileButton.enabled ? "white" : "#aaa" // Change text color based on enabled state
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
                ToolButton {
                    id: viewButton
                    text: qsTr("View")
                    font.family: Style.fontFamily
                    onClicked: viewPopup.open()
                    background: Rectangle {
                        id: viewBackground
                        color: viewButton.hovered ? "#555" : "#444" // Change color on hover
                        radius: 2 // Optional: rounded corners

                        // Respond to button press
                        MouseArea {
                            id: viewMouseArea
                            anchors.fill: parent
                            onPressed: background.color = "#666"
                            onReleased: background.color = viewButton.hovered ? "#555" : "#444"
                        }
                    }

                    contentItem: Text {
                        text: viewButton.text
                        color: viewButton.enabled ? "white" : "#aaa" // Change text color based on enabled state
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
                ToolButton {
                    id: devButton
                    font.family: Style.fontFamily
                    text: qsTr("Dev")
                    onClicked: devPopupMenu.open()
                    background: Rectangle {
                        id: devBackground
                        color: devButton.hovered ? "#555" : "#444" // Change color on hover
                        radius: 2 // Optional: rounded corners

                        // Respond to button press
                        MouseArea {
                            id: devMouseArea
                            anchors.fill: parent
                            onPressed: background.color = "#666"
                            onReleased: background.color = devButton.hovered ? "#555" : "#444"
                        }
                    }

                    contentItem: Text {
                        text: devButton.text
                        color: devButton.enabled ? "white" : "#aaa" // Change text color based on enabled state
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }

        }

    }



    //file tab in bar
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

    //dev tab in bar
    Popup {
        id: devPopupMenu
        x: devButton.x // Align the popup with the file button
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
                    id: devPopupButton1
                    text: qsTr("Net Manager Ex")
                    width: parent.width
                    onClicked: {
                        var component = Qt.createComponent("NetManagerExample.qml");
                        if (component.status === Component.Ready) {
                            var loginWindow = component.createObject(parent);
                            loginWindow.show();
                        } else if (component.status === Component.Error) {
                            console.error("Error loading component:", component.errorString());
                        }
                    }
                    // Optional: Set a fixed height or let it size to content
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

    //View tab in bar
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
                    onClicked: {
                        //popupSource = "DevWidget.qml"
                        //devPopup.open()
                        loadCustomComponent("DevWidget.qml")
                    }

                }
                ToolButton {
                    id: viewPopupButton2
                    text: qsTr("Item2")
                    width: parent.width
                    onClicked: {
                        //would love one that pops up on top of/out of the grid, worry about later
                        loadCustomComponent("DevWidget.qml")
                    }
                }

            }
        }
    }

    Popup {
        id: devPopup
        width: 220 // Slightly larger to account for padding or borders
        height: 220
        x: (parent.width - width) / 2 // Center the popup horizontally
        y: (parent.height - height) / 2 // Center the popup vertically

        Loader {
            id: loader
            source: popupSource
            anchors.fill: parent
        }
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



    //custom loader
    Component.onCompleted: {
        loadCustomComponent("DevWidget.qml");
        loadCustomComponent("DevWidget.qml");
    }

    function loadCustomComponent(source) {
        var component = Qt.createComponent(source);
        if (component.status === Component.Ready) {
            var object = component.createObject(columnLayout);
            if (object !== null) {
                // If the component uses QtQuick.Layouts, set Layout properties
                object.Layout.fillWidth = true;
            } else {
                console.error("Failed to create component");
            }
        } else if (component.status === Component.Error) {
            console.error("Error loading component:", component.errorString());
        }
    }


    //cool little custom item in qml.
    /*
    Test {
        id: button
        x: 100; y: 100
        text: "Start"
        onClicked: {
            DevWidget.open()
        }
    }*/

    /*
    DraggableItem{
        id: test
        x: 50
        y: 50
    }*/

}



