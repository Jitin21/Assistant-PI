# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AI1Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1516, 867)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -10, 1541, 881))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gif4 = QtWidgets.QLabel(self.centralwidget)
        self.gif4.setGeometry(QtCore.QRect(0, 600, 1521, 271))
        self.gif4.setStyleSheet("")
        self.gif4.setText("")
        self.gif4.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/2.gif"))
        self.gif4.setScaledContents(True)
        self.gif4.setObjectName("gif4")
        
        self.png_date = QtWidgets.QLabel(self.centralwidget)
        self.png_date.setGeometry(QtCore.QRect(1200, 0, 321, 141))
        self.png_date.setStyleSheet("border:2px solid green;")
        self.png_date.setText("")
        self.png_date.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/Premium Vector _ Technology dark metal green light futuristic background_.jpg"))
        self.png_date.setScaledContents(True)
        self.png_date.setObjectName("png_date")
        
        self.png_time_2 = QtWidgets.QLabel(self.centralwidget)
        self.png_time_2.setGeometry(QtCore.QRect(0, 0, 301, 141))
        self.png_time_2.setStyleSheet("border:2px solid green;")
        self.png_time_2.setText("")
        self.png_time_2.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/Premium Vector _ Technology dark metal green light futuristic background_.jpg"))
        self.png_time_2.setScaledContents(True)
        self.png_time_2.setObjectName("png_time_2")
        
        self.png_time1 = QtWidgets.QLabel(self.centralwidget)
        self.png_time1.setGeometry(QtCore.QRect(10, 40, 281, 61))
        self.png_time1.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.png_time1.setText("")
        self.png_time1.setObjectName("png_time1")
        self.png_date1 = QtWidgets.QLabel(self.centralwidget)
        self.png_date1.setGeometry(QtCore.QRect(1204, 40, 301, 61))
        self.png_date1.setStyleSheet("color: rgb(0, 0, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")
        self.png_date1.setText("")
        self.png_date1.setObjectName("png_date1")
        
        self.gif1 = QtWidgets.QLabel(self.centralwidget)
        self.gif1.setGeometry(QtCore.QRect(300, 0, 901, 601))
        self.gif1.setStyleSheet("border:2px solid green;")
        self.gif1.setText("")
        self.gif1.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/giphy.gif"))
        self.gif1.setScaledContents(True)
        self.gif1.setObjectName("gif1")
        
        self.listen_gif = QtWidgets.QLabel(self.centralwidget)
        self.listen_gif.setGeometry(QtCore.QRect(300, 600, 901, 131))
        self.listen_gif.setStyleSheet("border:2px solid green;")
        self.listen_gif.setText("")
        self.listen_gif.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/4.gif"))
        self.listen_gif.setScaledContents(True)
        self.listen_gif.setObjectName("listen_gif")
        
        self.start_gif = QtWidgets.QLabel(self.centralwidget)
        self.start_gif.setGeometry(QtCore.QRect(0, 140, 301, 161))
        self.start_gif.setStyleSheet("border:2px solid green;\n"
"")
        self.start_gif.setText("")
        self.start_gif.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/Premium Vector _ Abstract background of futuristic sci-fi hud display.jpg"))
        self.start_gif.setScaledContents(True)
        self.start_gif.setObjectName("start_gif")
        
        self.exit_gif = QtWidgets.QLabel(self.centralwidget)
        self.exit_gif.setGeometry(QtCore.QRect(1200, 140, 321, 151))
        self.exit_gif.setStyleSheet("border:2px solid green;")
        self.exit_gif.setText("")
        self.exit_gif.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/Premium Vector _ Abstract background of futuristic sci-fi hud display.jpg"))
        self.exit_gif.setScaledContents(True)
        self.exit_gif.setObjectName("exit_gif")
        
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(60, 160, 181, 121))
        self.start.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(255, 255, 255,0%);\n"
"border-top-color: rgb(0, 0, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"")
        self.start.setIconSize(QtCore.QSize(100, 100))
        self.start.setObjectName("start")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1210, 140, 301, 151))
        self.exit.setStyleSheet("background-color: rgb(255, 255, 255,0%);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.exit.setIconSize(QtCore.QSize(100, 100))
        self.exit.setObjectName("exit")
        self.gif2 = QtWidgets.QLabel(self.centralwidget)
        self.gif2.setGeometry(QtCore.QRect(-10, 300, 311, 431))
        self.gif2.setStyleSheet("border:2px solid green;")
        self.gif2.setText("")
        self.gif2.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/8.gif"))
        self.gif2.setScaledContents(True)
        self.gif2.setObjectName("gif2")
        
        self.gif3 = QtWidgets.QLabel(self.centralwidget)
        self.gif3.setGeometry(QtCore.QRect(1200, 290, 331, 441))
        self.gif3.setStyleSheet("border:2px solid green;")
        self.gif3.setText("")
        self.gif3.setPixmap(QtGui.QPixmap("C:/Users/jitin/Downloads/7.gif"))
        self.gif3.setScaledContents(True)
        self.gif3.setObjectName("gif3")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "START"))
        self.exit.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
