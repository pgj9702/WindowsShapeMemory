import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SystemTrayIcon(QSystemTrayIcon):
    icon_path = r'image\tray_icon.png'
    # icon = QIcon(icon_path)

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)

        # main main_menu
        main_menu = QMenu(parent)

        openAction = main_menu.addAction("설정")

        sub_menu = main_menu.addMenu('test')

        exitAction = main_menu.addAction("종료")

        exitAction.triggered.connect(QCoreApplication.instance().quit)

        self.setContextMenu(main_menu)

        self.activated.connect(self.Activation_Reason)

    def Activation_Reason(self, index):
        if index == 2 :
            print ("Double Click")

def main():
    app = QApplication(sys.argv)

    w = QWidget()

    trayIcon = SystemTrayIcon(QIcon(SystemTrayIcon.icon_path), w)

    trayIcon.show()

    # trayIcon.showMessage("제목", "내용", 1, 10000)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()