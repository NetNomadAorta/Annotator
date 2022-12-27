from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets


def main():
    app = QApplication([])
    screen = app.primaryScreen()
    size = screen.size()
    window = QWidget()
    window.setGeometry(int(size.width()/3), int(size.height()*0.04),
                       max(int(size.width()/2),int(size.height()*1.5)), int(size.height()*.9)
                       )
    window.setWindowTitle("My Simple GUI")

    layout = QVBoxLayout()

    label = QLabel("Press the button below")
    textbox = QTextEdit()
    button = QPushButton("Press me")

    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    # label = QLabel(window)
    # label.setText("Press the button below!")
    # label.setFont(QFont("Arial", 16))
    # label.move(50, 100)

    window.show()
    app.exec_()


def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

if __name__ == '__main__':
    main()