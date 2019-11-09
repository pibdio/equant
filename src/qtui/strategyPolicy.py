# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strategyPolicy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_strategyMainWin(object):
    def setupUi(self, strategyMainWin):
        strategyMainWin.setObjectName("strategyMainWin")
        strategyMainWin.resize(571, 616)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(strategyMainWin.sizePolicy().hasHeightForWidth())
        strategyMainWin.setSizePolicy(sizePolicy)
        strategyMainWin.setMinimumSize(QtCore.QSize(571, 616))
        strategyMainWin.setMaximumSize(QtCore.QSize(571, 616))
        self.centralwidget = QtWidgets.QWidget(strategyMainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.strategyTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.strategyTabWidget.setGeometry(QtCore.QRect(15, 14, 541, 531))
        self.strategyTabWidget.setObjectName("strategyTabWidget")
        self.runPolicy = QtWidgets.QWidget()
        self.runPolicy.setObjectName("runPolicy")
        self.trigger = QtWidgets.QGroupBox(self.runPolicy)
        self.trigger.setGeometry(QtCore.QRect(10, 10, 521, 171))
        self.trigger.setObjectName("trigger")
        self.KLineCheckBox = QtWidgets.QCheckBox(self.trigger)
        self.KLineCheckBox.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.KLineCheckBox.setChecked(True)
        self.KLineCheckBox.setObjectName("KLineCheckBox")
        self.snapShotCheckBox = QtWidgets.QCheckBox(self.trigger)
        self.snapShotCheckBox.setGeometry(QtCore.QRect(40, 60, 101, 16))
        self.snapShotCheckBox.setObjectName("snapShotCheckBox")
        self.tradeCheckBox = QtWidgets.QCheckBox(self.trigger)
        self.tradeCheckBox.setGeometry(QtCore.QRect(40, 90, 101, 16))
        self.tradeCheckBox.setObjectName("tradeCheckBox")
        self.cycleCheckBox = QtWidgets.QCheckBox(self.trigger)
        self.cycleCheckBox.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.cycleCheckBox.setObjectName("cycleCheckBox")
        self.cycleLineEdit = QtWidgets.QLineEdit(self.trigger)
        self.cycleLineEdit.setGeometry(QtCore.QRect(102, 118, 41, 20))
        self.cycleLineEdit.setObjectName("cycleLineEdit")
        self.label = QtWidgets.QLabel(self.trigger)
        self.label.setGeometry(QtCore.QRect(150, 120, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.trigger)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 54, 12))
        self.label_2.setObjectName("label_2")
        self.timerEdit = QtWidgets.QTimeEdit(self.trigger)
        self.timerEdit.setGeometry(QtCore.QRect(340, 140, 71, 22))
        self.timerEdit.setObjectName("timerEdit")
        self.addTimerButton = QtWidgets.QPushButton(self.trigger)
        self.addTimerButton.setGeometry(QtCore.QRect(419, 139, 41, 23))
        self.addTimerButton.setObjectName("addTimerButton")
        self.deleteTimerButton = QtWidgets.QPushButton(self.trigger)
        self.deleteTimerButton.setGeometry(QtCore.QRect(460, 139, 41, 23))
        self.deleteTimerButton.setObjectName("deleteTimerButton")
        self.timerListWidget = QtWidgets.QListWidget(self.trigger)
        self.timerListWidget.setGeometry(QtCore.QRect(340, 34, 171, 101))
        self.timerListWidget.setObjectName("timerListWidget")
        self.basePolicy = QtWidgets.QGroupBox(self.runPolicy)
        self.basePolicy.setGeometry(QtCore.QRect(10, 200, 521, 191))
        self.basePolicy.setObjectName("basePolicy")
        self.label_3 = QtWidgets.QLabel(self.basePolicy)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.basePolicy)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.basePolicy)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 54, 12))
        self.label_5.setObjectName("label_5")
        self.sendOrderRealtime = QtWidgets.QRadioButton(self.basePolicy)
        self.sendOrderRealtime.setGeometry(QtCore.QRect(120, 40, 89, 16))
        self.sendOrderRealtime.setChecked(True)
        self.sendOrderRealtime.setObjectName("sendOrderRealtime")
        self.sendOrderKStable = QtWidgets.QRadioButton(self.basePolicy)
        self.sendOrderKStable.setGeometry(QtCore.QRect(220, 40, 101, 16))
        self.sendOrderKStable.setObjectName("sendOrderKStable")
        self.actualCheckBox = QtWidgets.QCheckBox(self.basePolicy)
        self.actualCheckBox.setGeometry(QtCore.QRect(120, 90, 71, 16))
        self.actualCheckBox.setObjectName("actualCheckBox")
        self.alarmCheckBox = QtWidgets.QCheckBox(self.basePolicy)
        self.alarmCheckBox.setGeometry(QtCore.QRect(220, 90, 71, 16))
        self.alarmCheckBox.setObjectName("alarmCheckBox")
        self.allowCheckBox = QtWidgets.QCheckBox(self.basePolicy)
        self.allowCheckBox.setGeometry(QtCore.QRect(320, 90, 71, 16))
        self.allowCheckBox.setObjectName("allowCheckBox")
        self.userComboBox = QtWidgets.QComboBox(self.basePolicy)
        self.userComboBox.setGeometry(QtCore.QRect(120, 134, 171, 22))
        self.userComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.userComboBox.setObjectName("userComboBox")
        self.strategyTabWidget.addTab(self.runPolicy, "")
        self.contractPolicy = QtWidgets.QWidget()
        self.contractPolicy.setObjectName("contractPolicy")
        self.contractTableWidget = QtWidgets.QTableWidget(self.contractPolicy)
        self.contractTableWidget.setGeometry(QtCore.QRect(0, 4, 461, 501))
        self.contractTableWidget.setObjectName("contractTableWidget")
        self.contractTableWidget.setColumnCount(5)
        self.contractTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contractTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractTableWidget.setHorizontalHeaderItem(4, item)
        self.contractTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.contractTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.contractTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.contractTableWidget.horizontalHeader().setStretchLastSection(True)
        self.addContract = QtWidgets.QPushButton(self.contractPolicy)
        self.addContract.setGeometry(QtCore.QRect(470, 380, 61, 23))
        self.addContract.setObjectName("addContract")
        self.deleteContract = QtWidgets.QPushButton(self.contractPolicy)
        self.deleteContract.setGeometry(QtCore.QRect(470, 420, 61, 23))
        self.deleteContract.setObjectName("deleteContract")
        self.updateContract = QtWidgets.QPushButton(self.contractPolicy)
        self.updateContract.setGeometry(QtCore.QRect(470, 460, 61, 23))
        self.updateContract.setObjectName("updateContract")
        self.strategyTabWidget.addTab(self.contractPolicy, "")
        self.moneyPolicy = QtWidgets.QWidget()
        self.moneyPolicy.setObjectName("moneyPolicy")
        self.label_6 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 54, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_9.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_10.setGeometry(QtCore.QRect(30, 180, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_11.setGeometry(QtCore.QRect(30, 220, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_12.setGeometry(QtCore.QRect(30, 260, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_13.setGeometry(QtCore.QRect(30, 300, 81, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_14.setGeometry(QtCore.QRect(30, 340, 101, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_15.setGeometry(QtCore.QRect(30, 380, 81, 16))
        self.label_15.setObjectName("label_15")
        self.initFundlineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.initFundlineEdit.setGeometry(QtCore.QRect(140, 15, 151, 20))
        self.initFundlineEdit.setObjectName("initFundlineEdit")
        self.label_16 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_16.setGeometry(QtCore.QRect(300, 20, 54, 12))
        self.label_16.setObjectName("label_16")
        self.tradeDirectionComboBox = QtWidgets.QComboBox(self.moneyPolicy)
        self.tradeDirectionComboBox.setGeometry(QtCore.QRect(139, 54, 171, 22))
        self.tradeDirectionComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tradeDirectionComboBox.setObjectName("tradeDirectionComboBox")
        self.tradeDirectionComboBox.addItem("")
        self.tradeDirectionComboBox.addItem("")
        self.tradeDirectionComboBox.addItem("")
        self.defaultOrderComboBox = QtWidgets.QComboBox(self.moneyPolicy)
        self.defaultOrderComboBox.setGeometry(QtCore.QRect(140, 97, 101, 22))
        self.defaultOrderComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defaultOrderComboBox.setObjectName("defaultOrderComboBox")
        self.defaultOrderComboBox.addItem("")
        self.defaultOrderComboBox.addItem("")
        self.defaultOrderComboBox.addItem("")
        self.defaultOrderLineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.defaultOrderLineEdit.setGeometry(QtCore.QRect(250, 98, 41, 20))
        self.defaultOrderLineEdit.setObjectName("defaultOrderLineEdit")
        self.label_17 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_17.setGeometry(QtCore.QRect(301, 101, 54, 12))
        self.label_17.setObjectName("label_17")
        self.miniOrderLineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.miniOrderLineEdit.setGeometry(QtCore.QRect(140, 138, 91, 20))
        self.miniOrderLineEdit.setObjectName("miniOrderLineEdit")
        self.label_18 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_18.setGeometry(QtCore.QRect(240, 140, 71, 16))
        self.label_18.setObjectName("label_18")
        self.marginRateLineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.marginRateLineEdit.setGeometry(QtCore.QRect(140, 177, 113, 20))
        self.marginRateLineEdit.setObjectName("marginRateLineEdit")
        self.label_19 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_19.setGeometry(QtCore.QRect(260, 181, 54, 12))
        self.label_19.setObjectName("label_19")
        self.openTypeComboBox = QtWidgets.QComboBox(self.moneyPolicy)
        self.openTypeComboBox.setGeometry(QtCore.QRect(140, 218, 131, 22))
        self.openTypeComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.openTypeComboBox.setObjectName("openTypeComboBox")
        self.openTypeComboBox.addItem("")
        self.openTypeComboBox.addItem("")
        self.openFeeRateLineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.openFeeRateLineEdit.setGeometry(QtCore.QRect(140, 258, 113, 20))
        self.openFeeRateLineEdit.setObjectName("openFeeRateLineEdit")
        self.label_20 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_20.setGeometry(QtCore.QRect(260, 262, 54, 12))
        self.label_20.setObjectName("label_20")
        self.closeTypeComboBox = QtWidgets.QComboBox(self.moneyPolicy)
        self.closeTypeComboBox.setGeometry(QtCore.QRect(140, 297, 131, 22))
        self.closeTypeComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.closeTypeComboBox.setObjectName("closeTypeComboBox")
        self.closeTypeComboBox.addItem("")
        self.closeTypeComboBox.addItem("")
        self.closeFeeRateLineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.closeFeeRateLineEdit.setGeometry(QtCore.QRect(140, 338, 113, 20))
        self.closeFeeRateLineEdit.setObjectName("closeFeeRateLineEdit")
        self.label_21 = QtWidgets.QLabel(self.moneyPolicy)
        self.label_21.setGeometry(QtCore.QRect(263, 342, 54, 12))
        self.label_21.setObjectName("label_21")
        self.slippageLineEdit = QtWidgets.QLineEdit(self.moneyPolicy)
        self.slippageLineEdit.setGeometry(QtCore.QRect(140, 379, 113, 20))
        self.slippageLineEdit.setObjectName("slippageLineEdit")
        self.strategyTabWidget.addTab(self.moneyPolicy, "")
        self.samplePolicy = QtWidgets.QWidget()
        self.samplePolicy.setObjectName("samplePolicy")
        self.groupBox = QtWidgets.QGroupBox(self.samplePolicy)
        self.groupBox.setGeometry(QtCore.QRect(7, 10, 521, 231))
        self.groupBox.setObjectName("groupBox")
        self.isConOpenTimesCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.isConOpenTimesCheckBox.setGeometry(QtCore.QRect(30, 40, 151, 16))
        self.isConOpenTimesCheckBox.setObjectName("isConOpenTimesCheckBox")
        self.isConOpenTimesLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.isConOpenTimesLineEdit.setGeometry(QtCore.QRect(192, 37, 61, 20))
        self.isConOpenTimesLineEdit.setObjectName("isConOpenTimesLineEdit")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(267, 40, 54, 12))
        self.label_22.setObjectName("label_22")
        self.openTimesCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.openTimesCheckBox.setGeometry(QtCore.QRect(30, 90, 161, 16))
        self.openTimesCheckBox.setObjectName("openTimesCheckBox")
        self.openTimeslineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.openTimeslineEdit.setGeometry(QtCore.QRect(190, 88, 61, 20))
        self.openTimeslineEdit.setObjectName("openTimeslineEdit")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(265, 91, 54, 12))
        self.label_23.setObjectName("label_23")
        self.canCloseCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.canCloseCheckBox.setGeometry(QtCore.QRect(30, 140, 201, 16))
        self.canCloseCheckBox.setObjectName("canCloseCheckBox")
        self.canOpenCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.canOpenCheckBox.setGeometry(QtCore.QRect(30, 190, 221, 16))
        self.canOpenCheckBox.setObjectName("canOpenCheckBox")
        self.strategyTabWidget.addTab(self.samplePolicy, "")
        self.paramPolicy = QtWidgets.QWidget()
        self.paramPolicy.setObjectName("paramPolicy")
        self.paramsTableWidget = QtWidgets.QTableWidget(self.paramPolicy)
        self.paramsTableWidget.setGeometry(QtCore.QRect(0, 40, 531, 461))
        self.paramsTableWidget.setObjectName("paramsTableWidget")
        self.paramsTableWidget.setColumnCount(4)
        self.paramsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.paramsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.paramsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.paramsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.paramsTableWidget.setHorizontalHeaderItem(3, item)
        self.paramsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.label_24 = QtWidgets.QLabel(self.paramPolicy)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.label_24.setObjectName("label_24")
        self.strategyTabWidget.addTab(self.paramPolicy, "")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(350, 560, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(450, 560, 75, 23))
        self.cancel.setObjectName("cancel")
        strategyMainWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(strategyMainWin)
        self.statusbar.setObjectName("statusbar")
        strategyMainWin.setStatusBar(self.statusbar)

        self.retranslateUi(strategyMainWin)
        self.strategyTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(strategyMainWin)

    def retranslateUi(self, strategyMainWin):
        _translate = QtCore.QCoreApplication.translate
        strategyMainWin.setWindowTitle(_translate("strategyMainWin", "策略属性设置"))
        self.trigger.setTitle(_translate("strategyMainWin", "触发方式"))
        self.KLineCheckBox.setText(_translate("strategyMainWin", "K线触发"))
        self.snapShotCheckBox.setText(_translate("strategyMainWin", "即时行情触发"))
        self.tradeCheckBox.setText(_translate("strategyMainWin", "交易数据触发"))
        self.cycleCheckBox.setText(_translate("strategyMainWin", "每间隔"))
        self.cycleLineEdit.setText(_translate("strategyMainWin", "1000"))
        self.label.setText(_translate("strategyMainWin", "毫秒执行代码（100的整数倍）"))
        self.label_2.setText(_translate("strategyMainWin", "指定时刻"))
        self.timerEdit.setDisplayFormat(_translate("strategyMainWin", "HH:mm:ss"))
        self.addTimerButton.setText(_translate("strategyMainWin", "增加"))
        self.deleteTimerButton.setText(_translate("strategyMainWin", "删除"))
        self.basePolicy.setTitle(_translate("strategyMainWin", "基础设置"))
        self.label_3.setText(_translate("strategyMainWin", "发单时机："))
        self.label_4.setText(_translate("strategyMainWin", "运行模式："))
        self.label_5.setText(_translate("strategyMainWin", "账户："))
        self.sendOrderRealtime.setText(_translate("strategyMainWin", "实时发单"))
        self.sendOrderKStable.setText(_translate("strategyMainWin", "K线稳定后发单"))
        self.actualCheckBox.setText(_translate("strategyMainWin", "实盘运行"))
        self.alarmCheckBox.setText(_translate("strategyMainWin", "发单报警"))
        self.allowCheckBox.setText(_translate("strategyMainWin", "允许弹窗"))
        self.strategyTabWidget.setTabText(self.strategyTabWidget.indexOf(self.runPolicy), _translate("strategyMainWin", "运行设置"))
        item = self.contractTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("strategyMainWin", "合约"))
        item = self.contractTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("strategyMainWin", "K线类型"))
        item = self.contractTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("strategyMainWin", "K线周期"))
        item = self.contractTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("strategyMainWin", "运算起始点"))
        item = self.contractTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("strategyMainWin", "data"))
        self.addContract.setText(_translate("strategyMainWin", "增加"))
        self.deleteContract.setText(_translate("strategyMainWin", "删除"))
        self.updateContract.setText(_translate("strategyMainWin", "修改"))
        self.strategyTabWidget.setTabText(self.strategyTabWidget.indexOf(self.contractPolicy), _translate("strategyMainWin", "合约设置"))
        self.label_6.setText(_translate("strategyMainWin", "初始资金："))
        self.label_7.setText(_translate("strategyMainWin", "交易方向："))
        self.label_8.setText(_translate("strategyMainWin", "默认下单量："))
        self.label_9.setText(_translate("strategyMainWin", "最小下单量："))
        self.label_10.setText(_translate("strategyMainWin", "保证金率："))
        self.label_11.setText(_translate("strategyMainWin", "开仓收费方式："))
        self.label_12.setText(_translate("strategyMainWin", "开仓手续费(率)："))
        self.label_13.setText(_translate("strategyMainWin", "平仓收费方式："))
        self.label_14.setText(_translate("strategyMainWin", "平仓手续费(率)："))
        self.label_15.setText(_translate("strategyMainWin", "滑点损耗："))
        self.initFundlineEdit.setText(_translate("strategyMainWin", "1000000"))
        self.label_16.setText(_translate("strategyMainWin", "元"))
        self.tradeDirectionComboBox.setItemText(0, _translate("strategyMainWin", "双向交易"))
        self.tradeDirectionComboBox.setItemText(1, _translate("strategyMainWin", "仅多头"))
        self.tradeDirectionComboBox.setItemText(2, _translate("strategyMainWin", "仅空头"))
        self.defaultOrderComboBox.setItemText(0, _translate("strategyMainWin", "按固定合约数"))
        self.defaultOrderComboBox.setItemText(1, _translate("strategyMainWin", "按资金比例"))
        self.defaultOrderComboBox.setItemText(2, _translate("strategyMainWin", "按固定资金"))
        self.defaultOrderLineEdit.setText(_translate("strategyMainWin", "1"))
        self.label_17.setText(_translate("strategyMainWin", "手"))
        self.miniOrderLineEdit.setText(_translate("strategyMainWin", "1"))
        self.label_18.setText(_translate("strategyMainWin", "手(1-1000)"))
        self.marginRateLineEdit.setText(_translate("strategyMainWin", "8"))
        self.label_19.setText(_translate("strategyMainWin", "%"))
        self.openTypeComboBox.setItemText(0, _translate("strategyMainWin", "固定值"))
        self.openTypeComboBox.setItemText(1, _translate("strategyMainWin", "比例"))
        self.openFeeRateLineEdit.setText(_translate("strategyMainWin", "1"))
        self.label_20.setText(_translate("strategyMainWin", "%"))
        self.closeTypeComboBox.setItemText(0, _translate("strategyMainWin", "固定值"))
        self.closeTypeComboBox.setItemText(1, _translate("strategyMainWin", "比例"))
        self.closeFeeRateLineEdit.setText(_translate("strategyMainWin", "1"))
        self.label_21.setText(_translate("strategyMainWin", "%"))
        self.slippageLineEdit.setText(_translate("strategyMainWin", "0"))
        self.strategyTabWidget.setTabText(self.strategyTabWidget.indexOf(self.moneyPolicy), _translate("strategyMainWin", "资金设置"))
        self.groupBox.setTitle(_translate("strategyMainWin", "发单设置"))
        self.isConOpenTimesCheckBox.setText(_translate("strategyMainWin", "最大连续同向开仓次数："))
        self.isConOpenTimesLineEdit.setText(_translate("strategyMainWin", "1"))
        self.label_22.setText(_translate("strategyMainWin", "次(1-100)"))
        self.openTimesCheckBox.setText(_translate("strategyMainWin", "每根K线同向开仓次数："))
        self.openTimeslineEdit.setText(_translate("strategyMainWin", "1"))
        self.label_23.setText(_translate("strategyMainWin", "次(1-100)"))
        self.canCloseCheckBox.setText(_translate("strategyMainWin", "开仓的当前K线不允许反向下单"))
        self.canOpenCheckBox.setText(_translate("strategyMainWin", "平仓的当前K线不允许开仓"))
        self.strategyTabWidget.setTabText(self.strategyTabWidget.indexOf(self.samplePolicy), _translate("strategyMainWin", "样本设置"))
        item = self.paramsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("strategyMainWin", "参数"))
        item = self.paramsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("strategyMainWin", "当前值"))
        item = self.paramsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("strategyMainWin", "类型"))
        item = self.paramsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("strategyMainWin", "描述"))
        self.label_24.setText(_translate("strategyMainWin", "鼠标单击\"当前值\"进行参数修改："))
        self.strategyTabWidget.setTabText(self.strategyTabWidget.indexOf(self.paramPolicy), _translate("strategyMainWin", "参数设置"))
        self.confirm.setText(_translate("strategyMainWin", "确定"))
        self.cancel.setText(_translate("strategyMainWin", "取消"))
