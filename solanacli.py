import solana.rpc
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from spl.token.client import Token as spl
from solders.keypair import Keypair
from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction as txt
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import AuthorityType
from solana.transaction import Transaction
from os import getenv
import solana.exceptions
import solana.rpc.core

from borsh_construct import CStruct, U8, String, Option, Vec, Bool, Enum, U64, U16
from construct import Bytes
from solders.instruction import AccountMeta, Instruction

def get_balance(pubkey):
    client = Client(getenv("RPC_URL"))
    if not client.is_connected():
        return None
    pubkey = Pubkey.from_string(pubkey)
    account_balance = client.get_balance(pubkey)
    return account_balance.value / 1000000000

# Fix this
def required_balance():
    return 0

def create_mint(pubkey: str, privkey: str):
    client = Client(getenv("RPC_URL"))
    while not client.is_connected():
        client = Client(getenv("RPC_URL"))
    print("Client connected! Creating mint")
    pubkey = Pubkey.from_string(pubkey)
    privkey = Keypair.from_base58_string(privkey)
    Token = spl(client, pubkey, TOKEN_PROGRAM_ID, privkey)
    val = Token.create_mint(client, privkey, pubkey, 9, TOKEN_PROGRAM_ID, pubkey)
    return val

def create_account(mint: spl, pubkey: str):
    pubkey = Pubkey.from_string(pubkey)
    val = mint.create_associated_token_account(owner=pubkey)
    return val

def mint_tokens(mint: spl, account: spl, pubkey: str, amount: int):
    pubkey = Pubkey.from_string(pubkey)
    amount = amount * 1000000000
    val = mint.mint_to(account, pubkey, amount)
    return val

def revokeMint(mint: spl, privkey: str):
    privkey = Keypair.from_base58_string(privkey)
    val = mint.set_authority(mint.pubkey, privkey, AuthorityType.MINT_TOKENS)
    print("Revoked mint authority! (" + str(val.value) + ")")
    return val

def revokeFreeze(mint: spl, privkey: str):
    privkey = Keypair.from_base58_string(privkey)
    val = mint.set_authority(mint.pubkey, privkey, AuthorityType.FREEZE_ACCOUNT)
    print("Revoked freeze authority! (" + str(val.value) + ")")
    return val

def transfer_tokens(mint: spl, pubkey_owner: str, pubkey_receiver: str, account: spl, amount: int):
    pubkey_owner = Pubkey.from_string(pubkey_owner)
    pubkey_receiver = Pubkey.from_string(pubkey_receiver)
    amount = amount * 1000000000
    val = None
    receiver = None
    while val == None:
        try:
            if receiver == None:
                receiver = mint.create_associated_token_account(pubkey_receiver)
            val = mint.transfer(account, receiver, pubkey_owner, amount)
            return val
        except solana.exceptions.SolanaRpcException:
            print("Transfer error!")

def metadata_transaction(tokenname: str, tokenticker: str, jsonurl: str, mint: spl, pubkey: str, privkey: str):
    client = Client(getenv("RPC_URL"))
    while not client.is_connected():
        client = Client(getenv("RPC_URL"))
    print("Client connected!")
    pubkey = Pubkey.from_string(pubkey)
    kp = Keypair.from_base58_string(privkey)
    metadata_pubkey = Pubkey.from_string("metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s")
    instruction_structure = CStruct(
        "instructionDiscriminator" / U8,
        "createMetadataAccountArgsV3" / CStruct(
            "data" / CStruct(
                "name" / String,
                "symbol" / String,
                "uri" / String,
                "sellerFeeBasisPoints" / U16,
                "creators" / Option(Vec(CStruct(
                    "address" / Bytes(32),
                    "verified" / Bool,
                    "share" / U8
                ))),
                "collection" / Option(CStruct(
                    "verified" / Bool,
                    "key" / String
                )),
                "uses" / Option(CStruct(
                    "useMethod" / Enum(
                        "Burn",
                        "Multiple",
                        "Single",
                        enum_name="UseMethod"
                    ),
                    "remaining" / U64,
                    "total" / U64
                ))
            ),
            "isMutable" / Bool,
            "collectionDetails" / Option(String)
        )
    )
    # data for the instruction
    instruction_data = {
        "instructionDiscriminator": 33,
        "createMetadataAccountArgsV3": {
            "data": {
                "name": tokenname,
                "symbol": tokenticker,
                "uri": jsonurl,
                "sellerFeeBasisPoints": 0,
                "creators": [
                    {
                        "address": bytes(pubkey),
                        "verified": 1,
                        "share": 100
                    }
                ],
                "collection": None,
                "uses": None
            },
            "isMutable": 1,
            "collectionDetails": None
        }
    }
    # get pda of mint account
    metadata_pda = Pubkey.find_program_address([b"metadata", bytes(metadata_pubkey), bytes(mint.pubkey)], metadata_pubkey)[0]

    # account list for instruction
    accounts = [
        AccountMeta(pubkey=metadata_pda, is_signer=False, is_writable=True), # metadata
        AccountMeta(pubkey=mint.pubkey, is_signer=False, is_writable=False), # mint
        AccountMeta(pubkey=pubkey, is_signer=True, is_writable=False), # mint authority
        AccountMeta(pubkey=pubkey, is_signer=True, is_writable=True), # payer
        AccountMeta(pubkey=pubkey, is_signer=False, is_writable=False), # update authority
        AccountMeta(pubkey=Pubkey.from_string('11111111111111111111111111111111'), is_signer=False, is_writable=False), # system program
        AccountMeta(pubkey=Pubkey.from_string('SysvarRent111111111111111111111111111111111'), is_signer=False, is_writable=False) # rent
    ]

    # create instruction
    try:
        tx = Transaction()
        tx.add(Instruction(metadata_pubkey, instruction_structure.build(instruction_data), accounts))
        blockhash = client.get_latest_blockhash()
        tx.recent_blockhash = blockhash.value.blockhash
        tx.sign(kp)
        val = client.send_raw_transaction(tx.serialize())
        return val
    except solana.exceptions.SolanaRpcException:
        return None

def donateSolana(privkey: str, amount: float):
    privkey: Keypair = Keypair.from_base58_string(privkey)
    pubkey = Pubkey.from_string(getenv("DONATE_PUBKEY"))
    client = Client(getenv("RPC_URL"))
    while not client.is_connected():
        client = Client(getenv("RPC_URL"))
    print("Client connected!")
    tx = [transfer(TransferParams(
        from_pubkey=privkey.pubkey(), to_pubkey=pubkey, lamports=int(amount * 1000000000)
    ))]
    val = client.send_legacy_transaction(txt(instructions=tx), privkey)
    return val