import copy
from datetime import datetime
import pyautogui
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


class WindowsControl:
    windows_handle = []
    windows_info = []
    windows_info_datetime_list = []  # (datetime, WindowInfo)

    # windows_handle
    def set_windows_handle(self):
        self.windows_handle = pyautogui.getAllWindows()

    def clear_windows_handle(self):
        self.windows_handle.clear()

    # windows_info_datetime_list
    def append_windows_info_with_datetime(self):
        temp_list = []
        self.set_windows_handle()

        for handle in self.windows_handle:
            if handle.width == 0 and handle.height == 0:
                continue

            temp_window_info = WindowInfo(handle_repr=repr(handle),
                                          title=handle.title,
                                          top=handle.top,
                                          left=handle.left,
                                          width=handle.width,
                                          height=handle.height,
                                          isActive=handle.isActive,
                                          isMaximized=handle.isMaximized,
                                          isMinimized=handle.isMinimized)

            temp_list.append(temp_window_info)

        self.windows_info_datetime_list.append((datetime.now(), temp_list))
        self.clear_windows_handle()

    def set_windows_info_to_list(self, index):
        self.windows_info = copy.copy(self.windows_info_datetime_list[index][1])

    def set_window_shape(self, index):
        self.set_windows_info_to_list(index)
        self.set_windows_handle()

        for handle in self.windows_handle:
            if handle.width == 0 and handle.height == 0:
                continue

            for idx, val in enumerate(self.windows_info):
                if repr(handle) == val.handle_repr:
                    try:
                        handle.moveTo(val.left, val.top)
                        handle.width = val.width
                        handle.height = val.height
                        handle.isActive = val.isActive
                        handle.isMaximized = val.isMaximized
                        handle.isMinimized = val.isMinimized

                    except (Exception,):
                        pass
                        # print(repr(handle), handle.title, handle.width, handle.height, handle.top, handle.left)

                    finally:
                        self.windows_info.pop(idx)

        self.clear_windows_handle()

    def remove_windows_info_datetime_list(self, index):
        self.windows_info_datetime_list.pop(index)


    def clear_windows_info_datetime_list(self):
        self.windows_info_datetime_list.clear()

    # datetime_list
    def get_datetime_list(self, index):
        return [i[0] for i in self.windows_info_datetime_list]


if __name__ == '__main__':
    monitor_info = WindowsControl()

    monitor_info.set_windows_handle()

    for i in monitor_info.windows_handle:
        print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )


    # monitor_info.append_windows_info_with_datetime()

    # input()

    # monitor_info.set_window_shape(-1)

    # monitor_info.clear_windows_handle()

    # monitor_info.set_windows_handle()
    #
    # monitor_info.append_windows_info_with_datetime()
    #
    # for i in monitor_info.windows_info_datetime_list[0]:
    #     if i.isActive:
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )
    #
    # for i in monitor_info.windows_info_datetime_list[1]:
    #     if i.isActive:
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    # for i in pyautogui.getAllWindows():
    #     if i.visible :
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    # print(type(datetime.now()))

    # app = QApplication([])
