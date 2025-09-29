# bitquery-corecast-proto

A Python package containing gRPC protobuf definitions and generated Python code for Bitquery CoreCast Solana gRPC.

## Installation

```bash
pip install bitquery-corecast-proto
```

## Quick Start

```python
import grpc
from bitquery_corecast_proto import corecast_pb2, corecast_pb2_grpc
from bitquery_corecast_proto import stream_message_pb2

# Import Solana protobuf definitions
from solana import token_block_message_pb2, dex_block_message_pb2

# Create gRPC channel and stub
channel = grpc.insecure_channel('localhost:50051')
stub = corecast_pb2_grpc.CoreCastStub(channel)

# Make gRPC calls
request = corecast_pb2.StreamRequest()
response = stub.StreamMessages(request)
```

## Available Modules

- `bitquery_corecast_proto.corecast_pb2` - Core request/response messages
- `bitquery_corecast_proto.corecast_pb2_grpc` - gRPC service stubs
- `bitquery_corecast_proto.stream_message_pb2` - Stream message definitions
- `bitquery_corecast_proto.request_pb2` - Request message definitions

## Solana Dependencies

This package automatically installs `bitquery-pb2-kafka-package` which provides:
- `solana.token_block_message_pb2` - Token block messages
- `solana.dex_block_message_pb2` - DEX block messages
- `solana.parsed_idl_block_message_pb2` - Parsed IDL block messages
- `solana.block_message_pb2` - Block messages

## Requirements

- Python 3.8+
- grpcio>=1.60.0
- grpcio-tools>=1.60.0
- protobuf>=6.30.0,<7.0.0
- bitquery-pb2-kafka-package

## License

MIT License - see LICENSE file for details.
