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

    property int minimumWidth: 100
    property int minimumHeight: 100

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


    //for resizing, wrosk fine but a tad bit jank
    MouseArea {
        id: resizeArea
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        width: 20
        height: 20
        cursorShape: Qt.SizeFDiagCursor

        property point lastPos // Correctly define lastPos as a property of the MouseArea

        onPressed: {
            lastPos = mouse.position // Use mouse.position for Qt Quick 2.x
        }

        onPositionChanged: {
            if (pressed) {
                var dx = mouse.x - lastPos.x
                var dy = mouse.y - lastPos.y
                customComponent.width = Math.max(customComponent.width + dx, customComponent.minimumWidth)
                customComponent.height = Math.max(customComponent.height + dy, customComponent.minimumHeight)
                lastPos = mouse.position // Update lastPos with the new position
            }
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

