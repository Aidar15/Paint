import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.uic.properties import QtGui


class Paint(QMainWindow):
    def __init__(self, parent=None):
        super(Paint, self).__init__(parent)
        uic.loadUi('paint_true.ui', self)

        title = "MinPaint"

        self.setWindowTitle(title)
        self.setFixedSize(700, 700)
        self.setWindowIcon(QIcon('static/icon.png'))

        self.background = Qt.white

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(self.background)

        self.drawing = False
        self.color = Qt.black
        self.brushSize = 2
        self.brushColor = Qt.black
        self.LastPoint = QPoint()

        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.save)

        self.actionClose.setShortcut("Ctrl+C")
        self.actionClose.triggered.connect(self.clear)

        self.actionBlack.setShortcut("Ctrl+Shift+B")
        self.actionBlack.triggered.connect(self.image_black)

        self.actionGray.setShortcut("Ctrl+Shift+G")
        self.actionGray.triggered.connect(self.image_gray)

        self.actionRed.setShortcut("Ctrl+Shift+R")
        self.actionRed.triggered.connect(self.image_red)

        self.actionYellow.setShortcut("Ctrl+Shift+Y")
        self.actionYellow.triggered.connect(self.image_yellow)

        self.actionBlue.setShortcut("Ctrl+Shift+L")
        self.actionBlue.triggered.connect(self.image_blue)

        self.actionGreen.setShortcut("Ctrl+Shift+E")
        self.actionGreen.triggered.connect(self.image_green)

        self.actionWhite.setShortcut("Ctrl+Shift+W")
        self.actionWhite.triggered.connect(self.image_white)

        self.actionOpen_Pallete.setShortcut("Ctrl+P")
        self.actionOpen_Pallete.triggered.connect(self.open_pallete)

        self.action3px.setShortcut("Ctrl+3")
        self.action3px.triggered.connect(self.three_px)

        self.action3px_2.setShortcut("Ctrl+Shift+3")
        self.action3px_2.triggered.connect(self.eraser_3)

        self.action5px.setShortcut("Ctrl+5")
        self.action5px.triggered.connect(self.five_px)

        self.action5px_2.setShortcut("Ctrl+Shift+5")
        self.action5px_2.triggered.connect(self.eraser_5)

        self.action7px.setShortcut("Ctrl+7")
        self.action7px.triggered.connect(self.seven_px)

        self.action7px_2.setShortcut("Ctrl+Shift+7")
        self.action7px_2.triggered.connect(self.eraser_7)

        self.action9px.setShortcut("Ctrl+9")
        self.action9px.triggered.connect(self.nine_px)

        self.action9px_2.setShortcut("Ctrl+Shift+9")
        self.action9px_2.triggered.connect(self.eraser_9)

        self.action11px.setShortcut("Ctrl+Shift+1")
        self.action11px.triggered.connect(self.eraser_11)

        self.action15px.setShortcut("Ctrl+Shift+F")
        self.action15px.triggered.connect(self.eraser_15)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.LastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.LastPoint, event.pos())
            self.LastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "File PNG(*.png);;File JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if file_path == "":
            return
        self.image.save(file_path)

    def clear(self):
        self.image.fill(self.background)
        self.update()

    def image_black(self):
        self.background = Qt.black
        self.image.fill(self.background)
        self.update()

    def image_red(self):
        self.background = Qt.red
        self.image.fill(self.background)
        self.update()

    def image_yellow(self):
        self.background = Qt.yellow
        self.image.fill(self.background)
        self.update()

    def image_blue(self):
        self.background = Qt.blue
        self.image.fill(self.background)
        self.update()

    def image_green(self):
        self.background = Qt.green
        self.image.fill(self.background)
        self.update()

    def image_gray(self):
        self.background = Qt.gray
        self.image.fill(self.background)
        self.update()

    def image_white(self):
        self.background = Qt.white
        self.image.fill(self.background)
        self.update()

    def three_px(self):
        self.brushColor = self.color
        self.brushSize = 3

    def five_px(self):
        self.brushColor = self.color
        self.brushSize = 5

    def seven_px(self):
        self.brushColor = self.color
        self.brushSize = 7

    def nine_px(self):
        self.brushColor = self.color
        self.brushSize = 9

    def eraser_3(self):
        self.brushSize = 3
        self.brushColor = self.background

    def eraser_5(self):
        self.brushSize = 5
        self.brushColor = self.background

    def eraser_7(self):
        self.brushSize = 7
        self.brushColor = self.background

    def eraser_9(self):
        self.brushSize = 9
        self.brushColor = self.background

    def eraser_11(self):
        self.brushSize = 11
        self.brushColor = self.background

    def eraser_15(self):
        self.brushSize = 15
        self.brushColor = self.background

    def open_pallete(self):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            self.brushColor = self.color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Paint()
    window.show()
    app.exec()
