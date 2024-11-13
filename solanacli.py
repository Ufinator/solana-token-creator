import solana.rpc
from solana.rpc.api import Client
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
from spl.token.client import Token as spl
from spl.token.async_client import AsyncToken
from solders.keypair import Keypair
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import Transaction
from spl.token.instructions import initialize_mint, InitializeMintParams
from solana.rpc.commitment import Confirmed
from solana.rpc.types import TxOpts
from os import getenv
import solana.exceptions
import solana.rpc.core

from borsh_construct import CStruct, U8, String, Option, Vec, Bool, Enum, U64, U16
from construct import Bytes
from solders.instruction import AccountMeta, Instruction

async def get_balance(pubkey):
    client = AsyncClient(getenv("RPC"))
    if not await client.is_connected():
        return None
    pubkey = Pubkey.from_string(pubkey)
    account_balance = await client.get_balance(pubkey)
    return account_balance.value / 1000000000

async def required_balance():
    client = AsyncClient(getenv("RPC"))
    if not await client.is_connected():
        return None
    mint_bal = await AsyncToken.get_min_balance_rent_for_exempt_for_mint(client)
    account_bal = await AsyncToken.get_min_balance_rent_for_exempt_for_account(client)
    multisig_bal = await AsyncToken.get_min_balance_rent_for_exempt_for_multisig(client)
    req_bal = (mint_bal + account_bal + multisig_bal) / 1000000000
    return req_bal

async def create_mint(pubkey: str, privkey: str):
    client = AsyncClient(getenv("RPC"))
    if not await client.is_connected():
        return None
    pubkey = Pubkey.from_string(pubkey)
    privkey = Keypair.from_base58_string(privkey)
    tx = Transaction()
    mint_pub = Keypair().pubkey()
    params = InitializeMintParams(
        decimals=6,
        freeze_authority=pubkey,
        mint=mint_pub,
        mint_authority=pubkey,
        program_id=TOKEN_PROGRAM_ID,
    )
    tx.add(initialize_mint(params))
    tx.sign(privkey)
    val = await client.send_transaction(tx, privkey, TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))
    # val = await AsyncToken.create_mint(client, privkey, pubkey, 9, TOKEN_PROGRAM_ID, pubkey)
    print(val.value)
    return mint_pub

def create_minter(pubkey: str, privkey: str):
    client = Client(getenv("RPC"))
    if not client.is_connected():
        return None
    val = None
    pubkey = Pubkey.from_string(pubkey)
    privkey = Keypair.from_base58_string(privkey)
    blockhash = client.get_latest_blockhash().value.blockhash
    val = spl.create_mint(client, privkey, pubkey, 9, TOKEN_PROGRAM_ID, pubkey, recent_blockhash=blockhash)
    return val

async def create_account(mint: spl, pubkey: str):
    val = None
    pubkey = Pubkey.from_string(pubkey)
    val = await mint.create_associated_token_account(owner=pubkey)
    return val

async def mint_tokens(mint: spl, account: spl, pubkey: str, amount: int):
    pubkey = Pubkey.from_string(pubkey)
    amount = amount * 1000000000
    val = None
    while val == None:
        try:
            val = await mint.mint_to(account, pubkey, amount)
            return val
        except solana.exceptions.SolanaRpcException:
            print("Mint error!")

async def transfer_tokens(mint: spl, pubkey_owner: str, pubkey_receiver: str, account: spl, amount: int):
    pubkey_owner = Pubkey.from_string(pubkey_owner)
    pubkey_receiver = Pubkey.from_string(pubkey_receiver)
    amount = amount * 1000000000
    val = None
    receiver = None
    while val == None:
        try:
            if receiver == None:
                receiver = await mint.create_associated_token_account(pubkey_receiver)
            val = await mint.transfer(account, receiver, pubkey_owner, amount)
            return val
        except solana.exceptions.SolanaRpcException:
            print("Transfer error!")

async def metadata_transaction(tokenname: str, tokenticker: str, jsonurl: str, mint: spl, pubkey: str, privkey: str):
    client = AsyncClient(getenv("RPC"))
    if not await client.is_connected():
        return None
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
                "sellerFeeBasisPoints": 500,
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
        blockhash = await client.get_latest_blockhash()
        tx.recent_blockhash = blockhash.value.blockhash
        tx.sign(kp)
        val = await client.send_raw_transaction(tx.serialize())
        return val
    except solana.exceptions.SolanaRpcException:
        return None

