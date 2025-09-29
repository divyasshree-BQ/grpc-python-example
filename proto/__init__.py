"""
gRPC Proto Package

This package contains generated Python protobuf classes for CoreCast gRPC services.
It includes definitions for streaming Solana blockchain data.

Usage:
    from proto import corecast_pb2, corecast_pb2_grpc
    from proto.solana.corecast import stream_message_pb2
"""

__version__ = "1.0.1"

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
