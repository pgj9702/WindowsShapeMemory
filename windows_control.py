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
    windows_info_datetime_dict = {}  # datetime: WindowInfo

    # windows_handle
    def set_windows_handle(self):
        self.windows_handle = pyautogui.getAllWindows()

    def clear_windows_handle(self):
        self.windows_handle.clear()

    # windows_info_datetime_dict
    def append_windows_info_with_datetime(self):
        temp_list = []
        current_time: datetime
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

        current_time = datetime.now()
        self.windows_info_datetime_dict[current_time.strftime('%m/%d %H:%M:%S')] = temp_list
        self.clear_windows_handle()

        return current_time.strftime('%m/%d %H:%M:%S')

    def set_windows_info_to_dict(self, key):
        if key in self.windows_info_datetime_dict:
            self.windows_info = copy.copy(self.windows_info_datetime_dict[key])
            return 0
        else:
            return -1

    def set_window_shape(self, key):
        if self.set_windows_info_to_dict(key) == -1:
            return -1

        try:
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
                            break

            self.clear_windows_handle()

            return 0

        except (Exception,):
            return -1

    def remove_windows_info_datetime_dict(self, key):
        del(self.windows_info_datetime_dict[key])


    def clear_windows_info_datetime_dict(self):
        self.windows_info_datetime_dict.clear()

    # datetime_list
    def get_datetime_list(self):
        return [key for key, in self.windows_info_datetime_dict]


if __name__ == '__main__':

    print(datetime.now().strftime('%m/%d %H:%M:%S'))

    # monitor_info = WindowsControl()
    #
    # monitor_info.set_windows_handle()
    #
    # for i in monitor_info.windows_handle:
    #     print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )


    # monitor_info.append_windows_info_with_datetime()

    # input()

    # monitor_info.set_window_shape(-1)

    # monitor_info.clear_windows_handle()

    # monitor_info.set_windows_handle()
    #
    # monitor_info.append_windows_info_with_datetime()
    #
    # for i in monitor_info.windows_info_datetime_dict[0]:
    #     if i.isActive:
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )
    #
    # for i in monitor_info.windows_info_datetime_dict[1]:
    #     if i.isActive:
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    # for i in pyautogui.getAllWindows():
    #     if i.visible :
    #         print('test  ', i.title + '   ' , str(i.top), '   ', str(i.left) +  '   ', str(i.width),  '   ', str(i.height) )

    # print(type(datetime.now()))

    # app = QApplication([])