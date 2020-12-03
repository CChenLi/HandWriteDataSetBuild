import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tkinter as tk
import os

class Example(QMainWindow):
    def __init__(self, label, uid, batch, custompath=False):
        super(Example, self).__init__()
        self.label = label
        self.uid = uid
        self.batch = str(batch)
        self.custompath=custompath
        self.setWindowTitle("Press 'n' to save current and draw next")
        self.setGeometry(400, 400, 400, 400)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white) 
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu("File") 

        saveAction = QAction("Save", self) 
        saveAction.setShortcut("s") 
        fileMenu.addAction(saveAction) 
        saveAction.triggered.connect(self.save) 

        nextAction = QAction("Next", self)
        nextAction.setShortcut("n")
        fileMenu.addAction(nextAction)
        nextAction.triggered.connect(self.next)
        
        self.setMouseTracking(False)
        self.pos_xy = []

    def save(self): 
        pwd = os.getcwd()
        filePath = pwd + "/data/" + self.label + "_" + self.uid + "_" + self.batch + ".png"
        if self.custompath:
            filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ") 
        self.image.save(filePath) 
        print(filePath)

    def next(self):
        self.save()
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self.image)
        psudo_painter = QPainter()
        painter.begin(self)
        psudo_painter.begin(self)
        pen = QPen(Qt.black, 10, Qt.SolidLine)
        painter.setPen(pen)
        psudo_painter.setPen(pen)


        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for pos_tmp in self.pos_xy:
                point_end = pos_tmp

                if point_end == (-1, -1):
                    point_start = (-1, -1)
                    continue
                if point_start == (-1, -1):
                    point_start = point_end
                    continue

                painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                psudo_painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end
        painter.end()
        psudo_painter.end()

    def mouseMoveEvent(self, event):
        pos_tmp = (event.pos().x(), event.pos().y())
        self.pos_xy.append(pos_tmp)

        self.update()

    def mouseReleaseEvent(self, event):
        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)

        self.update()

if __name__ == "__main__":
    master = tk.Tk()
    master.title("Set config")
    tk.Label(master, text="Label").grid(row=0)
    tk.Label(master, text="UID").grid(row=1)
    tk.Label(master, text="Number of Images").grid(row=2)
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    tk.Button(master, 
          text='Start Drawing', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.mainloop()
app = QApplication(sys.argv)
for i in range(int(e3.get())):
    pyqt_learn = Example(e1.get(), e2.get(), i)
    pyqt_learn.show()
    app.exec_()
