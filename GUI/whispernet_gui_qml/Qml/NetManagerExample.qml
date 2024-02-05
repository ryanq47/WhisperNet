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
        onClicked: networkManager.postData("http://google.com","data_here")
    }

    // Connect the dataReceived signal to a handler
    Connections {
        target: networkManager
        function onDataReceived(data) {
            //keeping in old debugging statements for if data is being dumb
            //console.log("Type of data:")  // Print the actual data content
            //console.log(typeof data)  // Should print 'string'
            //console.log("data:")  // Print the actual data content
            //console.log(data)  // Print the actual data content
            receivedDataText.text = qsTr("Received: ") + data
            //receivedDataText.text = qsTr(data)
        }
    }
}
