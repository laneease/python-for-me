# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created: Thu Dec 30 04:14:12 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(400, 300)
        self.button_open = QtGui.QPushButton(notepad)
        self.button_open.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.editor_window = QtGui.QTextEdit(notepad)
        self.editor_window.setGeometry(QtCore.QRect(10, 40, 371, 241))
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.button_close = QtGui.QPushButton(notepad)
        self.button_close.setGeometry(QtCore.QRect(284, 10, 101, 23))
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.button_save = QtGui.QPushButton(notepad)
        self.button_save.setEnabled(False)
        self.button_save.setGeometry(QtCore.QRect(150, 10, 91, 23))
        self.button_save.setObjectName(_fromUtf8("button_save"))

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL(_fromUtf8("clicked()")), notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(QtGui.QApplication.translate("notepad", "notepad", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("notepad", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("notepad", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("notepad", "Save", None, QtGui.QApplication.UnicodeUTF8))

