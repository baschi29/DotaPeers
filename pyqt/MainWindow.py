# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(626, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../dp-server/static/img/dotalogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background-color: rgb(189, 93, 56);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 9, 601, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.connectButton = QtWidgets.QPushButton(self.page1)
        self.connectButton.setGeometry(QtCore.QRect(190, 340, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.connectButton.setFont(font)
        self.connectButton.setFlat(False)
        self.connectButton.setObjectName("connectButton")
        self.infoLabel = QtWidgets.QLabel(self.page1)
        self.infoLabel.setGeometry(QtCore.QRect(110, 90, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.idEdit = QtWidgets.QLineEdit(self.page1)
        self.idEdit.setEnabled(True)
        self.idEdit.setGeometry(QtCore.QRect(120, 210, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idEdit.setFont(font)
        self.idEdit.setToolTip("")
        self.idEdit.setStatusTip("")
        self.idEdit.setStyleSheet("border-color: rgb(54, 54, 54);")
        self.idEdit.setInputMask("")
        self.idEdit.setText("")
        self.idEdit.setFrame(True)
        self.idEdit.setObjectName("idEdit")
        self.headerLabel = QtWidgets.QLabel(self.page1)
        self.headerLabel.setGeometry(QtCore.QRect(0, 0, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.errorLabel = QtWidgets.QLabel(self.page1)
        self.errorLabel.setGeometry(QtCore.QRect(120, 189, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(170, 0, 0);")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.headerLabel_2 = QtWidgets.QLabel(self.page2)
        self.headerLabel_2.setGeometry(QtCore.QRect(10, 10, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.headerLabel_2.setFont(font)
        self.headerLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel_2.setObjectName("headerLabel_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page2)
        self.textBrowser.setGeometry(QtCore.QRect(70, 120, 471, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textBrowser.setObjectName("textBrowser")
        self.logLabel = QtWidgets.QLabel(self.page2)
        self.logLabel.setGeometry(QtCore.QRect(70, 90, 471, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logLabel.setFont(font)
        self.logLabel.setObjectName("logLabel")
        self.stackedWidget.addWidget(self.page2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "DotaPeers"))
        self.connectButton.setText(_translate("mainWindow", "Connect Agent"))
        self.infoLabel.setText(_translate("mainWindow", "Enter your connection ID"))
        self.idEdit.setPlaceholderText(_translate("mainWindow", "Connection ID"))
        self.headerLabel.setText(_translate("mainWindow", "DotaPeers with Logo"))
        self.headerLabel_2.setText(_translate("mainWindow", "DotaPeers with Logo"))
        self.logLabel.setText(_translate("mainWindow", "Log"))
