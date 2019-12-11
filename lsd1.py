#!/usr/bin/env python3
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout,
                             QGroupBox,QMenu, QPushButton,
                             QRadioButton, QVBoxLayout,
                             QWidget, QSlider,QLabel)

class sliderdemo(QWidget):
    def __init__(self, vSl=90, parent=None):
        super(sliderdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(20)
        self.sl.setMaximum(99)
        self.sl.setValue(vSl)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(10)

        layout.addWidget(self.sl)
        self.sl.valueChanged[int].connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("Lcd 1-1")
        a = "xrandr --output LVDS-1-1 --brightness ."
        b = vSl
        os.system(a + str(b))

    def valuechange(self, value):
        self.__init__(value)

def main():
   app = QApplication(sys.argv)
   ex = sliderdemo(90)
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()