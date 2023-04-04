import copy
from datetime import datetime
import PyQt5
import win32con
import win32process
import pyautogui
from win32api import GetSystemMetrics
from dataclasses import dataclass

@dataclass
class WindowInfo:
    handle_repr: str = ''
    title: str = ''
    top: int = 0
    left: int = 0
    width: int = 0
    height: int = 0
    isActive: bool = False
    isMaximized: bool = False
    isMinimized: bool = False


class MonitorInfo:
    windows_handle = []
    windows_info = []
    windows_info_list = []
    var_datetime = datetime
    datetime_list = []

    # constructor
    def __init__(self):
        pass


    # windows_handle
    def get_windows_handle(self):
        self.windows_handle = pyautogui.getAllWindows()

    def clear_windows_handle(self):
        self.windows_handle.clear()


    # windows_info_list
    def append_windows_info_list(self):
        temp_list = []
        self.get_windows_handle()

        for handle in self.windows_handle:
            temp_window_info = WindowInfo(handle_repr = handle.__repr__,
                                          title = handle.title,
                                          top = handle.top,
                                          left = handle.left,
                                          width = handle.width,
                                          height = handle.height,
                                          isActive = handle.isActive,
                                          isMaximized = handle.isMaximized,
                                          isMinimized = handle.isMinimized)

            temp_list.append(temp_window_info)

        self.windows_info_list.append(temp_list)
        self.clear_windows_handle()

    def get_windows_info_to_list(self, index):
        self.windows_info = copy.copy(self.windows_info_list[index])

    def set_window_shape(self, index):
        self.get_windows_info_to_list(index)
        self.get_windows_handle()

        for handle in self.windows_handle:
            for idx, val in enumerate(self.windows_info):
                if handle.__repr__ == val.handle_repr:
                    handle.move(val.left, val.top)
                    handle.resize(val.width, val.height)
                    val.pop(idx)

        self.clear_windows_handle()


    def remove_windows_info_list(self, index):
        self.windows_info_list.pop(index)

    def clear_windows_info_list(self):
        self.windows_info_list.clear()



    # datetime_list
    def append_now_datetime_list(self):
        self.datetime_list.append(datetime.now())

    def get_datetime_to_list(self, index):
        self.var_datetime = self.datetime_list[index]

    def remove_datetime_list(self, index):
        self.datetime_list.pop(index)

    def clear_datetime_list(self):
        self.datetime_list.clear()


if __name__ == '__main__':
    monitor_info = MonitorInfo()

    monitor_info.get_windows_handle()

    monitor_info.append_windows_info_list()

    for i in monitor_info.windows_info_list[0]:
        if i.isActive:
            print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    monitor_info.clear_windows_handle()

    pyautogui.getActiveWindow().move
    pyautogui.getActiveWindow().resize

    monitor_info.get_windows_handle()

    monitor_info.append_windows_info_list()

    for i in monitor_info.windows_info_list[0]:
        if i.isActive:
            print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    for i in monitor_info.windows_info_list[1]:
        if i.isActive:
            print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )


    # for i in pyautogui.getAllWindows():
    #     if i.visible :
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    print(type(datetime.now()))


    # app = QApplication([])