# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topiceval3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 704)
        MainWindow.setStyleSheet("QWidget#MainWindow {background-color:rgb(39, 39, 39)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMaxVisibleItems(4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 4, 1, 1, 3)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_8)
        self.gridLayout_3.addWidget(self.radioButton_8, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_10.setObjectName("radioButton_10")
        self.buttonGroup_2.addButton(self.radioButton_10)
        self.gridLayout_3.addWidget(self.radioButton_10, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_9.setObjectName("radioButton_9")
        self.buttonGroup_2.addButton(self.radioButton_9)
        self.gridLayout_3.addWidget(self.radioButton_9, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup_2.addButton(self.radioButton_7)
        self.gridLayout_3.addWidget(self.radioButton_7, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.gridLayout_3.addWidget(self.radioButton_6, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.scoreLabel_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel_2.setFont(font)
        self.scoreLabel_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.scoreLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel_2.setObjectName("scoreLabel_2")
        self.gridLayout_3.addWidget(self.scoreLabel_2, 0, 0, 1, 5)
        self.scoreLabel_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel_5.setFont(font)
        self.scoreLabel_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.scoreLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel_5.setObjectName("scoreLabel_5")
        self.gridLayout_3.addWidget(self.scoreLabel_5, 2, 0, 1, 5)
        self.radioButton_22 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_22.setFont(font)
        self.radioButton_22.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_22.setObjectName("radioButton_22")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.radioButton_22)
        self.gridLayout_3.addWidget(self.radioButton_22, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_24 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_24.setFont(font)
        self.radioButton_24.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_24.setObjectName("radioButton_24")
        self.buttonGroup_5.addButton(self.radioButton_24)
        self.gridLayout_3.addWidget(self.radioButton_24, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_23 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_23.setFont(font)
        self.radioButton_23.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_23.setObjectName("radioButton_23")
        self.buttonGroup_5.addButton(self.radioButton_23)
        self.gridLayout_3.addWidget(self.radioButton_23, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_21 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_21.setFont(font)
        self.radioButton_21.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_21.setObjectName("radioButton_21")
        self.buttonGroup_5.addButton(self.radioButton_21)
        self.gridLayout_3.addWidget(self.radioButton_21, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_25 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_25.setFont(font)
        self.radioButton_25.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_25.setObjectName("radioButton_25")
        self.buttonGroup_5.addButton(self.radioButton_25)
        self.gridLayout_3.addWidget(self.radioButton_25, 3, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_14.setObjectName("radioButton_14")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_14)
        self.gridLayout_4.addWidget(self.radioButton_14, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.scoreLabel_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel_3.setFont(font)
        self.scoreLabel_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.scoreLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel_3.setObjectName("scoreLabel_3")
        self.gridLayout_4.addWidget(self.scoreLabel_3, 0, 0, 1, 5)
        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_15.setObjectName("radioButton_15")
        self.buttonGroup_3.addButton(self.radioButton_15)
        self.gridLayout_4.addWidget(self.radioButton_15, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_12.setObjectName("radioButton_12")
        self.buttonGroup_3.addButton(self.radioButton_12)
        self.gridLayout_4.addWidget(self.radioButton_12, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_11.setObjectName("radioButton_11")
        self.buttonGroup_3.addButton(self.radioButton_11)
        self.gridLayout_4.addWidget(self.radioButton_11, 1, 4, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setMaxVisibleItems(4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_3, 5, 1, 1, 3)
        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_13.setObjectName("radioButton_13")
        self.buttonGroup_3.addButton(self.radioButton_13)
        self.gridLayout_4.addWidget(self.radioButton_13, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.scoreLabel_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel_6.setFont(font)
        self.scoreLabel_6.setStyleSheet("color:rgb(255, 255, 255)")
        self.scoreLabel_6.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel_6.setObjectName("scoreLabel_6")
        self.gridLayout_4.addWidget(self.scoreLabel_6, 2, 0, 1, 5)
        self.radioButton_28 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_28.setFont(font)
        self.radioButton_28.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_28.setObjectName("radioButton_28")
        self.buttonGroup_6 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.buttonGroup_6.addButton(self.radioButton_28)
        self.gridLayout_4.addWidget(self.radioButton_28, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_26 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_26.setFont(font)
        self.radioButton_26.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_26.setObjectName("radioButton_26")
        self.buttonGroup_6.addButton(self.radioButton_26)
        self.gridLayout_4.addWidget(self.radioButton_26, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_27 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_27.setFont(font)
        self.radioButton_27.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_27.setObjectName("radioButton_27")
        self.buttonGroup_6.addButton(self.radioButton_27)
        self.gridLayout_4.addWidget(self.radioButton_27, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_29 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_29.setFont(font)
        self.radioButton_29.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_29.setObjectName("radioButton_29")
        self.buttonGroup_6.addButton(self.radioButton_29)
        self.gridLayout_4.addWidget(self.radioButton_29, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_30 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_30.setFont(font)
        self.radioButton_30.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_30.setObjectName("radioButton_30")
        self.buttonGroup_6.addButton(self.radioButton_30)
        self.gridLayout_4.addWidget(self.radioButton_30, 3, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 9, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.showPrevious10PushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.showPrevious10PushButton_2.setObjectName("showPrevious10PushButton_2")
        self.horizontalLayout_2.addWidget(self.showPrevious10PushButton_2)
        self.showNext10PushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.showNext10PushButton_2.setObjectName("showNext10PushButton_2")
        self.horizontalLayout_2.addWidget(self.showNext10PushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 7, 1, 1)
        self.nextCommandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextCommandLinkButton.sizePolicy().hasHeightForWidth())
        self.nextCommandLinkButton.setSizePolicy(sizePolicy)
        self.nextCommandLinkButton.setStyleSheet("color:rgb(255, 255, 255)")
        self.nextCommandLinkButton.setObjectName("nextCommandLinkButton")
        self.gridLayout.addWidget(self.nextCommandLinkButton, 3, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalSepLine = QtWidgets.QFrame(self.centralwidget)
        self.verticalSepLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalSepLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalSepLine.setObjectName("verticalSepLine")
        self.gridLayout.addWidget(self.verticalSepLine, 0, 3, 4, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setAutoFillBackground(True)
        self.listWidget_2.setStyleSheet("color:rgb(85, 170, 255); border-bottom: 1px solid black")
        self.listWidget_2.setAlternatingRowColors(True)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_2.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_2.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_2.setUniformItemSizes(False)
        self.listWidget_2.setBatchSize(10)
        self.listWidget_2.setWordWrap(False)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 0, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 10, 1, 1)
        self.instructionsTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instructionsTextBrowser.sizePolicy().hasHeightForWidth())
        self.instructionsTextBrowser.setSizePolicy(sizePolicy)
        self.instructionsTextBrowser.setAutoFillBackground(False)
        self.instructionsTextBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.instructionsTextBrowser.setObjectName("instructionsTextBrowser")
        self.gridLayout.addWidget(self.instructionsTextBrowser, 0, 2, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.listWidget_1.setFont(font)
        self.listWidget_1.setAutoFillBackground(True)
        self.listWidget_1.setStyleSheet("color:rgb(85, 170, 255); border-bottom: 1px solid black")
        self.listWidget_1.setAlternatingRowColors(True)
        self.listWidget_1.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_1.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_1.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_1.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_1.setUniformItemSizes(False)
        self.listWidget_1.setBatchSize(10)
        self.listWidget_1.setWordWrap(False)
        self.listWidget_1.setObjectName("listWidget_1")
        self.gridLayout.addWidget(self.listWidget_1, 0, 5, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.showPrevious10PushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.showPrevious10PushButton_3.setObjectName("showPrevious10PushButton_3")
        self.horizontalLayout_3.addWidget(self.showPrevious10PushButton_3)
        self.showNext10PushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.showNext10PushButton_3.setObjectName("showNext10PushButton_3")
        self.horizontalLayout_3.addWidget(self.showNext10PushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 9, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showPrevious10PushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.showPrevious10PushButton_1.setObjectName("showPrevious10PushButton_1")
        self.horizontalLayout.addWidget(self.showPrevious10PushButton_1)
        self.showNext10PushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.showNext10PushButton_1.setObjectName("showNext10PushButton_1")
        self.horizontalLayout.addWidget(self.showNext10PushButton_1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 8, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_1 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_1.setObjectName("buttonGroup_1")
        self.buttonGroup_1.addButton(self.radioButton_4)
        self.gridLayout_2.addWidget(self.radioButton_4, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup_1.addButton(self.radioButton_5)
        self.gridLayout_2.addWidget(self.radioButton_5, 1, 4, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup_1.addButton(self.radioButton_2)
        self.gridLayout_2.addWidget(self.radioButton_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setMaxVisibleItems(4)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_1, 4, 1, 1, 3)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup_1.addButton(self.radioButton_3)
        self.gridLayout_2.addWidget(self.radioButton_3, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_1.setObjectName("radioButton_1")
        self.buttonGroup_1.addButton(self.radioButton_1)
        self.gridLayout_2.addWidget(self.radioButton_1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_18 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_18.setFont(font)
        self.radioButton_18.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_18.setObjectName("radioButton_18")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_18)
        self.gridLayout_2.addWidget(self.radioButton_18, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_19 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_19.setFont(font)
        self.radioButton_19.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_19.setObjectName("radioButton_19")
        self.buttonGroup_4.addButton(self.radioButton_19)
        self.gridLayout_2.addWidget(self.radioButton_19, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_16 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_16.setObjectName("radioButton_16")
        self.buttonGroup_4.addButton(self.radioButton_16)
        self.gridLayout_2.addWidget(self.radioButton_16, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_20 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_20.setFont(font)
        self.radioButton_20.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_20.setObjectName("radioButton_20")
        self.buttonGroup_4.addButton(self.radioButton_20)
        self.gridLayout_2.addWidget(self.radioButton_20, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_17 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_17.setObjectName("radioButton_17")
        self.buttonGroup_4.addButton(self.radioButton_17)
        self.gridLayout_2.addWidget(self.radioButton_17, 3, 4, 1, 1)
        self.scoreLabel_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel_1.setFont(font)
        self.scoreLabel_1.setStyleSheet("color:rgb(255, 255, 255)")
        self.scoreLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel_1.setObjectName("scoreLabel_1")
        self.gridLayout_2.addWidget(self.scoreLabel_1, 0, 0, 1, 5)
        self.scoreLabel_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel_4.setFont(font)
        self.scoreLabel_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.scoreLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel_4.setObjectName("scoreLabel_4")
        self.gridLayout_2.addWidget(self.scoreLabel_4, 2, 0, 1, 5)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 5, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.fontSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.fontSpinBox.setMinimum(6)
        self.fontSpinBox.setMaximum(30)
        self.fontSpinBox.setProperty("value", 17)
        self.fontSpinBox.setObjectName("fontSpinBox")
        self.horizontalLayout_4.addWidget(self.fontSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setAutoFillBackground(True)
        self.listWidget_3.setStyleSheet("color:rgb(85, 170, 255); border-bottom: 1px solid black")
        self.listWidget_3.setAlternatingRowColors(True)
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_3.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget_3.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_3.setUniformItemSizes(False)
        self.listWidget_3.setBatchSize(10)
        self.listWidget_3.setWordWrap(False)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 0, 9, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Topic Model Evaluation"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Label: None"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Fused"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Junk"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Unbalanced"))
        self.radioButton_8.setText(_translate("MainWindow", "5"))
        self.radioButton_10.setText(_translate("MainWindow", "2"))
        self.radioButton_9.setText(_translate("MainWindow", "3"))
        self.radioButton_7.setText(_translate("MainWindow", "1"))
        self.radioButton_6.setText(_translate("MainWindow", "4"))
        self.scoreLabel_2.setText(_translate("MainWindow", "Semantic Coherence Score"))
        self.scoreLabel_5.setText(_translate("MainWindow", "Thematic Relevance Score"))
        self.radioButton_22.setText(_translate("MainWindow", "1"))
        self.radioButton_24.setText(_translate("MainWindow", "2"))
        self.radioButton_23.setText(_translate("MainWindow", "3"))
        self.radioButton_21.setText(_translate("MainWindow", "4"))
        self.radioButton_25.setText(_translate("MainWindow", "5"))
        self.radioButton_14.setText(_translate("MainWindow", "4"))
        self.scoreLabel_3.setText(_translate("MainWindow", "Semantic Coherence Score"))
        self.radioButton_15.setText(_translate("MainWindow", "2"))
        self.radioButton_12.setText(_translate("MainWindow", "3"))
        self.radioButton_11.setText(_translate("MainWindow", "5"))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "Label: None"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Label: None"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Fused"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Junk"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Unbalanced"))
        self.radioButton_13.setText(_translate("MainWindow", "1"))
        self.scoreLabel_6.setText(_translate("MainWindow", "Thematic Relevance Score"))
        self.radioButton_28.setText(_translate("MainWindow", "1"))
        self.radioButton_26.setText(_translate("MainWindow", "2"))
        self.radioButton_27.setText(_translate("MainWindow", "3"))
        self.radioButton_29.setText(_translate("MainWindow", "4"))
        self.radioButton_30.setText(_translate("MainWindow", "5"))
        self.showPrevious10PushButton_2.setText(_translate("MainWindow", "Show Previous 10"))
        self.showNext10PushButton_2.setText(_translate("MainWindow", "Show Next 10"))
        self.nextCommandLinkButton.setText(_translate("MainWindow", "Next"))
        self.instructionsTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Instructions</span><span style=\" font-size:12pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1. The words represent top 10 words from one of the topics inferred from your emails, the top word is highest weighted and bottom word the lowest among the top 10.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2. Please select a score on a range of </span><span style=\" font-size:12pt; font-weight:600;\">1 (bad) to 5 (great)</span><span style=\" font-size:12pt;\"> based on the  critirea mentioned below</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3. You have to judge each topic based on:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Interpretability and Meaningfulness</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Ease with which you can provide a representative label to the topic</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Its merit in revealing a significant/interesting topic/theme in your mails</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- It is not too broad or too narrow in defining a theme. A broad topic would have multiple themes fused, and a narrow one would be too restricted and specific, applying to only ~ &lt;5 of your mails. </span></p></body></html>"))
        self.showPrevious10PushButton_3.setText(_translate("MainWindow", "Show Previous 10"))
        self.showNext10PushButton_3.setText(_translate("MainWindow", "Show Next 10"))
        self.showPrevious10PushButton_1.setText(_translate("MainWindow", "Show Previous 10"))
        self.showNext10PushButton_1.setText(_translate("MainWindow", "Show Next 10"))
        self.radioButton_4.setText(_translate("MainWindow", "4"))
        self.radioButton_5.setText(_translate("MainWindow", "5"))
        self.radioButton_2.setText(_translate("MainWindow", "2"))
        self.comboBox_1.setCurrentText(_translate("MainWindow", "Label: None"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "Label: None"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Fused"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Junk"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "Unbalanced"))
        self.radioButton_3.setText(_translate("MainWindow", "3"))
        self.radioButton_1.setText(_translate("MainWindow", "1"))
        self.radioButton_18.setText(_translate("MainWindow", "1"))
        self.radioButton_19.setText(_translate("MainWindow", "2"))
        self.radioButton_16.setText(_translate("MainWindow", "3"))
        self.radioButton_20.setText(_translate("MainWindow", "4"))
        self.radioButton_17.setText(_translate("MainWindow", "5"))
        self.scoreLabel_1.setText(_translate("MainWindow", "Semantic Coherence Score"))
        self.scoreLabel_4.setText(_translate("MainWindow", "Thematic Relevance Score"))
        self.label.setText(_translate("MainWindow", "Font Size:"))

