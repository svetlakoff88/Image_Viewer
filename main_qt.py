#!usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

import imageio
from PyQt5 import QtWidgets, QtGui, QtCore
import design
import logic
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QLabel, QWidget
import cv2

class WindowQt(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        widget = self.centralwidget
        self.graphic = QtWidgets.QGraphicsView(widget)
        self.graphic.setGeometry(110, 10, 581, 501)
        self.pushButton_4.clicked.connect(lambda: self.dir_read())

    def dir_read(self):
        res = list()
        try:
            cd = logic.dir_read(QtWidgets.QFileDialog.getExistingDirectory(self, 'Add Directory'))
            res.append(cd)
            return self.img_view(res)
        except FileNotFoundError:
            pass

    def img_view(self, lst):
        raw_image = cv2.imread(lst[0][0])
        height, width, channel = raw_image.shape
        bytes_per_line = width*3
        image = QtGui.QImage(raw_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap=QtGui.QPixmap.fromImage(logic.path))
        self.graphic.setScene(scene)  # здесь метод отображения картинки в виджете
        #self.graphic.resize(pix.width(), pix.height())
        #self.resize(pix.width(), pix.height())


def app():
    applic = QtWidgets.QApplication(sys.argv)
    window = WindowQt()
    window.show()
    applic.exec()


if __name__ == '__main__':
    app()
