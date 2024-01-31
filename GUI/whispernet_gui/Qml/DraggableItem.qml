// DraggableItem.qml
import QtQuick 2.0

Item {
    id: draggableItem
    width: 100
    height: 100
    // You can add other properties and visual elements here

    property point lastMousePos

    Rectangle {
        width: parent.width
        height: parent.height

        //text: "Wieeeee"
        Text {
            anchors.centerIn: parent
            text: "This is a popup!"
        }
    }

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
    }

    //resize handle
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
            ctx.fillStyle = "darkgray";
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
    }

}
