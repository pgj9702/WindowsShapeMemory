from datetime import datetime
from dataclasses import dataclass
import win32gui

"""
- docu placement
https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-windowplacement

"""

DATETIME_FORMAT = '%m/%d %H:%M:%S'
LEN_DATETIME_FORMAT = len('%m/%d %H:%M:%S')


@dataclass
class WindowInfo:
    hwnd: int = 0
    title: str = ''
    placement: tuple = ()


class WindowsControl:
    dict_datetime_window_info = {}  # datetime: WindowInfo

    # append_windows_info_to_dict (datetime: WindowInfo)
    def append_windows_info_to_dict(self):
        def callback(hwnd, hwnd_list: list):
            title = win32gui.GetWindowText(hwnd)

            if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
                placement = win32gui.GetWindowPlacement(hwnd)

                temp_window_info = WindowInfo(hwnd=hwnd,
                                              title=title,
                                              placement=placement)

                hwnd_list.append(temp_window_info)

        window_info_list = []

        win32gui.EnumWindows(callback, window_info_list)

        current_time = datetime.now().strftime(DATETIME_FORMAT)

        self.dict_datetime_window_info[current_time] = window_info_list

        return current_time

    def set_windows_from_dict(self, key):
        window_info_list = self.dict_datetime_window_info[key]

        try:

            for window_info in window_info_list:
                win32gui.SetWindowPlacement(window_info.hwnd, window_info.placement)

        except (Exception,):
            pass

    def remove_from_dict(self, key):
        del (self.dict_datetime_window_info[key])

    def clear_dict(self):
        self.dict_datetime_window_info.clear()

    # get_datetime_list
    def get_datetime_list(self):
        return [key for key in self.dict_datetime_window_info.keys()]


if __name__ == '__main__':
    window_control = WindowsControl()

    window_control.append_windows_info_to_dict()

    print(window_control.get_datetime_list())

    a = input()

    window_control.set_windows_from_dict(a)
