import PyQt5
import win32con
import win32process
import pyautogui
from win32api import GetSystemMetrics
from dataclasses import dataclass


# app = QApplication([])


@dataclass
class windowInfo:
    id: int = None
    name: str = None
    top: int = 0
    left: int = 0
    width: int = 0
    height: int = 0

    def __init__(self, id: int, name: str, top: int, left: int, width: int, height: int):
        self.id = id
        self.name = name
        self.top = top
        self.left = left
        self.width = width
        self.height = height


class monitorInfo:
    windows_info = []

    # constructor
    def __init__(self):
        pass

    def get_windows_info(self):
        self.windows_info = pyautogui.getAllWindows()

    def clear_windows_info(self):
        self.windows_info = []


if __name__ == '__main__':
    monitor_info = monitorInfo()

    monitor_info.get_windows_info()

    pyautogui.getActiveWindow().left = 10

    print(type(pyautogui.getActiveWindow()))

    #
    # print(type(pyautogui.getActiveWindow()))
    #
    # print(type(pyautogui.getAllWindows()))
    #
    # for win in pyautogui.getAllWindows():
    #     print(win)
    #
    # print('test')
    #
    # for win in pyautogui.getWindowsWithTitle(''):
    #     print(win)
