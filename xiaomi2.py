# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\PythonDao\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
import time
# import PyQt5
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QDialog
# from PyQt5.QtGui import QPixmap
import socket
from socket import *
import threading

# TCP  客户端










# class  MyWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super(MyWindow,self).__init__()
#         self.groupBox = QtWidgets.QGroupBox(self)
#         self.groupBox.setGeometry(QtCore.QRect(30, 20, 971, 651))
#         self.groupBox.setObjectName("groupBox")
#         self.ceshi = QtWidgets.QPushButton(self.groupBox)
#         self.ceshi.setGeometry(QtCore.QRect(20, 50, 93, 28))
#         self.ceshi.setIconSize(QtCore.QSize(20, 20))
#         self.ceshi.setObjectName("ceshi")
#         self.caiji = QtWidgets.QPushButton(self.groupBox)
#         self.caiji.setGeometry(QtCore.QRect(20, 110, 93, 28))
#         self.caiji.setIconSize(QtCore.QSize(20, 20))
#         self.caiji.setObjectName("caiji")
#         self.lvbo = QtWidgets.QPushButton(self.groupBox)
#         self.lvbo.setGeometry(QtCore.QRect(20, 170, 93, 28))
#         self.lvbo.setIconSize(QtCore.QSize(20, 20))
#         self.lvbo.setObjectName("lvbo")
#         self.fenge = QtWidgets.QPushButton(self.groupBox)
#         self.fenge.setGeometry(QtCore.QRect(20, 230, 93, 28))
#         self.fenge.setIconSize(QtCore.QSize(20, 20))
#         self.fenge.setObjectName("fenge")
#         self.zhixin = QtWidgets.QPushButton(self.groupBox)
#         self.zhixin.setGeometry(QtCore.QRect(20, 290, 93, 28))
#         self.zhixin.setIconSize(QtCore.QSize(20, 20))
#         self.zhixin.setObjectName("zhixin")
#         self.juxing = QtWidgets.QPushButton(self.groupBox)
#         self.juxing.setGeometry(QtCore.QRect(20, 350, 93, 28))
#         self.juxing.setIconSize(QtCore.QSize(20, 20))
#         self.juxing.setObjectName("juxing")
#         self.label = QtWidgets.QLabel(self.groupBox)
#         self.label.setGeometry(QtCore.QRect(40, 410, 51, 16))
#         self.label.setObjectName("label")
#         self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
#         self.lineEdit.setGeometry(QtCore.QRect(22, 430, 91, 21))
#         self.lineEdit.setObjectName("lineEdit")
#         self.progressBar = QtWidgets.QProgressBar(self.groupBox)
#         self.progressBar.setGeometry(QtCore.QRect(10, 510, 131, 23))
#         self.progressBar.setProperty("value", 50)
#         self.progressBar.setObjectName("progressBar")
#         self.label_14 = QtWidgets.QLabel(self.groupBox)
#         self.label_14.setGeometry(QtCore.QRect(30, 480, 72, 15))
#         self.label_14.setObjectName("label_14")
#         self.groupBox_3 = QtWidgets.QGroupBox(self)
#         self.groupBox_3.setGeometry(QtCore.QRect(30, 700, 161, 121))
#         self.groupBox_3.setObjectName("groupBox_3")
#         self.label_2 = QtWidgets.QLabel(self.groupBox_3)
#         self.label_2.setGeometry(QtCore.QRect(10, 30, 61, 16))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(self.groupBox_3)
#         self.label_3.setGeometry(QtCore.QRect(80, 30, 81, 16))
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(self.groupBox_3)
#         self.label_4.setGeometry(QtCore.QRect(10, 60, 72, 15))
#         self.label_4.setObjectName("label_4")
#         self.label_5 = QtWidgets.QLabel(self.groupBox_3)
#         self.label_5.setGeometry(QtCore.QRect(90, 60, 41, 16))
#         self.label_5.setObjectName("label_5")
#         self.label_6 = QtWidgets.QLabel(self.groupBox_3)
#         self.label_6.setGeometry(QtCore.QRect(10, 90, 61, 16))
#         self.label_6.setObjectName("label_6")
#         self.label_7 = QtWidgets.QLabel(self.groupBox_3)
#         self.label_7.setGeometry(QtCore.QRect(70, 90, 81, 16))
#         self.label_7.setObjectName("label_7")
#         self.label_15 = QtWidgets.QLabel(self.groupBox)
#         self.label_15.setGeometry(QtCore.QRect(150, 30, 800, 600))
#         self.label_15.setObjectName("label_15")
#         self.groupBox_4 = QtWidgets.QGroupBox(self)
#         self.groupBox_4.setGeometry(QtCore.QRect(450, 700, 551, 121))
#         self.groupBox_4.setObjectName("groupBox_4")
#         self.label_8 = QtWidgets.QLabel(self.groupBox_4)
#         self.label_8.setGeometry(QtCore.QRect(20, 30, 41, 16))
#         self.label_8.setObjectName("label_8")
#         self.label_9 = QtWidgets.QLabel(self.groupBox_4)
#         self.label_9.setGeometry(QtCore.QRect(90, 30, 111, 16))
#         self.label_9.setObjectName("label_9")
#         self.label_10 = QtWidgets.QLabel(self.groupBox_4)
#         self.label_10.setGeometry(QtCore.QRect(20, 60, 41, 16))
#         self.label_10.setObjectName("label_10")
#         self.label_11 = QtWidgets.QLabel(self.groupBox_4)
#         self.label_11.setGeometry(QtCore.QRect(90, 60, 461, 16))
#         self.label_11.setObjectName("label_11")
#         self.label_12 = QtWidgets.QLabel(self.groupBox_4)
#         self.label_12.setGeometry(QtCore.QRect(21, 90, 41, 20))
#         self.label_12.setObjectName("label_12")
#         self.label_13 = QtWidgets.QLabel(self.groupBox_4)
#         self.label_13.setGeometry(QtCore.QRect(90, 90, 421, 16))
#         self.label_13.setObjectName("label_13")
#         self.retranslateUi()
#     def retranslateUi(self):
#         self.groupBox.setTitle("")
#         self.ceshi.setText("测试")
#         self.caiji.setText("采集图像")
#         self.lvbo.setText("滤波")
#         self.fenge.setText("分割")
#         self.zhixin.setText("质心")
#         self.juxing.setText("外接矩形")
#         self.label.setText("  VB")
#         self.label_14.setText("准备就绪")
#         self.groupBox_3.setTitle("版本信息")
#         self.label_2.setText("Author：")
#         self.label_3.setText("Lilinghua")
#         self.label_4.setText("Version：")
#         self.label_5.setText("v1.1")
#         self.label_6.setText("Time：")
#         self.label_7.setText("2018-07-28")
#         self.groupBox_4.setTitle("使用说明")
#         self.label_8.setText("功能：")
#         self.label_9.setText("操控嵌入式设备")
#         self.label_10.setText("用法：")
#         self.label_11.setText("测试按钮用于开发人员演示此工具，采集图像按钮进行现场图像采集")
#         self.label_12.setText("结果：")
#         self.label_13.setText("生成采集到的刀具图像的特征值，VB值")
#         # self.label_15.setText("图像显示")
#         self.label_15.setPixmap(QPixmap("E:\pandan.jpg"))
#         self.label_15.setScaledContents(True)           # 让图片自适应label大小
#         self.ceshi.clicked.connect(self.Test)           # 使用按钮信息
#         self.caiji.clicked.connect(self.Photo)
#         self.lvbo.clicked.connect(self.Filter)
#         self.fenge.clicked.connect(self.Comminute)
#         self.zhixin.clicked.connect(self.Centroid)
#         self.juxing.clicked.connect(self.Rectangle)
#
#     def ButtonFalse(self):
#         self.ceshi.setEnabled(False)
#         self.caiji.setEnabled(False)
#         self.lvbo.setEnabled(False)
#         self.fenge.setEnabled(False)
#         self.zhixin.setEnabled(False)
#         self.juxing.setEnabled(False)
#     def ButtonTrue(self):
#         self.ceshi.setEnabled(True)
#         self.caiji.setEnabled(True)
#         self.lvbo.setEnabled(True)
#         self.fenge.setEnabled(True)
#         self.zhixin.setEnabled(True)
#         self.juxing.setEnabled(True)
#     def Test(self):
#         self.ButtonFalse()
#         self.label_15.setPixmap(QPixmap(""))            # 移除label上的图片
#         self.label_15.setPixmap(QPixmap("E:\001.jpg"))
#         self.label_15.setScaledContents(True)           # 让图片自适应label大小
#         self.ButtonTrue()
#     def Photo(self):
#         self.ButtonFalse()
#         time.sleep(10)
#         print('Photo')
#         self.ButtonTrue()
#     def Filter(self):
#         time.sleep(2)
#         print('Filter')
#     def Comminute(self):
#         time.sleep(2)
#         print('Comminute')
#     def Centroid(self):
#         time.sleep(2)
#         print('Centroid')
#     def Rectangle(self):
#         time.sleep(2)
#         print('Rectangle=')

if __name__=="__main__":
    time.sleep(8)
    print('hello')
    # app = QtWidgets.QApplication(sys.argv)
    # my_show = MyWindow()
    # my_show.resize(1032, 851)            #重设窗口大小
    # my_show.setWindowTitle("数控刀具")  #设置窗口标题
    # my_show.show()
    # sys.exit(app.exec_())
