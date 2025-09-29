"""
Bitquery CoreCast Proto Package

This package contains generated Python protobuf classes for Bitquery CoreCast gRPC services.
It includes definitions for streaming Solana blockchain data.

Usage:
    from bitquery_corecast_proto import corecast_pb2, corecast_pb2_grpc
    from bitquery_corecast_proto import stream_message_pb2
    from solana import token_block_message_pb2, dex_block_message_pb2
"""

__version__ = "1.0.3"

# Import main protobuf modules for easy access
try:
    from . import corecast_pb2
    from . import corecast_pb2_grpc
    from . import request_pb2
    from . import stream_message_pb2
except ImportError:
    # Handle case where protobuf files aren't generated yet
    pass

__all__ = [
    "corecast_pb2",
    "corecast_pb2_grpc", 
    "request_pb2",
    "stream_message_pb2",
]
