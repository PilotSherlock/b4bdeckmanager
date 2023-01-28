import sys
import json
import os
import shutil
import re

import requests
from PySide6.QtWidgets import QMainWindow,QMessageBox,QInputDialog,QApplication,QDialog
from PySide6.QtCore import QUrl,Signal,QTranslator,QCoreApplication
from PySide6.QtGui import QDesktopServices,QActionGroup,QAction
import ui.ui_decksmanager as ui_decksmanager
import ui.ui_pushdeck as ui_pushdeck


from src.cards import CardsSet
from src.screenshot import ScreenShotsWin
from src.importingame import AutoImport
from src.paddleocr import Ocr
from src.recommenddeck import RecommendDeck

TRANSLATOR = QTranslator()

class CardsManager(QMainWindow):
    #信号 向推荐卡组的子窗口传参tuple(卡组名字,[卡组])/signal
    signal_current_deck = Signal(tuple)
    def __init__(self,app):
        super().__init__()
        self.version = "0.2.0"

        self.app=app
        self.cards = CardsSet()
        self.ui = ui_decksmanager.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_config()
        self.recommendCards = RecommendDeck().get_recommend_deck(self.config['language'])
        #子窗口/subwindows
        self.subwindow_push_deck = Window_push_deck()

        #语言选择/select language
        self.languageActionGroup = QActionGroup(self.ui.menu_3)
        self.languageActionGroup.addAction(self.ui.actionChinese)
        self.languageActionGroup.addAction(self.ui.actionEnglish)
        self.languageActionGroup.triggered[QAction].connect(self.select_language)
        self.languageActionGroup.triggered[QAction].connect(self.update_recommend_deck_without_messagebox)
        #启动检查更新/check update
        try:
            self.check_update(0)
        except:
            pass
        #初始化数据/init data
        self.init_data()
        #------菜单-----menu---------
        self.ui.action_info.triggered.connect(self.get_version_info)
        self.ui.actionGithub.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/PilotSherlock/b4bdeckmanager")))
        self.ui.actioncheck.triggered.connect(lambda:self.check_update(1))
        self.ui.actioncheckDeck.triggered.connect(self.update_recommend_deck)
        #选择卡组/select deck
        self.ui.listWidget_cardSet.itemSelectionChanged.connect(self.update_listWidget_cards)
        self.ui.listWidget_cardSet_recommend.itemSelectionChanged.connect(self.update_listWidget_recommend_cards)
        #添加卡组/add deck
        self.ui.pushButton_insertSet.clicked.connect(self.add_set)
        #删除卡组/delet deck
        self.ui.pushButton_deletSet.clicked.connect(self.delet_set)
        #重命名/rename deck
        self.ui.pushButton_renameSet.clicked.connect(self.rename_set)
        #添加卡牌/add card
        self.ui.pushButton_insertCard.clicked.connect(self.add_card)
        #删除卡牌/delet card
        self.ui.pushButton_deletCard.clicked.connect(self.delet_card)
        #生成分享码/share by str
        self.ui.pushButton_shareCode.clicked.connect(self.share)
        #分享码导入/import by str
        self.ui.pushButton_codeImport.clicked.connect(self.importByshare)
        #截图导入/import by ovr
        self.ui.pushButton_ocrImport.clicked.connect(self.screenshot)
        #导入游戏/apply in game
        self.ui.pushButton_importInGame.clicked.connect(self.importTogame)
        self.ui.pushButton_importInGame_recommend.clicked.connect(self.importTogame_recommend)
        #推送推荐卡组
        self.ui.pushButton_recommend.clicked.connect(self.push_deck)
        self.signal_current_deck.connect(self.subwindow_push_deck.get_signal_from_mainwindow)
    def init_config(self):
        if not os.path.isfile("config.json"):
            with open("config.json","w") as cf:
                self.config = {"language":"cn_zh","ignore_version":"0.0.0"}
                json.dump(self.config ,cf,ensure_ascii=False)
        else:
            with open("config.json","r") as cf:
                self.config = json.load(cf)
        if self.config ['language'] == "en":
            TRANSLATOR.load('en',directory=os.path.join(os.getcwd(),"language"))
            self.ui.retranslateUi(self)

    #数据框更新/update listwidget
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
            self.ui.textBrowser_author.clear()
            self.ui.textBrowser_author.setPlainText(self.recommendCards[currentSet]['author'])
            self.ui.textBrowser_deck_info.clear()
            self.ui.textBrowser_deck_info.setPlainText(self.recommendCards[currentSet]['info'])
            self.ui.textBrowser_game_version.clear()
            self.ui.textBrowser_game_version.setPlainText(self.recommendCards[currentSet]['version'])
            self.ui.textBrowser_game_difficulty.setPlainText(self.recommendCards[currentSet]['difficulty'])
        except:
            pass
    #初始化显示数据/init data
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
        self.recommendCards = RecommendDeck().get_recommend_deck(self.config['language'])
        self.update_listWidget_recommend_cardSet()
        self.ui.listWidget_cardSet_recommend.setCurrentRow(0)
        self.update_listWidget_recommend_cards()
        self.ui.listWidget_cards_recommend.setCurrentRow(0)
        if self.recommendCards:
            QMessageBox.information(self,QCoreApplication.translate("MessageBox","更新",None),QCoreApplication.translate("MessageBox","推荐卡组更新成功",None))
    def update_recommend_deck_without_messagebox(self):
        self.recommendCards = RecommendDeck().get_recommend_deck(self.config['language'])
        self.update_listWidget_recommend_cardSet()
        self.ui.listWidget_cardSet_recommend.setCurrentRow(0)
        self.update_listWidget_recommend_cards()
        self.ui.listWidget_cards_recommend.setCurrentRow(0)


    #版本信息的弹窗/version info
    def get_version_info(self):
        QMessageBox.information(self,QCoreApplication.translate("MessageBox","版本信息",None),self.version)

    #检查是否有新版本/check_update
    def check_update(self,flag):
        url_cn_zh ="https://raw.githubusercontent.com/PilotSherlock/b4bdeckmanager/master/UpdateLog/update_log_cn_zh.md"
        url_en = "https://raw.githubusercontent.com/PilotSherlock/b4bdeckmanager/master/UpdateLog/update_log_en.md"
        response_latest_version = requests.get("https://api.github.com/repos/PilotSherlock/b4bdeckmanager/releases/latest").json()
        try:
            latest_version = response_latest_version['tag_name'].split("v")[1]
            if self.config['language'] == "en":
                response_update_log= requests.get(url_en).text
            else:
                response_update_log= requests.get(url_cn_zh).text
            try:
                latest_version = response_latest_version['tag_name'].split("v")[1]
            except:
                QMessageBox.warning(self,self.version,response_latest_version['message'])
            pattern = re.compile(r'## V(.*?) ')
            versions = pattern.findall(response_update_log)
            log_latest_version = max(versions)

            log_start = response_update_log.index(f'## V{log_latest_version}')
            try:
                log_end = response_update_log.index(f'## V', log_start+1)
            except:
                log_end = len(response_update_log)
            latest_version_infromation = response_update_log[log_start:len(response_update_log)]
            if not self.config['ignore_version'] == latest_version:
                if latest_version > self.version:
                    ret = QMessageBox.question(self,f"V{latest_version}",latest_version_infromation,QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)
                    if ret == QMessageBox.Ok:
                        QDesktopServices.openUrl(QUrl("https://github.com/PilotSherlock/b4bdeckmanager/releases"))
                    if ret == QMessageBox.Ignore:
                        with open("config.json","w") as cf:
                            self.config['ignore_version'] = latest_version
                            json.dump(self.config,cf)
                elif flag == 1:
                    QMessageBox.information(self,QCoreApplication.translate("MessageBox","当前已是最新版本",None),latest_version_infromation)
            else:
                if flag == 1:
                    QMessageBox.information(self,QCoreApplication.translate("MessageBox","当前已是最新版本",None),latest_version_infromation)
        except:
            QMessageBox.warning(self,self.version,response_latest_version['message'])

    #删除卡组
    def delet_set(self):
        try:
            currentCardSet = self.ui.listWidget_cardSet.currentItem().text()
            self.cards.cards.pop(currentCardSet)
            self.cards.update()
            self.update_listWidget_cardSet()
            self.update_listWidget_cards()
        except:
            pass

    #删除卡牌
    def delet_card(self):
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
            cardName,ok = QInputDialog.getText(self,QCoreApplication.translate("MessageBox","输入卡牌名字",None),QCoreApplication.translate("MessageBox","输入卡牌名字",None))
            if ok:
                self.cards.cards[currentCardSet].append(cardName)
                self.cards.update()
                self.update_listWidget_cards()
        except:
            pass
    #添加卡组
    def add_set(self):
        try:
            setName,ok = QInputDialog.getText(self,QCoreApplication.translate("MessageBox","输入卡组名字",None),QCoreApplication.translate("MessageBox","输入卡组名字",None))
            if ok:
                self.cards.cards[setName] = list()
                self.cards.update()
                self.update_listWidget_cardSet()
        except:
            pass

    #重命名卡组
    def rename_set(self):
        try:
            setName,ok = QInputDialog.getText(self,QCoreApplication.translate("MessageBox","输入卡组名字",None),QCoreApplication.translate("MessageBox","输入卡组名字",None))
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
            QMessageBox.information(self,QCoreApplication.translate("MessageBox","复制成功",None),QCoreApplication.translate("MessageBox","分享码已经复制到剪贴板",None))
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
            QMessageBox.warning(self,QCoreApplication.translate("MessageBox","请等待OCR模块解压",None),QCoreApplication.translate("MessageBox","请等待OCR模块解压",None))
            shutil.unpack_archive(zip_file, folder)
            QMessageBox.information(self,QCoreApplication.translate("MessageBox","OCR模块解压完成",None),QCoreApplication.translate("MessageBox","OCR模块解压完成",None))
            screenshot = ScreenShotsWin()
            screenshot.showFullScreen()
            screenshot.done.connect(self.importByimg)
        elif not os.path.exists(zip_file) and not os.path.exists(folder):
            QMessageBox.warning(self,QCoreApplication.translate("MessageBox","OCR功能不可用",None),QCoreApplication.translate("MessageBox","OCR功能不可用,请下载PaddleOCR-json.zip文件放入同目录",None))
        else:
            screenshot = ScreenShotsWin()
            screenshot.showFullScreen()
            screenshot.done.connect(self.importByimg)
    #图片导入
    def importByimg(self):
        try:
            setName,ok = QInputDialog.getText(self,QCoreApplication.translate("MessageBox","输入卡组名字",None),QCoreApplication.translate("MessageBox","输入卡组名字",None))
            ocr = Ocr()
            cards = ocr.to_list("../data/scan.png")
            cardsSet = {setName:cards}
            self.ui.textEdit_shareCode.setPlainText(json.dumps(cardsSet,ensure_ascii=False))
            self.ui.pushButton_codeImport.click()
            QMessageBox.information(self,QCoreApplication.translate("MessageBox","导入成功",None),QCoreApplication.translate("MessageBox","导入成功",None))
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
    #选择语言/select language
    def select_language(self,action):
        if action == self.ui.actionEnglish:
            TRANSLATOR.load('en',directory=os.path.join(os.getcwd(),"language"))
            with open("config.json","w") as cf:
                self.config['language'] = "en"
                json.dump(self.config,cf)
        else:
            TRANSLATOR.load('')
            with open("config.json","w") as cf:
                self.config['language'] = "cn_zh"
                json.dump(self.config,cf)
        self.ui.retranslateUi(self)
        self.subwindow_push_deck.ui.retranslateUi(self.subwindow_push_deck)
    #推送推荐卡组
    def push_deck(self):
        try:
            deck = (self.ui.listWidget_cardSet.currentItem().text(),self.cards.cards[self.ui.listWidget_cardSet.currentItem().text()])
            self.signal_current_deck.emit(deck)
            self.subwindow_push_deck.show()
        except:
            pass


    #关闭/close event
    def closeEvent(self, event):
        sys.exit(0)


