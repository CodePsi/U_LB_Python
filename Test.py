import sys

import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

app = QApplication(sys.argv)

w = QMainWindow()
w.resize(950, 450)
w.move(500, 300)
w.setWindowTitle('Simple')
menu = w.menuBar()
menu.setNativeMenuBar(False)
fileMenu = menu.addMenu('&amp;File')
@pyqtSlot()
def on_press():
    print('[', time.strftime('%X'), ']', " Button is press")
@pyqtSlot()
def on_click():
    print('[', time.strftime('%X'), ']', 'Button is clicked')
QMessageBox.about(w, 'Write', 'Would you like write? Send you main on: mongolzzz21@gmail.com')
result = QMessageBox.question(w, 'Start', 'Do you like Python?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if (result == QMessageBox.Yes):

    m_but = QAction('Exit', w)
    m_but.setShortcut('Ctrl+Q')
    m_but.setStatusTip('Exit app')
    m_but.triggered.connect(w.close)
    fileMenu.addAction(m_but)
    textbox = QLineEdit(w)
    textbox.move(10, 60)
    textbox.resize(100, 20)
    butt = QPushButton("", w);
    butt.setToolTip('Click to quite');
    butt.resize(butt.sizeHint())
    butt.move(10, 35)
    butt.clicked.connect(on_click);
    butt.pressed.connect(on_press);

    table = QTableWidget(w)
    tableItem = QTableWidgetItem()

    table.move(10, 120)
    table.setRowCount(3)
    table.setColumnCount(2)
    table.resize(216, 134)

    table.setItem(0, 0, QTableWidgetItem("Item 1"))
    table.setItem(0, 1, QTableWidgetItem("Item 2"))
    table.setItem(1, 0, QTableWidgetItem("Item 3"))
    table.setItem(1, 1, QTableWidgetItem("Item 4"))
    table.setItem(2, 0, QTableWidgetItem("Item 5"))
    table.setItem(2, 1, QTableWidgetItem("Item 6"))

    combbox = QComboBox(w)
    combbox.addItem("1")
    combbox.addItem("2")
    combbox.addItem("3")
    combbox.addItem("4")
    combbox.addItem("5")
    combbox.move(10, 90)

    w.show()
 #   m.show()
elif (result == QMessageBox.No):
    QMessageBox.critical(w, 'CRERROR', 'CRITICAL ERROR! finished with exit code -1073740791 (0xC0000409)')
    exit()
sys.exit(app.exec_())