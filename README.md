# CoreCast Python Client

A Python gRPC client for streaming Solana blockchain data from Bitquery's CoreCast service.

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

## Authentication Setup

The application requires a BitQuery CoreCast authorization token. For security, tokens are managed through environment variables.

### Setting up your authorization token:

1. **Set the environment variable:**
   ```bash
   export AUTHORIZATION_TOKEN="your_authorization_token_here"
   ```

2. **Or create a `.env` file in the project root:**
   ```bash
   echo "AUTHORIZATION_TOKEN=your_authorization_token_here" > .env
   ```

3. **For permanent setup, add to your shell profile:**
   ```bash
   echo 'export AUTHORIZATION_TOKEN="your_authorization_token_here"' >> ~/.bashrc
   # or for zsh:
   echo 'export AUTHORIZATION_TOKEN="your_authorization_token_here"' >> ~/.zshrc
   ```

**Note:** Configuration files now use `${AUTHORIZATION_TOKEN}` placeholder instead of hardcoded tokens for security.

## Run

### Using default configuration (dex_trades):
```bash
python3 main.py
```

### Using specific configuration:
```bash
python3 main.py --config ./configs/dex_trades.yaml
python3 main.py --config ./configs/transactions.yaml
```

### Filters

⚠️ **Important**: At least one filter must be specified for each stream type. Subscriptions without filters will be rejected.

#### Filter logic:
```
(program IN filter.programs) AND (pool IN filter.pools) AND (token IN filter.tokens)
```

## Configuration

All parameters are loaded from YAML configuration files located in the `configs/` directory.

### Available configurations:

- `configs/dex_trades.yaml` - DEX trades **filters**: *program, token, pool, trader*
- `configs/dex_orders.yaml` - DEX orders **filters**: *program, token, pool, trader*
- `configs/dex_pools.yaml` - DEX pools **filters**: *program, token, pool*
- `configs/transfers.yaml` - Transfers **filters**: *sender, receiver, token*
- `configs/balances.yaml` - Balance updates **filters**: *address, token*
- `configs/transactions.yaml` - Parsed transactions **filters**: *signer*

## Configuration format

All configuration files follow this structure:

```yaml
server:
  address: "corecast.bitquery.io"
  insecure: false            # if false, TLS will be used
  authorization: "${AUTHORIZATION_TOKEN}"  # environment variable; sent as metadata 'authorization'

stream:
  type: "dex_trades"  # or dex_orders, dex_pools, transactions, transfers, balances
  
filters:
  # DEX filters (for dex_trades, dex_orders, dex_pools), Transaction
  programs:
    - "9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin"
  pools:
    - "Hf6c2L9H8iQy2f5uF5eBkQK2A2c6R7FZ8pCkU9D1ABCD"
  tokens:
    - "So11111111111111111111111111111111111111112"  # SOL
  traders: # not for dex_pools
    - "7GJz9X7b1G9Nf1d5uQq2Z3B4nPq6F8d9LmNoPQrsTUV"
    
  # Transfer filters (for transfers)
  senders:
    - "DSqMPMsMAbEJVNuPKv1ZFdzt6YvJaDPDddfeW7ajtqds"
  receivers:
    - "ReceiverAddressHere..."
    
  # Balance filters (for balances)
  addresses:
    - "DSqMPMsMAbEJVNuPKv1ZFdzt6YvJaDPDddfeW7ajtqds"
    
  # Transaction filters (for transactions)
  signers:
    - "ETcW7iuVraMKLMJayNCCsr9bLvKrJPDczy1CMVMPmXTc"
```

## Examples

### DEX Trades with multiple programs:
```yaml
# configs/dex_trades.yaml
filters:
  programs:
    - "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"  # Prism AMM
    - "SoLFiHG9TfgtdUXUjWAxi3LtvYuFyDLVhBWxdMZxyCe"  # SolFi
  tokens:
    - "So11111111111111111111111111111111111111112"  # SOL
```

### Transfers from specific sender:
```yaml  
# configs/transfers.yaml
filters:
  senders:
    - "DSqMPMsMAbEJVNuPKv1ZFdzt6YvJaDPDddfeW7ajtqds"
  tokens:
    - "So11111111111111111111111111111111111111112"  # SOL
    - "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"  # USDC
```

### Balance updates for specific address:
```yaml
# configs/balances.yaml  
filters:
  addresses:
    - "DSqMPMsMAbEJVNuPKv1ZFdzt6YvJaDPDddfeW7ajtqds"
  tokens:
    - "So11111111111111111111111111111111111111112"  # SOL
```

### Transactions from specific signer:
```yaml
# configs/transactions.yaml
filters:
  signers:
    - "ETcW7iuVraMKLMJayNCCsr9bLvKrJPDczy1CMVMPmXTc"
```

## Additional Options

### Log Level
```bash
python main.py --log-level DEBUG
```

Available log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`

## Programmatic Usage

```python
from config import load_config
from client import CoreCastClient

# Load configuration
config = load_config('configs/dex_trades.yaml')

# Create and connect client
client = CoreCastClient(config)
client.connect()

# Stream data
client.stream_dex_trades()

# Close connection
client.close()
```

## Requirements

- Python 3.7+
- gRPC Python libraries
- PyYAML for configuration
- base58 for address encoding
- bitquery-pb2-kafka-package for Solana protobuf definitions
