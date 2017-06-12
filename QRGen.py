# coding: utf-8

import os
import sys

import PySide.QtCore as core
import PySide.QtGui as gui

import main

if __name__ == '__main__':
    app = gui.QApplication(sys.argv)
    qrgenerator = main.QRGenerator()
    qrgenerator.show()
    sys.exit(app.exec_())
