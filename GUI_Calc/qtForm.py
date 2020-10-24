# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Anatoly_Pichugin\PycharmProjects\EpamPython\task1\GUI_Calc\qtForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 136)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        # self.lineEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditA = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditA.setMaximum(9999999)
        self.lineEditA.setMinimum(-9999999)

        self.lineEditA.setObjectName("lineEditA")
        self.gridLayout.addWidget(self.lineEditA, 2, 0, 1, 1)

        self.lineEditB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditB.setMaximum(9999999)
        self.lineEditB.setMinimum(-9999999)
        self.lineEditB.setObjectName("lineEditB")
        self.gridLayout.addWidget(self.lineEditB, 2, 2, 1, 1)

        self.cbx_oper = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_oper.setObjectName("cbx_oper")
        self.gridLayout.addWidget(self.cbx_oper, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_calc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calc.setObjectName("btn_calc")
        self.gridLayout.addWidget(self.btn_calc, 4, 1, 1, 1)

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python GUI Калькулятор"))
        self.label_2.setText(_translate("MainWindow", "Операция"))
        self.label_3.setText(_translate("MainWindow", "Второе число"))
        self.label.setText(_translate("MainWindow", "Первое число"))
        self.btn_calc.setText(_translate("MainWindow", "Calc"))
        self.label_result.setText(_translate("MainWindow", "Результат"))


class CalcWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 438)
        MainWindow.setMinimumSize(QtCore.QSize(394, 438))
        MainWindow.setMaximumSize(QtCore.QSize(394, 438))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 110, 392, 326))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_0.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 6, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_7.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 5, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_4.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_1.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 5, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_5.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 4, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_clear.setFont(font)
        self.btn_clear.setToolTip("")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_2.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 2, 1, 1)

        # self.btn_comma = QtWidgets.QPushButton(self.gridLayoutWidget)
        # self.btn_comma.setBaseSize(QtCore.QSize(25, 25))
        # font = QtGui.QFont()
        # font.setPointSize(25)
        # self.btn_comma.setFont(font)
        # self.btn_comma.setObjectName("btn_comma")
        # self.gridLayout.addWidget(self.btn_comma, 6, 4, 1, 1)

        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_9.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 5, 4, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_6.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 4, 4, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_3.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 4, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_div.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 1, 5, 1, 1)
        self.btn_multy = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_multy.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_multy.setFont(font)
        self.btn_multy.setObjectName("btn_multy")
        self.gridLayout.addWidget(self.btn_multy, 3, 5, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_minus.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 4, 5, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_add.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 5, 5, 1, 1)
        self.btn_calc = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_calc.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_calc.setFont(font)
        self.btn_calc.setObjectName("btn_calc")
        self.gridLayout.addWidget(self.btn_calc, 6, 5, 1, 1)
        self.btn_power = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_power.setBaseSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_power.setFont(font)
        self.btn_power.setObjectName("btn_power")
        self.gridLayout.addWidget(self.btn_power, 1, 4, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setDigitCount(10)
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd.setProperty("value", 0.0)
        self.lcd.setProperty("intValue", 0)
        self.lcd.setObjectName("lcd")
        self.verticalLayout.addWidget(self.lcd)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python GUI Калькулятор"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_2.setText(_translate("MainWindow", "2"))

        # self.btn_comma.setText(_translate("MainWindow", ","))

        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_multy.setText(_translate("MainWindow", "*"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_calc.setText(_translate("MainWindow", "="))
        self.btn_power.setText(_translate("MainWindow", "^"))