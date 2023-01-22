# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'decksmanager.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 616)
        icon = QIcon()
        icon.addFile(u"ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.info = QAction(MainWindow)
        self.info.setObjectName(u"info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.cards = QWidget()
        self.cards.setObjectName(u"cards")
        self.listWidget_cardSet = QListWidget(self.cards)
        self.listWidget_cardSet.setObjectName(u"listWidget_cardSet")
        self.listWidget_cardSet.setGeometry(QRect(10, 30, 181, 481))
        font = QFont()
        font.setPointSize(16)
        self.listWidget_cardSet.setFont(font)
        self.pushButton_importInGame = QPushButton(self.cards)
        self.pushButton_importInGame.setObjectName(u"pushButton_importInGame")
        self.pushButton_importInGame.setGeometry(QRect(510, 30, 181, 61))
        self.pushButton_delectSet = QPushButton(self.cards)
        self.pushButton_delectSet.setObjectName(u"pushButton_delectSet")
        self.pushButton_delectSet.setGeometry(QRect(510, 170, 181, 61))
        self.pushButton_shareCode = QPushButton(self.cards)
        self.pushButton_shareCode.setObjectName(u"pushButton_shareCode")
        self.pushButton_shareCode.setGeometry(QRect(510, 450, 181, 61))
        self.pushButton_renameSet = QPushButton(self.cards)
        self.pushButton_renameSet.setObjectName(u"pushButton_renameSet")
        self.pushButton_renameSet.setGeometry(QRect(510, 240, 181, 61))
        self.pushButton_insertCard = QPushButton(self.cards)
        self.pushButton_insertCard.setObjectName(u"pushButton_insertCard")
        self.pushButton_insertCard.setGeometry(QRect(510, 400, 91, 41))
        self.pushButton_delectCard = QPushButton(self.cards)
        self.pushButton_delectCard.setObjectName(u"pushButton_delectCard")
        self.pushButton_delectCard.setGeometry(QRect(600, 400, 91, 41))
        self.listWidget_cards = QListWidget(self.cards)
        self.listWidget_cards.setObjectName(u"listWidget_cards")
        self.listWidget_cards.setGeometry(QRect(200, 30, 256, 481))
        self.listWidget_cards.setFont(font)
        self.pushButton_insertSet = QPushButton(self.cards)
        self.pushButton_insertSet.setObjectName(u"pushButton_insertSet")
        self.pushButton_insertSet.setGeometry(QRect(510, 100, 181, 61))
        self.tabWidget.addTab(self.cards, "")
        self.importCards = QWidget()
        self.importCards.setObjectName(u"importCards")
        self.widget = QWidget(self.importCards)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 697, 252))
        self.textEdit_shareCode = QTextEdit(self.widget)
        self.textEdit_shareCode.setObjectName(u"textEdit_shareCode")
        self.textEdit_shareCode.setGeometry(QRect(10, 20, 681, 111))
        self.pushButton_codeImport = QPushButton(self.widget)
        self.pushButton_codeImport.setObjectName(u"pushButton_codeImport")
        self.pushButton_codeImport.setGeometry(QRect(190, 140, 301, 81))
        font1 = QFont()
        font1.setPointSize(28)
        self.pushButton_codeImport.setFont(font1)
        self.widget_2 = QWidget(self.importCards)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 270, 697, 252))
        self.pushButton_ocrImport = QPushButton(self.widget_2)
        self.pushButton_ocrImport.setObjectName(u"pushButton_ocrImport")
        self.pushButton_ocrImport.setGeometry(QRect(190, 70, 301, 81))
        self.pushButton_ocrImport.setFont(font1)
        self.tabWidget.addTab(self.importCards, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.info)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"b4bdeck manager", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u5165\u8bbe\u7f6e", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.pushButton_importInGame.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6e38\u620f", None))
        self.pushButton_delectSet.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5361\u7ec4", None))
        self.pushButton_shareCode.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5206\u4eab\u5b57\u7b26\u4e32", None))
        self.pushButton_renameSet.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.pushButton_insertCard.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5361\u724c", None))
        self.pushButton_delectCard.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5361\u724c", None))
        self.pushButton_insertSet.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5361\u7ec4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cards), QCoreApplication.translate("MainWindow", u"\u5361\u724c\u914d\u7f6e", None))
        self.pushButton_codeImport.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u7b26\u4e32\u5bfc\u5165", None))
        self.pushButton_ocrImport.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.importCards), QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5361\u724c\u914d\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

