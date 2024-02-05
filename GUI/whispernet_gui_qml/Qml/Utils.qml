import QtQuick 2.0

QtObject {
    function createWindow(qmlFilePath) {
        var component = Qt.createComponent(qmlFilePath);
        if (component.status === Component.Ready) {
            var window = component.createObject(null);
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
