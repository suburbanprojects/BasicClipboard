import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
QLineEdit, QPushButton, QListWidget, QHBoxLayout)

class Clipboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clipboard')
        self.setGeometry(100, 100, 550,525)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
    
        self.layout = QVBoxLayout(self.central_widget)
        #text field input
        self.clip_insert = QLineEdit(self)
        self.layout.addWidget(self.clip_insert)
        #add buttons
        button_layout = QHBoxLayout()

        self.add_button = QPushButton('Add Entry', self)
        self.add_button.clicked.connect(self.add_entry)
        button_layout.addWidget(self.add_button)

        self.delete_button = QPushButton('Delete Entry', self)
        self.delete_button.clicked.connect(self.delete_entry)
        button_layout.addWidget(self.delete_button)

        self.clear_button = QPushButton('Clear Field', self)
        self.clear_button.clicked.connect(self.clear_field)
        button_layout.addWidget(self.clear_button)
        
        self.layout.addLayout(button_layout)
        #result list
        self.clip_list = QListWidget(self)
        #word wrap the entries in the list
        self.clip_list.setWordWrap(True) 
        self.layout.addWidget(self.clip_list)

        QApplication.clipboard().dataChanged.connect(self.onClipboardChanged)

    def onClipboardChanged(self):
        #action on copying and inserting text
        text = QApplication.clipboard().text()
        #use setText for QLineEdit
        self.clip_insert.setText(text + '\n')

    def add_entry(self):
        task = self.clip_insert.text()
        if task:
            self.clip_list.addItem(task)
            self.clip_insert.clear()
    
    def delete_entry(self):
        selected_items = self.clip_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.clip_list.takeItem(self.clip_list.row(item))

    def clear_field(self):
        #function to clear text
        self.clip_insert.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main_window = Clipboard()
    main_window.show()
    sys.exit(app.exec())
