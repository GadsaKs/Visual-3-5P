from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200,0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry() #cek ukuran window app
        cwc = QDesktopWidget().availableGeometry().center()
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()