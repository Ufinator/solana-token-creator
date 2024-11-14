# Solana Token Creator
In progress...

# Test- & Mainnet fixes
There is right know a problem inside the dependency "Solana.py" (It throws in Testnet sometimes and in Mainnet often the error "SolanaRPCException"). The problem has been fixed, when the following codes inside "Solana.py" gets changed:

http.py:
```
%PYTHON_VENV%\Lib\site-packages\solana\rpc\providers\http.py
```
In this file, inside the function `def make_request_unparsed(...)` the line/code `raw_response = httpx.post(**request_kwargs)` needs an additional argument: `timeout=None`. Edit the code like this:

`raw_response = httpx.post(**request_kwargs, timeout=None)`

api.py:
```
%PYTHON_VENV%\Lib\site-packages\solana\rpc\api.py
```
There, you should change the default `sleep_seconds` in `def confirm_transaction(
        ...
        sleep_seconds: float = 0.1
        ...
)` to 5 like this:

`def confirm_transaction(
        ...
        sleep_seconds: float = 5
        ...
)` 

Save and the problem should be fixed. 

*I will maybe get in touch with the creator to get this fixed*