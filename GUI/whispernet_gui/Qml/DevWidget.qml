import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

Rectangle {
    id: customComponent
    color: Style.primaryColor
    // Optionally use Layout.fillWidth: true and Layout.fillHeight: true if inside a Layout.
    Layout.fillWidth: true
    Layout.fillHeight: true

    property var dragStart: null  // To store the initial click position
    property string widgetName: "widgetName"  // To store the initial click position


    Text {
        anchors.centerIn: parent
        text: "Custom Content"
    }


    // Title Bar
    Rectangle {
        id: titleBar
        width: parent.width
        height: 20
        color: "grey"//Style.primaryColor //"grey"

        MouseArea {
            id: dragArea
            anchors.fill: parent
            property point clickPos

            onPressed: { clickPos = Qt.point(mouse.x, mouse.y) }
            onPositionChanged: {
                if (dragArea.pressed) {
                    customComponent.x += mouse.x - dragArea.clickPos.x
                    customComponent.y += mouse.y - dragArea.clickPos.y
                }
            }
        }

        Label {
            text: widgetName
            anchors.centerIn: parent
            color: "white"
        }
    }

    //close button, KEEP AT BOTTOM
    Button {
        id: closeButton
        text: "X"
        anchors.top: parent.top
        anchors.right: parent.right
        width: 30
        height: 20

        background: Rectangle {
            //color: closeButton.hovered ? Style.closeButton : Style.closeButton  // Changes color on hover

            color: Style.closeButton  // Set to your desired color
            //radius: 2  // Optional: adds rounded corners
        }

        onClicked: {
            customComponent.visible = false; // Hide the Rectangle
            // If you need to completely destroy the component, use customComponent.destroy()
        }
    }

}


//next, impleemnt style form stylepy
