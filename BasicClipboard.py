import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QPlainTextEdit, QGridLayout, QApplication)

class ClipWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.clipEdit = QPlainTextEdit()
        #create button along with action
        ClearButton = QPushButton(parent=self, text="Clear Text")
        ClearButton.clicked.connect(self.ClearText)
        #create grid
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.clipEdit, 0,1,5,1)
        grid.addWidget(ClearButton, 0,2)
        self.setLayout(grid)
        self.setFixedSize(550,350)

        QApplication.clipboard().dataChanged.connect(self.onClipboardChanged)

    def ClearText(self):
        #function to clear text
        self.clipEdit.clear()
    
    def onClipboardChanged(self):
        #action on copying and inserting text
        text = QApplication.clipboard().text()
        self.clipEdit.insertPlainText(text + '\n')

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainWin = ClipWindow()
    mainWin.setWindowTitle("Basic Clipboard")
    mainWin.show()
    sys.exit(app.exec())