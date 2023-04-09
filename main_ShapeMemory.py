from tray_ShapeMemory import *


if __name__ == '__main__':
    run_app()

# pyinstaller -w -F -n=ShapeMemory -i=icon.ico --add-data="icon.ico;." main_ShapeMemory.py

# pyinstaller -F -n ShapeMemory -w -i icon.ico --add-data "icon.ico;." main_ShapeMemory.py