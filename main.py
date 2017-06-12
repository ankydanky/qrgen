# coding: utf-8

import os
import sys

import pyqrcode

import PySide.QtCore as core
import PySide.QtGui as gui


class QRGenerator(object):
    
    def __init__(self):
        self.setWindow()
        self.setLabels()
        self.setButtons()
        self.setInputs()
        self.setLayout()
    
    def setWindow(self):
        self.mainwindow = gui.QMainWindow()
        self.mainwindow.setWindowTitle("Simple QR Generator 1.0")
        self.mainwidget = gui.QWidget()
        self.mainwindow.setCentralWidget(self.mainwidget)
    
    def setLabels(self):
        self.lblscale = gui.QLabel("Size:")
        self.lblformat = gui.QLabel("Format:")
        
    def setButtons(self):
        self.btngen = gui.QPushButton("Generete QR")
        self.btngen.clicked.connect(self.generateCode)
    
    def setInputs(self):
        self.textinput = gui.QTextEdit()
        self.scaleinput = gui.QSpinBox()
        self.scaleinput.setValue(4)
        self.scaleinput.setMinimum(1)
        self.scaleinput.setMaximum(20)
        self.radioeps = gui.QRadioButton("EPS")
        self.radioeps.setChecked(True)
        self.radiopng = gui.QRadioButton("PNG")
    
    def setLayout(self):
        self.mainlayout = gui.QVBoxLayout()
        self.btnlayout = gui.QHBoxLayout()
        self.btnlayout.addWidget(self.lblscale)
        self.btnlayout.addWidget(self.scaleinput)
        self.btnlayout.addWidget(self.lblformat)
        self.btnlayout.addWidget(self.radioeps)
        self.btnlayout.addWidget(self.radiopng)
        self.btnlayout.addStretch(True)
        self.btnlayout.addWidget(self.btngen)
        self.mainlayout.addWidget(self.textinput)
        self.mainlayout.addLayout(self.btnlayout)
        self.mainwidget.setLayout(self.mainlayout)
        
    def show(self):
        self.mainwindow.show()
        self.mainwindow.raise_()
    
    def generateCode(self):
        content = unicode(self.textinput.toPlainText())
        qr = pyqrcode.create(content)
        filedlg = gui.QFileDialog()
        filedlg.setAcceptMode(gui.QFileDialog.AcceptSave)
        filedlg.setConfirmOverwrite(True)
        if self.radioeps.isChecked():
            filedlg.setDefaultSuffix("eps")
        elif self.radiopng.isChecked():
            filedlg.setDefaultSuffix("png")
        filedlg.exec_()
        self.mainwindow.activateWindow()
        filename = filedlg.selectedFiles()[0]
        scalevalue = self.scaleinput.value()
        bgcolor = "#fff"
        if self.radioeps.isChecked():
            qr.eps(filename, scale=scalevalue, background=bgcolor)
        elif self.radiopng.isChecked():
            qr.png(filename, scale=scalevalue, background=bgcolor)
