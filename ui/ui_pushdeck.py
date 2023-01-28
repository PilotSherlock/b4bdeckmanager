# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pushdeck.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog_push_deck(object):
    def setupUi(self, Dialog_push_deck):
        if not Dialog_push_deck.objectName():
            Dialog_push_deck.setObjectName(u"Dialog_push_deck")
        Dialog_push_deck.setEnabled(True)
        Dialog_push_deck.resize(277, 504)
        icon = QIcon()
        icon.addFile(u"../icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_push_deck.setWindowIcon(icon)
        self.textEdit_author = QTextEdit(Dialog_push_deck)
        self.textEdit_author.setObjectName(u"textEdit_author")
        self.textEdit_author.setGeometry(QRect(0, 30, 271, 41))
        font = QFont()
        font.setPointSize(16)
        self.textEdit_author.setFont(font)
        self.textEdit_game_version = QTextEdit(Dialog_push_deck)
        self.textEdit_game_version.setObjectName(u"textEdit_game_version")
        self.textEdit_game_version.setGeometry(QRect(0, 100, 271, 41))
        self.textEdit_game_version.setFont(font)
        self.textEdit_deck_info = QTextEdit(Dialog_push_deck)
        self.textEdit_deck_info.setObjectName(u"textEdit_deck_info")
        self.textEdit_deck_info.setGeometry(QRect(0, 220, 271, 221))
        self.comboBox_difficulty = QComboBox(Dialog_push_deck)
        self.comboBox_difficulty.addItem("")
        self.comboBox_difficulty.addItem("")
        self.comboBox_difficulty.addItem("")
        self.comboBox_difficulty.addItem("")
        self.comboBox_difficulty.addItem("")
        self.comboBox_difficulty.setObjectName(u"comboBox_difficulty")
        self.comboBox_difficulty.setGeometry(QRect(0, 170, 271, 22))
        self.label_author = QLabel(Dialog_push_deck)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setGeometry(QRect(50, 0, 161, 31))
        self.label_author.setFont(font)
        self.label_game_version = QLabel(Dialog_push_deck)
        self.label_game_version.setObjectName(u"label_game_version")
        self.label_game_version.setGeometry(QRect(50, 70, 161, 31))
        self.label_game_version.setFont(font)
        self.label_difficulty = QLabel(Dialog_push_deck)
        self.label_difficulty.setObjectName(u"label_difficulty")
        self.label_difficulty.setGeometry(QRect(50, 140, 161, 31))
        self.label_difficulty.setFont(font)
        self.label_deck_info = QLabel(Dialog_push_deck)
        self.label_deck_info.setObjectName(u"label_deck_info")
        self.label_deck_info.setGeometry(QRect(50, 190, 161, 31))
        self.label_deck_info.setFont(font)
        self.pushButton_importInGame_recommend = QPushButton(Dialog_push_deck)
        self.pushButton_importInGame_recommend.setObjectName(u"pushButton_importInGame_recommend")
        self.pushButton_importInGame_recommend.setGeometry(QRect(50, 440, 181, 61))

        self.retranslateUi(Dialog_push_deck)

        QMetaObject.connectSlotsByName(Dialog_push_deck)
    # setupUi

    def retranslateUi(self, Dialog_push_deck):
        Dialog_push_deck.setWindowTitle(QCoreApplication.translate("Dialog_push_deck", u"\u5206\u4eab\u5361\u7ec4", None))
        self.textEdit_author.setHtml(QCoreApplication.translate("Dialog_push_deck", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_game_version.setHtml(QCoreApplication.translate("Dialog_push_deck", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.comboBox_difficulty.setItemText(0, QCoreApplication.translate("Dialog_push_deck", u"\u7edd\u671b", None))
        self.comboBox_difficulty.setItemText(1, QCoreApplication.translate("Dialog_push_deck", u"\u5669\u68a6", None))
        self.comboBox_difficulty.setItemText(2, QCoreApplication.translate("Dialog_push_deck", u"\u8001\u5175", None))
        self.comboBox_difficulty.setItemText(3, QCoreApplication.translate("Dialog_push_deck", u"\u65b0\u5175", None))
        self.comboBox_difficulty.setItemText(4, QCoreApplication.translate("Dialog_push_deck", u"\u5a31\u4e50", None))

        self.label_author.setText(QCoreApplication.translate("Dialog_push_deck", u"<html><head/><body><p align=\"center\">\u4f5c\u8005</p></body></html>", None))
        self.label_game_version.setText(QCoreApplication.translate("Dialog_push_deck", u"<html><head/><body><p align=\"center\">\u9002\u7528\u7248\u672c</p></body></html>", None))
        self.label_difficulty.setText(QCoreApplication.translate("Dialog_push_deck", u"<html><head/><body><p align=\"center\">\u96be\u5ea6</p></body></html>", None))
        self.label_deck_info.setText(QCoreApplication.translate("Dialog_push_deck", u"<html><head/><body><p align=\"center\">\u5361\u7ec4\u4fe1\u606f</p></body></html>", None))
        self.pushButton_importInGame_recommend.setText(QCoreApplication.translate("Dialog_push_deck", u"\u63d0\u4ea4", None))
    # retranslateUi

