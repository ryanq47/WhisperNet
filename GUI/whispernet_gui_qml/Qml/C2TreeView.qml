// CustomDevWidget.qml
import QtQuick
import QtQuick.Controls
//DO NOT call Item. has to be DevWidget
Item {
    //widgetName: "CustomDevWidget"
    width: 500
    height: 500

    // Override properties or add new functionality
    Component.onCompleted: {
        console.log("widgetName" + " is ready.");
    }

    ListModel {
        id: model
        ListElement {
            name: "Bill Smith"
            number: "555 3264"
        }
        ListElement {
            name: "John Brown"
            number: "555 8426"
        }
        ListElement {
            name: "Sam Wise"
            number: "555 0473"
        }
    }

    //standin model
    Component {
        id: contactDelegate
        Item {
            width: 180; height: 40
            Column {
                Text { text: '<b>Name:</b> ' + name }
                Text { text: '<b>Number:</b> ' + number }
            }
        }
    }

    ListView {
        anchors.fill: parent
        model: model
        delegate: contactDelegate
        highlight: Rectangle { color: "lightsteelblue"; radius: 5 }
        focus: true
    }

}


