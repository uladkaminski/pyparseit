#!/bin/bash

# Clean previous builds (optional but recommended)                                                                                           ─╯
rm -rf build/ dist/ *.egg-info

# Build the package
python setup.py sdist bdist_wheel
