# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1229, 653)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnReplace = QPushButton(self.centralwidget)
        self.btnReplace.setObjectName(u"btnReplace")
        self.btnReplace.setGeometry(QRect(480, 240, 93, 39))
        self.plainText = QPlainTextEdit(self.centralwidget)
        self.plainText.setObjectName(u"plainText")
        self.plainText.setGeometry(QRect(20, 110, 421, 391))
        self.plainCode = QPlainTextEdit(self.centralwidget)
        self.plainCode.setObjectName(u"plainCode")
        self.plainCode.setGeometry(QRect(620, 40, 581, 561))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1229, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Program", None))
        self.btnReplace.setText(QCoreApplication.translate("MainWindow", u"Replace!", None))
    # retranslateUi

