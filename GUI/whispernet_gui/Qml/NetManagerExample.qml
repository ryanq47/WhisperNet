import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Network Manager Example"

    // A text field to display the received data
    Text {
        id: receivedDataText
        text: qsTr("Waiting for data...")
        anchors.centerIn: parent
        anchors.verticalCenterOffset: 50 // Position below the button
    }

    Button {
        text: qsTr("Post Data")
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: networkManager.postData("http://google.com")
    }

    // Connect the dataReceived signal to a handler
    Connections {
        target: networkManager
        onDataReceived: {
            receivedDataText.text = qsTr("Received: ") + data
        }
    }
}
