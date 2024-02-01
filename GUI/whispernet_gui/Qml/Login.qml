// DraggableItem.qml
import QtQuick
import QtQuick.Controls 2.0
//A playaround draggable item. Maybe use this as a plugin template

ApplicationWindow {
    id: draggableItem
    //crazy that this works, but its cool
    width: backgroundRect.width
    height: backgroundRect.height
    visible: true
    // You can add other properties and visual elements here

    property point lastMousePos

    Rectangle {
        id: backgroundRect
        color: "white"

        // Let the Rectangle size itself based on the Column
        width: column.width + 20  // Add margin
        height: column.height + 20 // Add margin

        Column {
            id: column
            spacing: 5
            anchors.centerIn: parent // Center the column in the Rectangle

            Text {
                id: headerField
                width: parent.width
                //anchors.centerIn: parent
                height: 30
                text: "<b>Login Form</b>"
            }

            TextField {
                id: serverField
                width: parent.width
                height: 30
                placeholderText: qsTr("Server")
            }

            TextField {
                id: usernameField
                width: 200 // Set a fixed width or use percentage of parent
                height: 30
                placeholderText: qsTr("Username")
            }

            TextField {
                id: passwordField
                width: parent.width
                height: 30
                placeholderText: qsTr("Password")
            }


            Button {
                id: loginButton

                width: parent.width
                height: 30
                text: qsTr("Log In")
            }
        }
    }


    /*
    MouseArea {
        anchors.fill: parent
        drag.target: parent

        onPressed: {
            lastMousePos = Qt.point(mouseX, mouseY)
        }

        onPositionChanged: {
            var dx = mouseX - lastMousePos.x
            var dy = mouseY - lastMousePos.y
            draggableItem.x += dx
            draggableItem.y += dy
        }

        onReleased: {
            // Snap logic goes here
            // Adjust draggableItem.x and draggableItem.y based on your snapping criteria
        }
    }*/

    //resize handle
    /*
    Canvas {
        id: resizeHandle
        width: 20
        height: 20
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        //cool way to turn into triangle
        onPaint: {
            var ctx = getContext("2d");
            ctx.beginPath();
            ctx.moveTo(0, height);  // Bottom left
            ctx.lineTo(width, height);  // Bottom right
            ctx.lineTo(width, 0);  // Top right
            ctx.closePath();
            ctx.fillStyle = "black";
            ctx.fill();
        }

        MouseArea {
            id: resizeArea
            anchors.fill: parent
            property point clickPos

            onPressed: {
                clickPos = Qt.point(mouseX, mouseY)
            }

            onPositionChanged: {
                if (resizeArea.pressed) {
                    draggableItem.width = Math.max(100, draggableItem.width + (mouseX - clickPos.x))
                    draggableItem.height = Math.max(100, draggableItem.height + (mouseY - clickPos.y))
                }
            }
        }
    }*/


    /*
    Button {
        id: closePopupButton
        //what to anchor //where to anchor to/in ref from
        anchors.top: draggableItem.top
        anchors.right: draggableItem.right
        text: "Close"
        //onClicked: { //destroys object
        //    draggableItem.destroy()
        //}
        onClicked: { //hides object
            draggableItem.visible = false
        }
    }*/
}