class Window_push_deck(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_pushdeck.Ui_Dialog_push_deck()
        self.ui.setupUi(self)
        self.ui.pushButton_importInGame_recommend.clicked.connect(self.push)

        with open("config.json","r") as cf:
            self.config = json.load(cf)

    def get_signal_from_mainwindow(self,deck):
        self.deck = deck


    def push(self):
        rezult = {}
        rezult["name"] = self.deck[0]
        if not self.ui.textEdit_author.toPlainText() == "" and not self.ui.textEdit_deck_info.toPlainText() == "" and not self.ui.textEdit_game_version.toPlainText() == "":
            rezult["data"] = {"deck":self.deck[1],"author":self.ui.textEdit_author.toPlainText(),"info":self.ui.textEdit_deck_info.toPlainText(),"version":self.ui.textEdit_game_version.toPlainText(),"difficulty":self.ui.comboBox_difficulty.currentText(),"language":self.config['language']}
            respons = requests.post("https://sherlock117.com:8001/share",data=json.dumps(rezult)).json()
            try:
                if respons["code"] == 1:
                    QMessageBox.information(self,QCoreApplication.translate("MessageBox","信息",None),QCoreApplication.translate("MessageBox","分享成功,等待审核",None))
                elif respons["code"] == 2:
                    QMessageBox.information(self,QCoreApplication.translate("MessageBox","信息",None),QCoreApplication.translate("MessageBox","分享失败:卡组名存在,请换一个名字",None))
            except:
                QMessageBox.information(self,QCoreApplication.translate("MessageBox","信息",None),QCoreApplication.translate("MessageBox","分享失败:{}".format(respons["message"]),None))
            self.close()
        else:
            QMessageBox.information(self,QCoreApplication.translate("MessageBox","信息",None),QCoreApplication.translate("MessageBox","请填写数据",None))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.installTranslator(TRANSLATOR)
    widget = CardsManager(app)
    widget.show()
    sys.exit(app.exec())
