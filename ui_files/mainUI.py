# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 636)
        MainWindow.setMinimumSize(QtCore.QSize(850, 636))
        MainWindow.setMaximumSize(QtCore.QSize(850, 636))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 30, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(264, 90, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.walletAddress = QtWidgets.QLabel(parent=self.centralwidget)
        self.walletAddress.setGeometry(QtCore.QRect(0, 180, 851, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.walletAddress.setFont(font)
        self.walletAddress.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.walletAddress.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.walletAddress.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.walletAddress.setObjectName("walletAddress")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.balanceText = QtWidgets.QLabel(parent=self.centralwidget)
        self.balanceText.setGeometry(QtCore.QRect(430, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.balanceText.setFont(font)
        self.balanceText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.balanceText.setObjectName("balanceText")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 201, 16))
        self.label_6.setObjectName("label_6")
        self.personalAddress = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.personalAddress.setGeometry(QtCore.QRect(30, 350, 401, 22))
        self.personalAddress.setText("")
        self.personalAddress.setObjectName("personalAddress")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 380, 201, 16))
        self.label_7.setObjectName("label_7")
        self.tokenName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tokenName.setGeometry(QtCore.QRect(30, 400, 401, 22))
        self.tokenName.setText("")
        self.tokenName.setObjectName("tokenName")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 430, 201, 16))
        self.label_8.setObjectName("label_8")
        self.tokenTicker = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tokenTicker.setGeometry(QtCore.QRect(30, 450, 401, 22))
        self.tokenTicker.setText("")
        self.tokenTicker.setObjectName("tokenTicker")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 230, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.reqBalText = QtWidgets.QLabel(parent=self.centralwidget)
        self.reqBalText.setGeometry(QtCore.QRect(430, 230, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.reqBalText.setFont(font)
        self.reqBalText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.reqBalText.setObjectName("reqBalText")
        self.metadataURL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.metadataURL.setGeometry(QtCore.QRect(30, 500, 401, 22))
        self.metadataURL.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.metadataURL.setText("")
        self.metadataURL.setReadOnly(False)
        self.metadataURL.setClearButtonEnabled(False)
        self.metadataURL.setObjectName("metadataURL")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 480, 201, 16))
        self.label_11.setObjectName("label_11")
        self.createTokenButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createTokenButton.setGeometry(QtCore.QRect(30, 550, 141, 41))
        self.createTokenButton.setObjectName("createTokenButton")
        self.reloadWalletButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reloadWalletButton.setGeometry(QtCore.QRect(180, 550, 141, 41))
        self.reloadWalletButton.setObjectName("reloadWalletButton")
        self.amountBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.amountBox.setGeometry(QtCore.QRect(470, 350, 341, 22))
        self.amountBox.setDecimals(9)
        self.amountBox.setMaximum(1000000000000000.0)
        self.amountBox.setObjectName("amountBox")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 330, 201, 16))
        self.label_10.setObjectName("label_10")
        self.decimalPlacesBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.decimalPlacesBox.setGeometry(QtCore.QRect(470, 400, 41, 22))
        self.decimalPlacesBox.setDecimals(0)
        self.decimalPlacesBox.setMaximum(9.0)
        self.decimalPlacesBox.setObjectName("decimalPlacesBox")
        self.decimalPlacesText = QtWidgets.QLabel(parent=self.centralwidget)
        self.decimalPlacesText.setGeometry(QtCore.QRect(470, 380, 201, 16))
        self.decimalPlacesText.setObjectName("decimalPlacesText")
        self.tokenDescriptionTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.tokenDescriptionTitle.setGeometry(QtCore.QRect(470, 430, 201, 16))
        self.tokenDescriptionTitle.setObjectName("tokenDescriptionTitle")
        self.revokeMintCheckbox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.revokeMintCheckbox.setGeometry(QtCore.QRect(470, 450, 301, 20))
        self.revokeMintCheckbox.setObjectName("revokeMintCheckbox")
        self.revokeFreezeCheckbox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.revokeFreezeCheckbox.setGeometry(QtCore.QRect(470, 480, 301, 20))
        self.revokeFreezeCheckbox.setObjectName("revokeFreezeCheckbox")
        self.changeOwnerCheckbox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.changeOwnerCheckbox.setGeometry(QtCore.QRect(470, 510, 301, 20))
        self.changeOwnerCheckbox.setObjectName("changeOwnerCheckbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.personalAddress, self.tokenName)
        MainWindow.setTabOrder(self.tokenName, self.tokenTicker)
        MainWindow.setTabOrder(self.tokenTicker, self.metadataURL)
        MainWindow.setTabOrder(self.metadataURL, self.createTokenButton)
        MainWindow.setTabOrder(self.createTokenButton, self.reloadWalletButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solana Token Creator (STC)"))
        self.title.setText(_translate("MainWindow", "Solana Token Creator"))
        self.label.setText(_translate("MainWindow", "Made by Ufinator"))
        self.label_2.setText(_translate("MainWindow", "Solana Wallet Address:"))
        self.walletAddress.setText(_translate("MainWindow", "ATPX7nxu3rqHumwGT9fJoG1AtCD42dvmiByx8uiaXfVo"))
        self.label_4.setText(_translate("MainWindow", "Available Solana:"))
        self.balanceText.setText(_translate("MainWindow", "- SOL"))
        self.label_6.setText(_translate("MainWindow", "Your Solana Wallet Address:"))
        self.personalAddress.setPlaceholderText(_translate("MainWindow", "(Your wallet address, where the tokens should be transfered to)"))
        self.label_7.setText(_translate("MainWindow", "New token name"))
        self.tokenName.setPlaceholderText(_translate("MainWindow", "(e.x. Solana)"))
        self.label_8.setText(_translate("MainWindow", "New token ticker:"))
        self.tokenTicker.setPlaceholderText(_translate("MainWindow", "(e.x. SOL)"))
        self.label_9.setText(_translate("MainWindow", "Needed amount:"))
        self.reqBalText.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">- SOL</span></p></body></html>"))
        self.metadataURL.setPlaceholderText(_translate("MainWindow", "(URL to metadata JSON)"))
        self.label_11.setText(_translate("MainWindow", "Metadata URL (JSON File):"))
        self.createTokenButton.setText(_translate("MainWindow", "Create Token!"))
        self.reloadWalletButton.setText(_translate("MainWindow", "Reload Wallet"))
        self.label_10.setText(_translate("MainWindow", "Amount:"))
        self.decimalPlacesText.setText(_translate("MainWindow", "Decimal places:"))
        self.tokenDescriptionTitle.setText(_translate("MainWindow", "Additional options"))
        self.revokeMintCheckbox.setText(_translate("MainWindow", "Revoke mint authorization"))
        self.revokeFreezeCheckbox.setText(_translate("MainWindow", "Revoke freeze authorization"))
        self.changeOwnerCheckbox.setText(_translate("MainWindow", "Change owner of the tokens to your wallet"))
