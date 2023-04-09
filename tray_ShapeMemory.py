import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ctypes import windll
from PyQt5 import uic

from settings import *
from windows_control import WindowsControl, WindowInfo
from datetime import datetime

# icon_path = r'image\tray_icon.png'
icon_path = r'.\icon.ico'

icon_file_name = 'icon.ico'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class SystemTrayIcon(QSystemTrayIcon, WindowsControl):
    
    main_men: QMenu

    datetime_section: QAction

    datetime_menu_list = []

    def __init__(self, icon, parent=None):

        QSystemTrayIcon.__init__(self, icon, parent)

        # main self.main_menu
        self.main_menu = QMenu(parent)

        # 설정 메뉴
        settings_action = self.main_menu.addAction("설정")

        # Seperator 추가
        self.main_menu.addSeparator()

        # Seperator 추가
        self.datetime_section = self.main_menu.addSeparator()

        # 윈도우 정보 추가 + 윈도우 잠금 메뉴
        add_windows_info_and_lock_action = self.main_menu.addAction("화면 저장 후 윈도우 잠금")
        add_windows_info_and_lock_action.triggered.connect(self.add_menu_datetime_and_lock)

        # 윈도우 정보 추가 메뉴
        add_windows_info_action = self.main_menu.addAction("화면 저장")
        add_windows_info_action.triggered.connect(self.add_menu_datetime)

        # Seperator 추가
        self.main_menu.addSeparator()

        # 종료 메뉴
        exit_action = self.main_menu.addAction("종료")

        exit_action.triggered.connect(sys.exit)

        self.setContextMenu(self.main_menu)

        self.activated.connect(self.activation_reason)


    def activation_reason(self, index):
        if index == 0:  # Unknown
            print("Unknown")
        if index == 1:  # Context
            print("Context")
        if index == 2:  # Double click
            print("Double Click")
        if index == 3:  # Trigger (click)
            print("Click")
        if index == 4:  # Middle Click
            print("Middle Click")


    def add_menu_datetime(self):

        print('add_menu_datetime')

        try:
            current_time = self.append_windows_info_with_datetime()

            action = self.main_menu.addAction(current_time)

            action.triggered.connect(self.set_windows)

            self.datetime_menu_list.append(action)

            self.main_menu.insertAction(self.datetime_section, action)

            return 0

        except Exception as e:
            self.showMessage(e)

            return -1


    def add_menu_datetime_and_lock(self):

        print('add_menu_datetime_and_lock')

        if self.add_menu_datetime() == -1:
            self.showMessage('불러오기 실패')

            return -1

        else:
            windll.user32.LockWorkStation()

            return 0


    def remove_menu_datetime(self, index: int = 1):

        print('remove_menu_datetime')

        self.main_menu.removeAction(self.datetime_menu_list[index])

        try:
            self.datetime_menu_list.pop(index)

            return 0

        except Exception as e:
            self.ShowMessage(e)

            return -1


    def set_windows(self):

        print('set_windows')

        if self.set_window_shape(self.sender().text()) == -1:
            self.showMessage('불러오기 실패')

            return -1

        else:
            return 0


def run_app():
    # main_ui = resource_path('main.ui')
    # Ui_MainWindow = uic.loadUiType(main_ui)[0]  # ui 가져오기

    app = QApplication(sys.argv)

    w = QWidget()

    ico = resource_path(icon_file_name)

    trayIcon = SystemTrayIcon(QIcon(ico), w)

    trayIcon.show()

    app.exec_()



if __name__ == '__main__':
    run_app()
