import sys
import json
import os
import shutil

from PySide6.QtWidgets import QMainWindow,QMessageBox,QInputDialog,QApplication
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
import ui_decksmanager


from scr.cards import CardsSet
from scr.screenshot import ScreenShotsWin
from scr.importingame import AutoImport
from scr.paddleocr import Ocr

class CardsManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cards = CardsSet()
        self.ui = ui_decksmanager.Ui_MainWindow()
        self.ui.setupUi(self)
        #初始化数据
        self.init_data()
        #-------菜单--------------
        self.ui.action_info.triggered.connect(lambda: QMessageBox.information(None, "Info", "This is an information message"))
        self.ui.actionGithub.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/PilotSherlock/b4bdeckmanager")))
        #选择卡组
        self.ui.listWidget_cardSet.itemSelectionChanged.connect(self.update_listWidget_cards)
        #添加卡组
        self.ui.pushButton_insertSet.clicked.connect(self.add_set)
        #删除卡组
        self.ui.pushButton_delectSet.clicked.connect(self.delect_set)
        #重命名
        self.ui.pushButton_renameSet.clicked.connect(self.rename_set)
        #添加卡牌
        self.ui.pushButton_insertCard.clicked.connect(self.add_card)
        #删除卡牌
        self.ui.pushButton_delectCard.clicked.connect(self.delect_card)
        #生成分享码
        self.ui.pushButton_shareCode.clicked.connect(self.share)
        #分享码导入
        self.ui.pushButton_codeImport.clicked.connect(self.importByshare)
        #截图导入
        self.ui.pushButton_ocrImport.clicked.connect(self.screenshot)
        #导入游戏
        self.ui.pushButton_importInGame.clicked.connect(self.importTogame)

    #数据框更新
    def update_listWidget_cardSet(self):
        self.ui.listWidget_cardSet.clear()
        self.ui.listWidget_cardSet.addItems(self.cards.cards.keys())

    def update_listWidget_cards(self):
        try:
            currentSet = self.ui.listWidget_cardSet.currentItem().text()
            self.ui.listWidget_cards.clear()
            self.ui.listWidget_cards.addItems(self.cards.cards[currentSet])
        except:
            pass

    #初始化显示数据
    def init_data(self):
        self.update_listWidget_cardSet()
        self.ui.listWidget_cardSet.setCurrentRow(0)
        self.update_listWidget_cards()
        self.ui.listWidget_cards.setCurrentRow(0)


    #删除卡组
    def delect_set(self):
        try:
            currentCardSet = self.ui.listWidget_cardSet.currentItem().text()
            self.cards.cards.pop(currentCardSet)
            self.cards.update()
            self.update_listWidget_cardSet()
            self.update_listWidget_cards()
        except:
            pass

    #删除卡牌
    def delect_card(self):
        try:
            currentCardSet = self.ui.listWidget_cardSet.currentItem().text()
            currentCard = self.ui.listWidget_cards.currentItem().text()
            self.cards.cards[currentCardSet].remove(currentCard)
            self.cards.update()
            self.update_listWidget_cards()
        except:
            pass

    #添加卡牌
    def add_card(self):
        try:
            currentCardSet = self.ui.listWidget_cardSet.currentItem().text()
            cardName,ok = QInputDialog.getText(self,"输入卡牌名字","输入卡牌名字")
            if ok:
                self.cards.cards[currentCardSet].append(cardName)
                self.cards.update()
                self.update_listWidget_cards()
        except:
            pass
    #添加卡组
    def add_set(self):
        try:
            setName,ok = QInputDialog.getText(self,"输入卡组名字","输入卡组名字")
            if ok:
                self.cards.cards[setName] = list()
                self.cards.update()
                self.update_listWidget_cardSet()
        except:
            pass

    #重命名卡组
    def rename_set(self):
        try:
            setName,ok = QInputDialog.getText(self,"输入卡组名字","输入卡组名字")
            currentSet = self.ui.listWidget_cardSet.currentItem().text()
            if ok:
                self.cards.cards[setName] = self.cards.cards.pop(currentSet)
                self.cards.update()
                self.update_listWidget_cardSet()
        except:
            pass

    #分享字符串
    def share(self):
        try:
            currentSet = self.ui.listWidget_cardSet.currentItem().text()
            share_str = json.dumps({currentSet:self.cards.cards[currentSet]},ensure_ascii=False)
            clipboard = QApplication.clipboard()
            clipboard.setText(share_str)
            QMessageBox.information(self,"复制成功","分享码已经复制到剪贴板")
        except:
            pass

    #分享码导入
    def importByshare(self):
        if self.ui.textEdit_shareCode.toPlainText():
            try:
                share_dic = json.loads(self.ui.textEdit_shareCode.toPlainText()).popitem()
                self.cards.cards[share_dic[0]]=share_dic[1]
                self.cards.update()
                self.update_listWidget_cardSet()
            except:
                pass

    #截图
    def screenshot(self):
        zip_file = os.path.join(os.getcwd(),"PaddleOCR-json.zip")
        folder = os.path.join(os.getcwd(),"PaddleOCR-json")
        if os.path.exists(zip_file) and not os.path.exists(folder):
            QMessageBox.warning(self,"请等待OCR模块解压","请等待OCR模块解压")
            shutil.unpack_archive(zip_file, folder)
            QMessageBox.information(self,"OCR模块解压完成","OCR模块解压完成")
            screenshot = ScreenShotsWin()
            screenshot.showFullScreen()
            screenshot.done.connect(self.importByimg)
        elif not os.path.exists(zip_file) and not os.path.exists(folder):
            QMessageBox.warning(self,"OCR功能不可用","OCR功能不可用,请下载PaddleOCR-json.zip文件放入同目录")
        else:
            screenshot = ScreenShotsWin()
            screenshot.showFullScreen()
            screenshot.done.connect(self.importByimg)
    #图片导入
    def importByimg(self):
        try:
            setName,ok = QInputDialog.getText(self,"输入卡组名字","输入卡组名字")
            ocr = Ocr()
            cards = ocr.to_list("../data/scan.png")
            cardsSet = {setName:cards}
            self.ui.textEdit_shareCode.setPlainText(json.dumps(cardsSet,ensure_ascii=False))
            self.ui.pushButton_codeImport.click()
            QMessageBox.information(self,"导入成功","导入成功")
        except:
            pass
    #导入游戏
    def importTogame(self):
        try:
            currentCardSet = self.ui.listWidget_cardSet.currentItem().text()
            auto = AutoImport(currentCardSet,self.cards.cards[currentCardSet])
            auto.importCard()
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CardsManager()
    widget.show()
    sys.exit(app.exec())
