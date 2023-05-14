from tray_ShapeMemory import *
from app_singleton import SingleInstance
from setproctitle import getproctitle

if __name__ == '__main__':
    # sys.argv

    # current_prog = System.Diagnostics.Process.GetCurrentProcess().ProcessName.ToUpper()

    main = SingleInstance()

    run_app()


# pyinstaller -w -F -n=ShapeMemory -i=icon.ico --add-data="icon.ico;." main_ShapeMemory.py

# pyinstaller -F -n ShapeMemory -w -i icon.ico --add-data "icon.ico;." main_ShapeMemory.py
