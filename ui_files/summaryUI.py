# Form implementation generated from reading ui file '.\summary.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 531)
        MainWindow.setMinimumSize(QtCore.QSize(913, 0))
        MainWindow.setMaximumSize(QtCore.QSize(913, 99999))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 30, 911, 61))
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
        self.label.setGeometry(QtCore.QRect(-6, 90, 921, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 170, 201, 16))
        self.label_6.setObjectName("label_6")
        self.tokenAddress = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tokenAddress.setGeometry(QtCore.QRect(50, 190, 401, 22))
        self.tokenAddress.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNoEditMenu)
        self.tokenAddress.setText("")
        self.tokenAddress.setReadOnly(True)
        self.tokenAddress.setObjectName("tokenAddress")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 170, 201, 16))
        self.label_7.setObjectName("label_7")
        self.mintTransaction = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.mintTransaction.setGeometry(QtCore.QRect(50, 250, 401, 22))
        self.mintTransaction.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNoEditMenu)
        self.mintTransaction.setText("")
        self.mintTransaction.setReadOnly(True)
        self.mintTransaction.setObjectName("mintTransaction")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 230, 201, 16))
        self.label_8.setObjectName("label_8")
        self.metadataTransaction = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.metadataTransaction.setGeometry(QtCore.QRect(460, 250, 401, 22))
        self.metadataTransaction.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNoEditMenu)
        self.metadataTransaction.setText("")
        self.metadataTransaction.setReadOnly(True)
        self.metadataTransaction.setObjectName("metadataTransaction")
        self.tokenAccountAddress = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tokenAccountAddress.setGeometry(QtCore.QRect(460, 190, 401, 22))
        self.tokenAccountAddress.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNoEditMenu)
        self.tokenAccountAddress.setText("")
        self.tokenAccountAddress.setReadOnly(True)
        self.tokenAccountAddress.setClearButtonEnabled(False)
        self.tokenAccountAddress.setObjectName("tokenAccountAddress")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 230, 201, 16))
        self.label_11.setObjectName("label_11")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(300, 450, 331, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.processText = QtWidgets.QLabel(parent=self.centralwidget)
        self.processText.setGeometry(QtCore.QRect(304, 480, 321, 20))
        self.processText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.processText.setObjectName("processText")
        self.transferTransaction = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.transferTransaction.setGeometry(QtCore.QRect(260, 300, 401, 22))
        self.transferTransaction.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNoEditMenu)
        self.transferTransaction.setText("")
        self.transferTransaction.setReadOnly(True)
        self.transferTransaction.setObjectName("transferTransaction")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 280, 201, 16))
        self.label_12.setObjectName("label_12")
        self.revokeMintField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.revokeMintField.setEnabled(True)
        self.revokeMintField.setGeometry(QtCore.QRect(50, 350, 401, 22))
        self.revokeMintField.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.revokeMintField.setText("")
        self.revokeMintField.setReadOnly(True)
        self.revokeMintField.setObjectName("revokeMintField")
        self.revokeMintTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.revokeMintTitle.setEnabled(True)
        self.revokeMintTitle.setGeometry(QtCore.QRect(50, 330, 201, 16))
        self.revokeMintTitle.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.revokeMintTitle.setObjectName("revokeMintTitle")
        self.revokeFreezeField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.revokeFreezeField.setEnabled(True)
        self.revokeFreezeField.setGeometry(QtCore.QRect(460, 350, 401, 22))
        self.revokeFreezeField.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.revokeFreezeField.setText("")
        self.revokeFreezeField.setReadOnly(True)
        self.revokeFreezeField.setObjectName("revokeFreezeField")
        self.revokeFreezeTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.revokeFreezeTitle.setEnabled(True)
        self.revokeFreezeTitle.setGeometry(QtCore.QRect(460, 330, 231, 16))
        self.revokeFreezeTitle.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.revokeFreezeTitle.setObjectName("revokeFreezeTitle")
        self.donateTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.donateTitle.setEnabled(True)
        self.donateTitle.setGeometry(QtCore.QRect(270, 390, 231, 16))
        self.donateTitle.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.donateTitle.setObjectName("donateTitle")
        self.donateField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.donateField.setEnabled(True)
        self.donateField.setGeometry(QtCore.QRect(270, 410, 401, 22))
        self.donateField.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.donateField.setText("")
        self.donateField.setReadOnly(True)
        self.donateField.setObjectName("donateField")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tokenAddress, self.mintTransaction)
        MainWindow.setTabOrder(self.mintTransaction, self.metadataTransaction)
        MainWindow.setTabOrder(self.metadataTransaction, self.tokenAccountAddress)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solana Token Creator (STC) - Summary"))
        self.title.setText(_translate("MainWindow", "Solana Token Creator"))
        self.label.setText(_translate("MainWindow", "Summary"))
        self.label_6.setText(_translate("MainWindow", "Token address"))
        self.tokenAddress.setPlaceholderText(_translate("MainWindow", "Processing..."))
        self.label_7.setText(_translate("MainWindow", "Token account address"))
        self.mintTransaction.setPlaceholderText(_translate("MainWindow", "Pending..."))
        self.label_8.setText(_translate("MainWindow", "Mint transaction"))
        self.metadataTransaction.setPlaceholderText(_translate("MainWindow", "Pending..."))
        self.tokenAccountAddress.setPlaceholderText(_translate("MainWindow", "Pending..."))
        self.label_11.setText(_translate("MainWindow", "Metadata transaction"))
        self.processText.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffaa00;\">Processing...</span></p></body></html>"))
        self.transferTransaction.setPlaceholderText(_translate("MainWindow", "Pending..."))
        self.label_12.setText(_translate("MainWindow", "Transfer transaction"))
        self.revokeMintField.setPlaceholderText(_translate("MainWindow", "Pending..."))
        self.revokeMintTitle.setText(_translate("MainWindow", "Revoke mint authority transaction"))
        self.revokeFreezeField.setPlaceholderText(_translate("MainWindow", "Pending..."))
        self.revokeFreezeTitle.setText(_translate("MainWindow", "Revoke freeze authority transaction"))
        self.donateTitle.setText(_translate("MainWindow", "Donate transaction"))
        self.donateField.setPlaceholderText(_translate("MainWindow", "Pending..."))
