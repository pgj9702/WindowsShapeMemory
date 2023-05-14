import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ctypes import windll
import threading
import win32gui

from settings import *
from windows_control import WindowsControl, LEN_DATETIME_FORMAT

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

    thread_get_win_message: threading.Thread

    datetime_menu_list = []


    def __init__(self, icon, parent=None):

        # thread_get_win_message
        # thread_get_win_message =

        QSystemTrayIcon.__init__(self, icon, parent)

        # main self.main_menu
        self.main_menu = QMenu(parent)

        # 설정 메뉴
        settings_action = self.main_menu.addAction("설정")

        # 화면 정보 전부 삭제
        clear_windows_info_action = self.main_menu.addAction("초기화")
        clear_windows_info_action.triggered.connect(self.add_menu_datetime_and_lock)

        # Seperator 추가
        self.main_menu.addSeparator()

        # Seperator 추가 (datetime_section)
        self.datetime_section = self.main_menu.addSeparator()

        # 화면 정보 추가 + 윈도우 잠금 메뉴
        add_windows_info_and_lock_action = self.main_menu.addAction("화면 저장 후 윈도우 잠금")
        add_windows_info_and_lock_action.triggered.connect(self.add_menu_datetime_and_lock)

        # 화면 정보 추가 메뉴
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

    def add_menu_datetime(self, text=''):

        # print('add_menu_datetime')

        try:
            current_time = self.append_windows_info_to_dict()

            action = self.main_menu.addAction(current_time + ' ' + text)

            action.triggered.connect(self.set_windows)

            self.datetime_menu_list.append(action)

            self.main_menu.insertAction(self.datetime_section, action)

            return 0

        except Exception as e:
            self.showMessage('Error', str(e))

            return -1

    def add_menu_datetime_and_lock(self):

        # print('add_menu_datetime_and_lock')

        if self.add_menu_datetime() == -1:
            self.showMessage('Error', '불러오기 실패')

            return -1

        else:
            windll.user32.LockWorkStation()

            return 0

    def remove_menu_datetime(self, index: int = 0):

        # print('remove_menu_datetime')

        if not (0 <= index < len(self.datetime_menu_list)):
            return -1

        try:
            temp_datetime = self.datetime_menu_list[index].text()
            self.main_menu.removeAction(self.datetime_menu_list[index])
            self.datetime_menu_list.pop(index)
            self.remove_from_dict(temp_datetime[0:LEN_DATETIME_FORMAT])

            return 0

        except Exception as e:
            self.showMessage('Error', str(e))

            return -1


    def clear_menu_datetime(self):
        try:
            for index, action in enumerate(self.datetime_menu_list):
                temp_datetime = action.text()
                self.main_menu.removeAction(action)
                self.datetime_menu_list.pop(index)
                self.remove_from_dict(temp_datetime[0:LEN_DATETIME_FORMAT])

            return 0

        except Exception as e:
            self.showMessage('Error', str(e))

            return -1


    def set_windows(self):

        # print('set_windows')

        if self.set_windows_from_dict(self.sender().text()[0:LEN_DATETIME_FORMAT]) == -1:
            self.showMessage('Error', '불러오기 실패')

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
