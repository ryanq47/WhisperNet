.pragma library
//^^ does some stuff to make sure this is shared instead of being called again?


//Creates a new popup window. Top level item must be Window or WindowApplication
function openWindow(qmlFile) {
    var component = Qt.createComponent(qmlFile);
    component.statusChanged.connect(function() {
        if (component.status === QtQuick.Component.Ready) {
            var window = component.createObject(null); // Create without parent
            if (window) {
                window.visible = true;
            } else {
                console.error("Error creating window:", component.errorString());
            }
        } else if (component.status === QtQuick.Component.Error) {
            console.error("Error loading window:", component.errorString());
        }
    });
}
