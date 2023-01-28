#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by GJ on 2017/11/21
from PySide6.QtGui import QPainter,QGuiApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, Signal
import logging
import os
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class ScreenShotsWin(QMainWindow):
    # 定义一个信号
    oksignal = Signal()
    done = Signal()
    def __init__(self):
        super(ScreenShotsWin, self).__init__()
        self.initUI()
        self.start = (0, 0)  # 开始坐标点
        self.end = (0, 0)  # 结束坐标点
        self.cwd = os.getcwd()  # 获取当前程序文件位置
    def initUI(self):
        # self.showFullScreen()
        self.setWindowOpacity(0.4)
        # self.btn_ok = QPushButton('保存', self)

        self.oksignal.connect(lambda: self.screenshots(self.start,self.end))

    def screenshots(self,start,end):
        '''
        截图功能
        :param start:截图开始点
        :param end:截图结束点
        :return:
        '''
        # logger.debug('开始截图,%s, %s', start, end)

        x = min(start[0], end[0])
        y = min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])

        # des = QApplication.desktop()
        screen = QGuiApplication.primaryScreen()
        if screen:
            self.setWindowOpacity(0.0)
            pix = screen.grabWindow(0, x, y, width, height)
            pix.save('./data/scan.png')
            self.done.emit()
        self.close()

    def paintEvent(self, event):
        '''
        给出截图的辅助线
        :param event:
        :return:
        '''
        # logger.debug('开始画图')
        x = self.start[0]
        y = self.start[1]
        w = self.end[0] - x
        h = self.end[1] - y

        pp = QPainter(self)
        pp.drawRect(x, y, w, h)

    def mousePressEvent(self, event):

        # 点击左键开始选取截图区域
        if event.button() == Qt.LeftButton:
            self.start = (event.pos().x(), event.pos().y())
            # logger.debug('开始坐标：%s', self.start)

    def mouseReleaseEvent(self, event):

        # 鼠标左键释放开始截图操作
        if event.button() == Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            # logger.debug('结束坐标：%s', self.end)

            self.oksignal.emit()
            # logger.debug('信号提交')
            # 进行重新绘制
            self.update()

    def mouseMoveEvent(self, event):

        # 鼠标左键按下的同时移动鼠标绘制截图辅助线
        if event.buttons() and Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            # 进行重新绘制
            self.update()
