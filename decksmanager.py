import sys
import json
import os
import shutil

from PySide6.QtWidgets import QMainWindow,QMessageBox,QInputDialog,QApplication
from PySide6.QtCore import QUrl,QObject,Signal,Slot,QThread
from PySide6.QtGui import QDesktopServices
import ui_decksmanager


from scr.cards import CardsSet
from scr.screenshot import ScreenShotsWin
from scr.importingame import AutoImport
from scr.paddleocr import Ocr
from scr.update import update_onefile,check_updata,restart,ignore_version
from scr.recommenddeck import RecommendDeck
#update_thread
class Update_thread(QObject):
    finished = Signal()

    @Slot()
    def update(self):
        new,local,remote = check_updata(os.getcwd())
        update_onefile(os.getcwd(),local,remote)
        print("update done!")
        self.finished.emit()

class CardsManager(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.version = "0.0.1.0"
        self.app=app
        self.cards = CardsSet()
        self.recommendCards = RecommendDeck().get_recommend_deck()
        self.ui = ui_decksmanager.Ui_MainWindow()
        self.ui.setupUi(self)
        if os.path.isfile("upgrade.bat"):
            os.remove("upgrade.bat")
        #check updata
        try:
            self.check_update()
        except:
            pass
        #初始化数据
        self.init_data()
        #-------菜单--------------
        self.ui.action_info.triggered.connect(self.get_version_info)
        self.ui.actionGithub.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/PilotSherlock/b4bdeckmanager")))
        self.ui.actioncheck.triggered.connect(self.menu_check_update)
        self.ui.actioncheckDeck.triggered.connect(self.update_recommend_deck)
        #选择卡组
        self.ui.listWidget_cardSet.itemSelectionChanged.connect(self.update_listWidget_cards)
        self.ui.listWidget_cardSet_recommend.itemSelectionChanged.connect(self.update_listWidget_recommend_cards)
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

    def update_listWidget_recommend_cardSet(self):
        try:
            self.ui.listWidget_cardSet_recommend.clear()
            self.ui.listWidget_cardSet_recommend.addItems(self.recommendCards.keys())
        except:
            pass

    def update_listWidget_recommend_cards(self):
        try:
            currentSet = self.ui.listWidget_cardSet_recommend.currentItem().text()
            self.ui.listWidget_cards_recommend.clear()
            self.ui.listWidget_cards_recommend.addItems(self.recommendCards[currentSet]['deck'])
            self.ui.textBrowser_author.setPlainText(self.recommendCards[currentSet]['author'])
            self.ui.textBrowser_deck_info.setPlainText(self.recommendCards[currentSet]['info'])
            self.ui.textBrowser_game_version.setPlainText(self.recommendCards[currentSet]['version'])
        except:
            pass
    #初始化显示数据
    def init_data(self):
        self.update_listWidget_cardSet()
        self.ui.listWidget_cardSet.setCurrentRow(0)
        self.update_listWidget_cards()
        self.ui.listWidget_cards.setCurrentRow(0)
        self.update_listWidget_recommend_cardSet()
        self.ui.listWidget_cardSet_recommend.setCurrentRow(0)
        self.update_listWidget_recommend_cards()
        self.ui.listWidget_cards_recommend.setCurrentRow(0)
    #update recommend deck
    def update_recommend_deck(self):
        self.recommendCards = RecommendDeck().get_recommend_deck()
        self.update_listWidget_recommend_cardSet()
        self.ui.listWidget_cardSet_recommend.setCurrentRow(0)
        self.update_listWidget_recommend_cards()
        self.ui.listWidget_cards_recommend.setCurrentRow(0)
        if self.recommendCards:
            QMessageBox.information(self, "更新", "推荐卡组更新成功")

    #version info
    def get_version_info(self):
        QMessageBox.information(self, "版本信息", f"当前版本: {self.version}")
    #check_update
    def check_update(self):
        new,local,remote = check_updata(os.getcwd())
        if new is True:
            msg_check_update = QMessageBox()
            msg_check_update.setWindowTitle("更新")
            msg_check_update.setText("检测到新版本")
            msg_check_update.addButton(QMessageBox.Ok).setText("更新")
            msg_check_update.addButton(QMessageBox.Ignore).setText("忽略此版本")
            msg_check_update.addButton(QMessageBox.Cancel).setText("取消")
            ret = msg_check_update.exec()
            if ret == QMessageBox.Ok:
                self.thread = QThread()
                self.worker = Update_thread()
                self.worker.moveToThread(self.thread)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.update_and_restar)
                self.thread.started.connect(self.worker.update)
                self.thread.start()
            elif ret == QMessageBox.Ignore:
                ignore_version(os.getcwd(),local,remote)
            new,local,remote = check_updata(os.getcwd())
        else:
            return False

    def menu_check_update(self):
        if not self.check_update():
            QMessageBox.information(self,"更新","当前已是最新版本")
    #upgrade then restart new version
    def update_and_restar(self):
        msg_restart = QMessageBox()
        msg_restart.setWindowTitle("更新")
        msg_restart.setText("新版本下载完成,软件将重启更新")
        msg_restart.addButton(QMessageBox.Ok).setText("确定")
        ret = msg_restart.exec()
        if ret == QMessageBox.Ok:
            restart("decksmanager.exe")
            self.app.exit()
        else:
            restart("decksmanager.exe")
            self.app.exit()

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
    def importTogame_recommend(self):
        try:
            currentCardSet = self.ui.listWidget_cardSet_recommend.currentItem().text()
            auto = AutoImport(currentCardSet,self.recommendCards[currentCardSet]['deck'])
            auto.importCard()
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CardsManager(app)
    widget.show()
    sys.exit(app.exec())
