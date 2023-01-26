import win32gui,win32api,win32con
import win32clipboard as wc
import time



class AutoImport():
    def __init__(self,setName,set):
        self.setName = setName
        self.cards = set
        self.hwnd = self.get_game_hwnd()
        self.left,self.top,self.right,self.bottom = win32gui.GetWindowRect(self.hwnd)
    def get_game_hwnd(self):
        hWnd_list = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
        for hwnd in hWnd_list:
            if "喋血复仇" in win32gui.GetWindowText(hwnd) or "Back 4 Blood" in win32gui.GetWindowText(hwnd):
                return hwnd
    def importCard(self):
        #创建卡组
        self.left,self.top,self.right,self.bottom = win32gui.GetWindowRect(self.hwnd)
        self.right = self.right-self.left
        self.bottom = self.bottom - self.top
        self.setCopy(self.setName)
        win32gui.SetForegroundWindow(self.hwnd)

        win32api.SetCursorPos([int(self.left+(200*self.right/1920)),int(self.top+(250*self.bottom/1080))])
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

        #卡组名
        time.sleep(0.5)
        win32api.SetCursorPos([int(self.left+(200*self.right/1920)),int(self.top+(330*self.bottom/1080))])
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        self.paste()
        #搜卡
        for card in self.cards:
            win32api.SetCursorPos([int(self.left+(1600*self.right/1920)),int(self.top+(170*self.bottom/1080))])
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.2)
            self.selectAll()
            if card in "前蹲!":
                self.setCopy("前蹲！")
            else:
                self.setCopy(card)
            time.sleep(0.2)
            self.paste()
            win32api.SetCursorPos([int(self.left+(650*self.right/1920)),int(self.top+(400*self.bottom/1080))])
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.2)
    # 写入剪切板内容
    def setCopy(self,str):
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, str)
        wc.CloseClipboard()


    def paste(self):
        win32api.keybd_event(17,0,0,0)
        time.sleep(0.1)
        win32api.keybd_event(86,0,0,0)
        time.sleep(0.1)
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)

    def selectAll(self):
        win32api.keybd_event(17,0,0,0)
        time.sleep(0.1)
        win32api.keybd_event(65,0,0,0)
        time.sleep(0.1)
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)