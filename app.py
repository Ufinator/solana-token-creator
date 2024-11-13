import json
import base58
from solana.rpc.api import Client
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from dotenv import load_dotenv
from os import getenv
from time import sleep

load_dotenv()

pubkey = None
privkey = None
sol_cli = None
mint: Token = None

def init():
    global pubkey, privkey
    with open("./credentials.json", "r") as f:
        loaded_json = json.load(f)
        pubkey = Pubkey.from_string(loaded_json["pubkey"])
        privkey = Keypair.from_base58_string(loaded_json["privkey"])
    connect_client()
    return

def connect_client():
    load_dotenv()
    global sol_cli
    sol_cli = Client("https://api.mainnet-beta.solana.com")
    while not sol_cli.is_connected():
        sleep(5)
        sol_cli = Client(getenv("RPC"))
    print("Connected to Solana RPC! " + getenv("RPC"))
    create_token()
    return

def create_token():
    global sol_cli, pubkey, privkey, mint
    tk = Token(sol_cli, pubkey, TOKEN_PROGRAM_ID, privkey)
    mint = tk.create_mint(sol_cli, privkey, pubkey, 9, TOKEN_PROGRAM_ID)
    print("Created mint: " + str(mint.pubkey))
    create_account()
    return

def create_account():
    global mint, pubkey, privkey
    accocunt = mint.create_account(pubkey)
    print("Account: " + str(accocunt))
    val = mint.mint_to(accocunt, privkey, 66666 * 1000000000)
    print("TxID: " + str(val.value))

if __name__ == "__main__":
    init()
    