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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QTextEdit, QWidget)

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
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.actioncheck = QAction(MainWindow)
        self.actioncheck.setObjectName(u"actioncheck")
        self.actioncheckDeck = QAction(MainWindow)
        self.actioncheckDeck.setObjectName(u"actioncheckDeck")
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
        self.recommend = QWidget()
        self.recommend.setObjectName(u"recommend")
        self.listWidget_cardSet_recommend = QListWidget(self.recommend)
        self.listWidget_cardSet_recommend.setObjectName(u"listWidget_cardSet_recommend")
        self.listWidget_cardSet_recommend.setGeometry(QRect(10, 10, 181, 481))
        self.listWidget_cardSet_recommend.setFont(font)
        self.listWidget_cards_recommend = QListWidget(self.recommend)
        self.listWidget_cards_recommend.setObjectName(u"listWidget_cards_recommend")
        self.listWidget_cards_recommend.setGeometry(QRect(200, 10, 256, 481))
        self.listWidget_cards_recommend.setFont(font)
        self.pushButton_importInGame_recommend = QPushButton(self.recommend)
        self.pushButton_importInGame_recommend.setObjectName(u"pushButton_importInGame_recommend")
        self.pushButton_importInGame_recommend.setGeometry(QRect(500, 430, 181, 61))
        self.textBrowser_author = QTextBrowser(self.recommend)
        self.textBrowser_author.setObjectName(u"textBrowser_author")
        self.textBrowser_author.setGeometry(QRect(470, 50, 241, 31))
        self.label_author = QLabel(self.recommend)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setGeometry(QRect(560, 10, 53, 31))
        self.textBrowser_game_version = QTextBrowser(self.recommend)
        self.textBrowser_game_version.setObjectName(u"textBrowser_game_version")
        self.textBrowser_game_version.setGeometry(QRect(470, 160, 241, 31))
        self.textBrowser_deck_info = QTextBrowser(self.recommend)
        self.textBrowser_deck_info.setObjectName(u"textBrowser_deck_info")
        self.textBrowser_deck_info.setGeometry(QRect(470, 240, 241, 161))
        self.label_game_version = QLabel(self.recommend)
        self.label_game_version.setObjectName(u"label_game_version")
        self.label_game_version.setGeometry(QRect(510, 120, 161, 31))
        self.label_deck_info = QLabel(self.recommend)
        self.label_deck_info.setObjectName(u"label_deck_info")
        self.label_deck_info.setGeometry(QRect(510, 200, 161, 31))
        self.tabWidget.addTab(self.recommend, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionGithub)
        self.menu.addAction(self.action_info)
        self.menu_2.addAction(self.actioncheck)
        self.menu_2.addAction(self.actioncheckDeck)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"b4bdeck manager", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u5165\u8bbe\u7f6e", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.actioncheck.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.actioncheckDeck.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u724c\u7ec4", None))
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
        self.pushButton_importInGame_recommend.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6e38\u620f", None))
        self.label_author.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u4f5c\u8005</span></p></body></html>", None))
        self.textBrowser_deck_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_game_version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u9002\u7528\u6e38\u620f\u7248\u672c</span></p><p align=\"center\"><span style=\" font-size:16pt;\"><br/></span></p></body></html>", None))
        self.label_deck_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u5361\u7ec4\u8bf4\u660e</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recommend), QCoreApplication.translate("MainWindow", u"\u63a8\u8350\u5361\u7ec4", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
    # retranslateUi

