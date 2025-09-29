#!/usr/bin/env python3
"""Setup script for bitquery-corecast-proto package."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="bitquery-corecast-proto",
    version="1.0.2",
    author="Divyasshree",
    author_email="divyasshree@bitquery.io",
    description="gRPC protobuf definitions and generated Python code for Bitquery CoreCast Solana gRPC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.bitquery.io/docs/category/grpc-streams/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": ["*.proto"],
    },
    zip_safe=False,
)
