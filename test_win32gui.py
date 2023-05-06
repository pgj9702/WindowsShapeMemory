import copy

import win32con
import win32gui
import win32api


"""
- docu placement
https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-windowplacement

"""

def getWindowList():
    def callback(hwnd, hwnd_list: list):
        try:

            title = win32gui.GetWindowText(hwnd)

            if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
                hwnd_list.append((title, hwnd))

            result = True

        except Exception as e:
            win32api.MessageBox(0, 'getWindowList\n' + e, __name__, 16)

            result = False

        return result

    output = []

    win32gui.EnumWindows(callback, output)

    return output

if __name__ == '__main__':
    window_list = getWindowList()

    window_rect_list = []

    for title, hwnd in window_list:
        # win32gui.ShowWindow()

        hwnd_placement = win32gui.GetWindowPlacement(hwnd)

        window_rect_list.append((hwnd, hwnd_placement))

    a = input()

    for hwnd, rect in window_rect_list:
        win32gui.SetWindowPlacement(hwnd, rect)