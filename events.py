from solders.keypair import Keypair
import base58
import json
from mnemonic import Mnemonic
import globalvar
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QCoreApplication
from ui_files import backupUI, mainUI, summaryUI
from solanacli import get_balance, required_balance, create_mint, create_account, mint_tokens, transfer_tokens, metadata_transaction
from time import sleep

def createWallet(self, window):
    mnemo = Mnemonic("english")
    mnemo_generated = mnemo.generate(128)
    print(mnemo_generated)
    kp = Keypair().from_seed(bytes(mnemo.to_seed(mnemo_generated))[:32])
    kp_pubkey = kp.pubkey()
    pubkey_encoded = bytes(kp_pubkey)
    kp_encoded = kp.secret()+pubkey_encoded
    kp_privkey = base58.b58encode(kp_encoded).decode()
    with open("./credentials.json", "w") as f:
        data = {
            "pubkey": str(kp_pubkey),
            "privkey": str(kp_privkey)
        }
        f.write(json.dumps(data))
        globalvar.credentials = data
    self.createAddressButton.setEnabled(False)
    self.window = QMainWindow()
    backupUI_var = backupUI.Ui_MainWindow()
    backupUI_var.setupUi(self.window)
    backupUI_var.backupField.setText(str(mnemo_generated))
    backupUI_var.continueButton.pressed.connect(lambda: continue_create(window, self.window))
    self.window.show()

def continue_create(mainUI_var, backup_window: QMainWindow):
    mui = mainUI.Ui_MainWindow()
    mui.setupUi(mainUI_var)
    mui.walletAddress.setText(globalvar.credentials["pubkey"])
    mui.reloadWalletButton.pressed.connect(lambda: reload_wallet(globalvar.credentials["pubkey"], mui))
    mui.createTokenButton.pressed.connect(lambda: create_token(mui))
    mainUI_var.show()
    backup_window.close()
    reload_wallet(globalvar.credentials["pubkey"], mui)
    
def reload_wallet(pubkey, mui: mainUI.Ui_MainWindow):
    mui.reloadWalletButton.setText("Please wait...")
    mui.reloadWalletButton.setEnabled(False)
    mui.balanceText.setText("- SOL")
    mui.reqBalText.setText("- SOL")
    QCoreApplication.processEvents()
    bal = get_balance(pubkey)
    if bal == None:
        mui.balanceText.setText("Error!")
    else:
        mui.balanceText.setText(str(bal) + " SOL")
    QCoreApplication.processEvents()
    req_bal = required_balance()
    if bal == None:
        mui.reqBalText.setText("Error!")
    else:
        mui.reqBalText.setText('<html><head/><body><p><span style="color:#ff0000;">' + str(req_bal) + " SOL</span></p></body></html")
    mui.reloadWalletButton.setEnabled(True)
    mui.reloadWalletButton.setText("Reload Wallet")  

def create_token(mui: mainUI.Ui_MainWindow):
    mui.window = QMainWindow()
    sumUI = summaryUI.Ui_MainWindow()
    sumUI.setupUi(mui.window)
    mui.window.show()
    mui.createTokenButton.setText("Processing...")
    mui.createTokenButton.setEnabled(False)
    QCoreApplication.processEvents()
    privkey = globalvar.credentials["privkey"]
    pubkey = globalvar.credentials["pubkey"]
    pubkey_receiver = mui.personalAddress.text()
    amount = mui.amountBox.value()
    tokenname = mui.tokenName.text()
    tokenticker = mui.tokenTicker.text()
    jsonurl = mui.metadataURL.text()
    mint = create_mint(pubkey, privkey)
    if mint == None:
        print("Mint error!")
        sumUI.tokenAddress.setPlaceholderText("Failed!")
        sumUI.progressBar.setValue(100)
        sumUI.processText.setText('<html><head/><body><p><span style=" font-weight:600; color:#ff0000;">Failed!</span></p></body></html>')
        mui.createTokenButton.setText("Create Token!")
        mui.createTokenButton.setEnabled(True)
        return
    print("Mint created! (" + str(mint.pubkey) + ")")
    sumUI.tokenAddress.setText(str(mint.pubkey))
    sumUI.tokenAccountAddress.setPlaceholderText("Processing...")
    sumUI.progressBar.setValue(20)
    QCoreApplication.processEvents()
    account = create_account(mint, pubkey)
    if account == None:
        print("Account error!")
        sumUI.tokenAccountAddress.setPlaceholderText("Failed!")
        sumUI.progressBar.setValue(100)
        sumUI.processText.setText('<html><head/><body><p><span style=" font-weight:600; color:#ff0000;">Failed!</span></p></body></html>')
        mui.createTokenButton.setText("Create Token!")
        mui.createTokenButton.setEnabled(True)
        return
    print("Account created! (" + str(account) + ")")
    sumUI.tokenAccountAddress.setText(str(account))
    sumUI.progressBar.setValue(40)
    sumUI.mintTransaction.setPlaceholderText("Processing...")
    QCoreApplication.processEvents()
    minted = mint_tokens(mint, account, pubkey, int(amount))
    if minted == None:
        print("Minting error!")
        sumUI.mintTransaction.setPlaceholderText("Failed!")
        sumUI.progressBar.setValue(100)
        sumUI.processText.setText('<html><head/><body><p><span style=" font-weight:600; color:#ff0000;">Failed!</span></p></body></html>')
        mui.createTokenButton.setText("Create Token!")
        mui.createTokenButton.setEnabled(True)
        return
    print("Tokens minted! (" + str(minted.value) + ")")
    sumUI.mintTransaction.setText(str(minted.value))
    sumUI.progressBar.setValue(60)
    sumUI.metadataTransaction.setPlaceholderText("Processing...")
    QCoreApplication.processEvents()
    metadata = metadata_transaction(tokenname, tokenticker, jsonurl, mint, pubkey, privkey)
    if metadata == None:
        print("Metadata error!")
        sumUI.metadataTransaction.setPlaceholderText("Failed!")
        sumUI.progressBar.setValue(100)
        sumUI.processText.setText('<html><head/><body><p><span style=" font-weight:600; color:#ff0000;">Failed!</span></p></body></html>')
        mui.createTokenButton.setText("Create Token!")
        mui.createTokenButton.setEnabled(True)
        return
    print("Metadata updated! (" + str(metadata.value) + ")")
    sumUI.metadataTransaction.setText(str(metadata.value))
    sumUI.progressBar.setValue(80)
    sumUI.transferTransaction.setPlaceholderText("Processing...")
    transfer = transfer_tokens(mint, pubkey, pubkey_receiver, account, int(amount))
    if transfer == None:
        print("Transfer error!")
        sumUI.transferTransaction.setPlaceholderText("Failed!")
        sumUI.progressBar.setValue(100)
        sumUI.processText.setText('<html><head/><body><p><span style=" font-weight:600; color:#ff0000;">Failed!</span></p></body></html>')
        mui.createTokenButton.setText("Create Token!")
        mui.createTokenButton.setEnabled(True)
        return
    print("Tokens transfered! (" + str(transfer.value) + ")")
    sumUI.transferTransaction.setText(str(transfer.value))
    sumUI.progressBar.setValue(100)
    sumUI.processText.setText('<html><head/><body><p><span style=" font-weight:600; color:#00ff00;">Done!</span></p></body></html>')
    mui.createTokenButton.setText("Create Token!")
    mui.createTokenButton.setEnabled(True)
    

