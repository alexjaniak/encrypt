from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='encrypt',
    version='1.0',
    description="CLI for Encrypting & Decrypting Files",
    long_description= (Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="alexjaniak",
    license="MIT 2021",
    url="https://github.com/alexjaniak/encrypt",
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pycryptodome'
    ],
    entry_points={
        'console_scripts': [
            'encrypt = encrypt.main:encrypt',
            'decrypt = encrypt.main:decrypt'
        ],
    },
)