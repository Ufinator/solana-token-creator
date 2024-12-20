from ui_files import mainUI, startUI
from PyQt6.QtWidgets import QApplication, QMainWindow
from dotenv import load_dotenv
from events import reload_wallet, create_token, createWallet, toggle_donate
import globalvar
import json

load_dotenv("./.env", override=True)

def main():
    init()
    mui = mainUI.Ui_MainWindow()
    sui = startUI.Ui_MainWindow()
    app = QApplication([])
    window = QMainWindow()
    if globalvar.credentials != None:
        mui.setupUi(window)
        mui.walletAddress.setText(globalvar.credentials["pubkey"])
        mui.reloadWalletButton.pressed.connect(lambda: reload_wallet(globalvar.credentials["pubkey"], mui))
        mui.createTokenButton.pressed.connect(lambda: create_token(mui))
        mui.donateSolanaCheckbox.stateChanged.connect(lambda: toggle_donate(mui))
        toggle_donate(mui)
        reload_wallet(globalvar.credentials["pubkey"], mui)
    else:
        sui.setupUi(window)
        sui.createAddressButton.pressed.connect(lambda: createWallet(sui, window))
    window.show()
    app.exec()

# Load credentials, Fix this with f.write()
def init():
    try:
        with open("./credentials.json", "r") as f:
            try:
                jf = json.load(f)
                globalvar.credentials = jf
                return
            except json.decoder.JSONDecodeError:
                with open("./credentials.json", "w") as f:
                    # f.write("{}")
                    return 0
    except FileNotFoundError or TypeError:
        with open("./credentials.json", "w") as f:
            # f.write("{}")
            return 0

if __name__ == "__main__":
    main()