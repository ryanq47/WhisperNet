import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    title: "QML Terminal with Python Backend"
    width: 640
    height: 480
    visible: true

    TextArea {
        id: terminalOutput
        anchors.fill: parent
        font.family: "monospace"
        wrapMode: TextEdit.WrapAnywhere
        readOnly: true
        text: "user@whatever:$ "
    }

    TextInput {
        id: commandInput
        anchors.left: terminalOutput.left
        anchors.bottom: terminalOutput.bottom
        width: terminalOutput.width
        color: "transparent"
        font: terminalOutput.font
        cursorVisible: true

        onAccepted: {
            terminalOutput.append(text);
            var result = backend.processCommand(text); // Call Python method
            terminalOutput.append("\n" + result + "\nuser@whatever:$ ");
            text = "";
        }
    }

    Component.onCompleted: {
        commandInput.forceActiveFocus();
    }
}
