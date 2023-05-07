import win32gui
import win32api


"""
- docu placement
https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-windowplacement

"""


def get_hwnd_placement_list():
    def callback(hwnd, hwnd_list: list):
        try:

            if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):

                placement = win32gui.GetWindowPlacement(hwnd)

                hwnd_list.append((hwnd, placement))


        except Exception as e:
            win32api.MessageBox(0, 'error! getWindowList\n' + str(e), __name__, 16)

            return -1

    hwnd_placement_list = []

    win32gui.EnumWindows(callback, hwnd_placement_list)

    return hwnd_placement_list



if __name__ == '__main__':

    hwnd_placement_list = get_hwnd_placement_list()

    for i, v in hwnd_placement_list:
        print(i, v)
