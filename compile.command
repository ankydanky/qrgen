#! /bin/bash

rm -rf build
rm -rf dist

pyinstaller --windowed QRGen.py
