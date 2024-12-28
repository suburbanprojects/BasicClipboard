import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
QLineEdit, QPushButton, QListWidget, QHBoxLayout, QLabel)

class Clipboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Basic Clipboard')
        self.setGeometry(100, 100, 550, 525)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        #text field input
        self.layout = QVBoxLayout(self.central_widget)
        self.clip_insert_entry = QLineEdit(self)
        #add button layout
        self.layout.addWidget(self.clip_insert_entry)
        button_layout = QHBoxLayout()
        #add the buttons
        self.add_button = QPushButton('Add Entry', self)
        self.add_button.clicked.connect(self.add_entry)
        button_layout.addWidget(self.add_button)
        #delete button
        self.delete_button = QPushButton('Delete Entry',self)
        self.delete_button.clicked.connect(self.delete_entry)
        button_layout.addWidget(self.delete_button)
        #clear buttons
        self.clear_button = QPushButton('Clear Field',self)
        self.clear_button.clicked.connect(self.clear_field)
        button_layout.addWidget(self.clear_button)
        #add button layout
        self.layout.addLayout(button_layout)
        #put entries here
        self.clip_list_entry = QListWidget(self)
        self.clip_list_entry.setWordWrap(True)
        self.layout.addWidget(self.clip_list_entry)
        
        #add label here
        self.copied_task_label = QLabel(self)
        self.layout.addWidget(self.copied_task_label)
        
        #Second button layout at the bottom
        button_layout_2 = QHBoxLayout()
        #button to copy from the list
        self.copy_entry_button = QPushButton('Copy Entry',self)
        self.copy_entry_button.clicked.connect(self.copy_entry)
        button_layout_2.addWidget(self.copy_entry_button)
        #button to clear all
        self.clear_all_button = QPushButton('Clear All',self)
        self.clear_all_button.clicked.connect(self.clear_all)
        button_layout_2.addWidget(self.clear_all_button)
        self.layout.addLayout(button_layout_2)
        #action for clipboard
        QApplication.clipboard().dataChanged.connect(self.onClipboardChanged)
    
    #put clipboard function here
    def onClipboardChanged(self):
        #action on copying and inserting text
        text = QApplication.clipboard().text()
        #use setText for QLineEdit
        self.clip_insert_entry.setText(text + '\n')
    #put functions for the upper buttons here
    def add_entry(self):
        task = self.clip_insert_entry.text()
        if task:
            self.clip_list_entry.addItem(task)
            self.clip_insert_entry.clear()

    def delete_entry(self):
        selected_items = self.clip_list_entry.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.clip_list_entry.takeItem(self.clip_list_entry.row(item))

    def clear_field(self):
        self.clip_insert_entry.clear()

    #put functions for the lower buttons here
    def copy_entry(self):
        #copy the entry from the clipboard
        selected_entry = self.clip_list_entry.selectedItems()
        if not selected_entry:
            return
        #copies the list to a clipboard
        copied_entry = selected_entry[0].text()
        clipboard = QApplication.clipboard()
        clipboard.setText(copied_entry)
        self.copied_task_label.setText(f'Copied Entry: {copied_entry}')

    def clear_all(self):
        self.clip_list_entry.clear()
        self.copied_task_label.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main_window = Clipboard()
    main_window.show()
    sys.exit(app.exec())
