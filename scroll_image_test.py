###########################################################################
# Covert .ui file to .py
#    pyside2-uic "C:\Users\LR Admin\QtProjects\scroll_pictures\mainwindow.ui" -o "C:\Users\LR Admin\PycharmProjects\qt_stuff\gui_scroll_test.py"
###########################################################################

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QPixmap, QPalette, QPainter, QImage
from gui_scroll_test import Ui_MainWindow
import numpy as np
import sys
import cv2

basePath = "C:/Users/LR Admin/Downloads/Houses-dataset-master/Houses Dataset/"
savePath = "C:/Users/LR Admin/Python36/image.jpg"
PADDING = 20

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.create_image()
        self.label.setPixmap(QPixmap(savePath))
        self.scrollArea.setWidget(self.label)

    def create_image(self):
        newWidth = self.label.width()
        newHeight = self.label.height()
        row_zeros = np.zeros((PADDING,471,3))
        col_zeros = np.zeros(((261 * 4 + PADDING * 3), PADDING, 3))
        image = np.zeros((261 * 4 + PADDING * 3, 1, 3))
        num_rooms = 10
        for i in range(1,num_rooms+1):
            tmp = cv2.resize(cv2.imread(basePath + str(i) + "_bathroom.jpg"), (471,261))
            for room in ["bedroom", "frontal", "kitchen"]:
                newHeight += (261 + PADDING)
                imagePath = basePath + str(i) + "_" + room + ".jpg"
                input = cv2.resize(cv2.imread(imagePath), (471, 261))
                tmp = np.vstack((tmp, row_zeros, input))
            newWidth += 471
            image = np.hstack((image, tmp, col_zeros))

        image = image[:,:-20,:]
        cv2.imwrite(savePath, image)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())