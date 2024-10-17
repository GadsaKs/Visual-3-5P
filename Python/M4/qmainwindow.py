from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
# label = QLabel("Label", window)
label = QLabel("Label1")
label.setText("Label1")
label.move(200, 0)

# button = QPushButton("MyButton", window)
button = QPushButton(window)
button.setText("Button1")

window.show()
app.exec_()