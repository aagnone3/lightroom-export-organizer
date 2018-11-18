"""
Simple user interface to use a file dialog to get a root directory from the user.
This is a liberal adaptation of https://pythonspot.com/pyqt5-file-dialog/
"""
import sys
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

from lightroom_export_organizer.org_folders import do, undo


class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Lightroom Export Organizer"
        self.init_ui()

    def get_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getExistingDirectory(
            self,
            "Select the directory where the photos are.",
            path.join(path.expanduser("~"), "Desktop"),
            options=options
        )

    def init_ui(self):
        self.setWindowTitle(self.title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    dir_base = ui.get_directory()
    print(dir_base)
    #if dir_base:
    #    sys.exit(do(dir_base))
    sys.exit(-1)
