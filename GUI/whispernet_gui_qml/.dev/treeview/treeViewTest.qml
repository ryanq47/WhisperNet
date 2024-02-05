import QtQuick 
import QtQuick.Controls 
import QtQuick.Window 

Window {
    visible: true
    width: 640
    height: 480
    title: "TreeView Delegate Example"

    ListModel {
        id: treeModel
        ListElement {
            name: "Folder 1"
            type: "folder"
            // Sub-items of the folder
            children: ListModel {
                ListElement { name: "File 1.1"; type: "file" }
                ListElement { name: "File 1.2"; type: "file" }
            }
        }
        ListElement {
            name: "Folder 2"
            type: "folder"
            children: ListModel {
                ListElement { name: "File 2.1"; type: "file" }
                ListElement { name: "Folder 2.1"; type: "folder"
                    children: ListModel {
                        ListElement { name: "File 2.1.1"; type: "file" }
                    }
                }
            }
        }
    }

    TreeView {
        anchors.fill: parent
        model: treeModel

        TreeViewColumn {
            title: "Name"
            role: "name"
            width: 300
        }

        rowDelegate: ItemDelegate {
            height: 20
            contentItem: Row {
                spacing: 10
                Image {
                    source: model.type === "folder" ? "folder-icon.png" : "file-icon.png"
                    width: 16
                    height: 16
                }
                Text {
                    text: model.name
                }
            }
        }
    }
}
